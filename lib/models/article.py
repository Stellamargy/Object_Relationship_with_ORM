from lib.db import get_db_connection

class Article:
    all={}
    def __init__(self, title, author_id, magazine_id):
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id
        self._id = None

    @property
    def id(self):
        return self._id
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string.")
        if len(value) > 255:
            raise ValueError("Title must be at most 255 characters.")
        self._title = value.strip()

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise ValueError("author_id must be a positive integer or None.")
        self._author_id = value

    @property
    def magazine_id(self):
        return self._magazine_id

    @magazine_id.setter
    def magazine_id(self, value):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise ValueError("magazine_id must be a positive integer or None.")
        self._magazine_id = value
    def __repr__(self):
        return f"Article(title={self.title}, author_id={self.author_id}, magazine_id={self.magazine_id}, id={self.id})"
    
    def validate_foreign_keys(self,author_id, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM authors WHERE id = ?", (author_id,))
        if cursor.fetchone() is None:
            raise ValueError("Invalid author_id: no such author exists.")
        cursor.execute("SELECT id FROM magazines WHERE id = ?", (magazine_id,))
        if cursor.fetchone() is None:
            raise ValueError("Invalid magazine_id: no such magazine exists.")
        cursor.close()
        conn.close()

    def save(self):
        """Save the article to the database."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            if self.id is None:
                self.validate_foreign_keys(self.author_id, self.magazine_id)
                cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                               (self.title, self.author_id, self.magazine_id))
                self._id = cursor.lastrowid
                conn.commit()
                Article.all[self.id] = self
        finally:
            cursor.close()
            conn.close()
    def update_article(self, title, author_id, magazine_id):
        """Update the article in the database."""
        if self.id is None:
            raise ValueError("Cannot update an article that has not been saved.")
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            self.validate_foreign_keys(self.author_id, self.magazine_id)
            cursor.execute("UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?", 
                           (title, author_id, magazine_id, self.id))
            conn.commit()
            Article.all[self.id] = self
        finally:
            cursor.close()
            conn.close()
    def delete(self):
        """Delete the article from the database."""
        if self.id is None:
            raise ValueError("Cannot delete an article that has not been saved.")
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
            conn.commit()
            del Article.all[self.id]
            self._id = None
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def create_article(cls, title, author_id, magazine_id):
        """Create a new article and save it to the database."""
        article = cls(title, author_id, magazine_id)
        article.save()
        return article
    @classmethod
    def get_article_instance(cls,row):
        """Create an article instance from a database row."""
        article = cls.all.get(row["id"])
        if article is None:
            article = cls(row["title"], row["author_id"], row["magazine_id"])
            article._id = row["id"]
            cls.all[article.id] = article
        else:
            article.title = row["title"]
            article.author_id = row["author_id"]
            article.magazine_id = row["magazine_id"]
            article._id = row["id"]
        return article
    @classmethod
    def get_all_articles(cls):
        """Retrieve all articles from the database."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles")
            rows = cursor.fetchall()
            articles = [cls.get_article_instance(row) for row in rows]
            return articles
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def find_article_by_id(cls, article_id):
        """Find an article by its ID."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
            row = cursor.fetchone()
            if row is None:
                return "No article found with that ID."
            return cls.get_article_instance(row)
        finally:
            cursor.close()
            conn.close()  
    @classmethod
    def find_article_by_title(cls,title):
        """Find an article by its title."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
            row = cursor.fetchone()
            if row is None:
                return "No article found with that title."
            return cls.get_article_instance(row)
        finally:
            cursor.close()
            conn.close()

    
    

    
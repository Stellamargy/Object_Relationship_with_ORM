from lib.db import get_db_connection, get_db_cursor

class Author():
    all={}
    def __init__(self, name):
        self.name = name
        self._id=None
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value.strip()

    def __repr__(self):
        return f"Author(name={self.name}, id={self.id})"
    

    def save(self):
        """Save the author to the database."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
                self._id = cursor.lastrowid
                conn.commit()
                Author.all[self.id] = self
           
        finally:
            cursor.close()
            conn.close()

    
    @classmethod
    def get_instance_from_db(cls,row):
        #check if the instance is in the cache
        author =cls.all.get(row['id'])
        if author:
            #if the instance is in the cache, make sure data was not changed
            author._name = row['name']

        #if the instance is not in the cache, create a new instance     
        else:
            author=cls(name=row['name'])
            author._id = row['id']
            #add the instance to the cache
            cls.all[author.id] = author
        return author

    @classmethod
    def find_author_by_id(cls, author_id):
        """Find an author by ID."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
            row = cursor.fetchone()
            if row:
                return cls.get_instance_from_db(row)
            return "No author found with that ID."
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def find_author_by_name(cls, name):
        """Find an author by name."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
            row = cursor.fetchone()
            if row:
                return cls.get_instance_from_db(row)
            return "No author found with that name."
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def get_all_authors(cls):
        """Get all authors from the database."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            rows = cursor.fetchall()
            authors = [cls.get_instance_from_db(row) for row in rows]
            return authors
        finally:
            cursor.close()
            conn.close()

    def update(self,name):
        """Update the author's name."""
        self.name = name.strip()
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))
            conn.commit()
            Author.all[self.id] = self  
        finally:
            cursor.close()
            conn.close()

    def delete(self):
        """Delete the author from the database."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM authors WHERE id = ?", (self.id,))
            conn.commit()
            del Author.all[self.id]  # Remove from cache
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def create_author(cls, name):
        """Create a new author."""
        author = cls(name)
        author.save()
        return author
    






    


   

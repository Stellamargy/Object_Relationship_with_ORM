from lib.db import get_db_connection
class Magazine():
    all = {}
    def __init__(self,name,category):
        self.name = name
        self.category = category
        self._id = None
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 1:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) < 1:
            raise ValueError("Category cannot be empty")
        self._category = value

    def __repr__(self):
        return f"Magazine(title={self.name}, category={self.category}, id={self.id})"
    
    def save(self):
        """Save the magazine to the database."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
                self._id = cursor.lastrowid
                conn.commit()
                Magazine.all[self.id] = self
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def create_magazine(cls, name, category):
        """Create a new magazine and save it to the database."""
        magazine = cls(name, category)
        magazine.save()
        return magazine
    def delete_magazine(self):
        """Delete the magazine from the database."""
        if self.id is None:
            raise ValueError("Cannot delete a magazine that has not been saved.")
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM magazines WHERE id = ?", (self.id,))
            conn.commit()
            del Magazine.all[self.id]
        finally:
            cursor.close()
            conn.close()
    def update(self, name=None, category=None):
        """Update the magazine's name and/or category."""
        if self.id is None:
            raise ValueError("Cannot update a magazine that has not been saved.")
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        conn=get_db_connection()
        
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", (self.name, self.category, self.id))
            conn.commit()
            Magazine.all[self.id] = self
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def get_magazine_instance(cls,row):
        """Create a magazine instance from a database row."""
        magazine=cls.all.get(row["id"])
        if magazine is None:
            magazine = cls(row["name"], row["category"])
            magazine._id = row["id"]
            cls.all[magazine.id] = magazine
        else:
            magazine.name = row["name"]
            magazine.category = row["category"]
        return magazine
    @classmethod
    def get_all_magazines(cls):
        """Retrieve all magazines from the database."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines")
            rows = cursor.fetchall()
            return [cls.get_magazine_instance(row) for row in rows]
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def find_magazine_by_id(cls, id):
        """Find a magazine by its ID."""
        if id in cls.all:
            return cls.all[id]
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return "No magazine found with that ID."
            return cls.get_magazine_instance(row)
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def find_magazine_by_name(cls, name):
        """Find a magazine by its name."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
            row = cursor.fetchone()
            if row is None:
                return "No magazine found with that name."
            return cls.get_magazine_instance(row)
        finally:
            cursor.close()
            conn.close()

        
        








    


    



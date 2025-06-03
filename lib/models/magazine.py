from lib.db import get_db_connection, get_db_cursor
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
   




    


    



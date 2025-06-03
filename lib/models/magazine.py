from lib.db import get_db_connection, get_db_cursor
class Magazine():
    def __init__(self,title,category):
        self.title = title
        self.category = category
        self._id = None
    @property
    def id(self):
        return self._id
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if len(value) < 1:
            raise ValueError("Title cannot be empty")
        self._title = value

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

    
    

    



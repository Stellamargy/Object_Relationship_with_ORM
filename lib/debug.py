from lib.models import Author
from lib.db import get_db_connection,get_db_cursor
from lib.models.magazine import Magazine
#test save method for Author model
# author_001=Author(name="John Doe")
# author_001.save()
#test create_author method for Author model
# Author.create_author("Stella Margy")
#test get_all_authors method for Author model
# authors=Author.get_all_authors()
# print(authors)
#test get_author_by_id method for Author model
# author=Author.find_author_by_id(1)
# print(author)
#test get_author_by_name method for Author model
# author=Author.find_author_by_name("Esther Oloo")
# print(author)
#update author name

# author.update("Esther Oloo")
# author.delete()

#test delete method for Author model
# author.delete()


magazine_001=Magazine("Tech Today", "Technology")
magazine_001.save()
#test create_magazine method for Magazine model
Magazine.create_magazine("Health Weekly", "Health")



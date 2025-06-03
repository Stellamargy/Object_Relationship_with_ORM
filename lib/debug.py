from lib.models import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
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


# magazine_001=Magazine("Tech Today", "Technology")
# magazine_001.save()
#test create_magazine method for Magazine model
# Magazine.create_magazine("Health Weekly", "Health")
# travel=Magazine.create_magazine("Travel Explorer", "Travel")
# # travel.update(name="Travel Adventures", category="Adventure")
# print(travel)
# travel.update(name="The Standard", category="Adventure")
# # travel.delete_magazine()  
# travel.delete_magazine()
# magazines=Magazine.get_all_magazines()
# print(magazines)
# magazine=Magazine.find_magazine_by_id(1)
# print(magazine)
# magazine2=Magazine.find_magazine_by_name("Tech Today")
# print(magazine2)

article1=Article("The Future of AI", 1, 1)
article1.save()
article2=Article("Climate Change and You", 100, 1111)
article2.save()  



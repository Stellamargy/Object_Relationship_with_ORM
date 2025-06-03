from lib.models import Author
from lib.db import get_db_connection,get_db_cursor
# import os



    
#Create a function to run a SQL file to set up the database schema
# def set_db_schema(schema):
#     """db connection and run a SQL file to set up the database schema."""
#     conn=get_db_connection()  
#     cursor=get_db_cursor()  
   
#     base_dir = os.path.dirname(__file__)
#     sql_file_path = os.path.join(base_dir, schema)

#     with open(sql_file_path, 'r') as f:
#         sql_script = f.read()

#     cursor.executescript(sql_script)
#     conn.commit()
#     conn.close()





# # Author.create_author(name="Stella Margy")
# #Test save method in Author Class
# stella = Author(name="Stella Margy")
# # stella.save()
# stella.delete
# #Test create author method
# # Author.create_author("Moffat Oloo")
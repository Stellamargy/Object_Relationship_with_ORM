from .connection import get_db_connection, get_db_cursor
import os



def run_sql_file(schema):
    """db connection and run a SQL file to set up the database schema."""
    conn=get_db_connection()  
    cursor=get_db_cursor()  
   
    base_dir = os.path.dirname(__file__)
    sql_file_path = os.path.join(base_dir, schema)

    with open(sql_file_path, 'r') as f:
        sql_script = f.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()



# Seed data for authors
authors = [
    (1, "Alice Johnson"),
    (2, "Bob Smith"),
    (3, "Catherine Lee"),
    (4, "David Kim"),
    (5, "Eva Brown"),
]

# Seed data for magazines
magazines = [
    (1, "Tech Today", "Technology"),
    (2, "Health Weekly", "Health"),
    (3, "Travel Explorer", "Travel"),
    (4, "Food Lovers", "Food"),
    (5, "Business Insights", "Business"),
]

# Seed data for articles
articles = [
    (1, "The Rise of AI", 1, 1),
    (2, "Healthy Living Tips", 2, 2),
    (3, "Exploring the Alps", 3, 3),
    (4, "Gourmet Recipes", 4, 4),
    (5, "Startup Success Stories", 5, 5),
    (6, "Quantum Computing Explained", 1, 1),
    (7, "Mental Health Matters", 2, 2),
    (8, "Backpacking Southeast Asia", 3, 3),
    (9, "Vegan Delights", 4, 4),
    (10, "Investing in 2024", 5, 5),
]



# Seed data
articles = [
    (1, "The Rise of AI", 1, 1),
    (2, "Healthy Living Tips", 2, 2),
    (3, "Exploring the Alps", 3, 3),
    (4, "Gourmet Recipes", 4, 4),
    (5, "Startup Success Stories", 5, 5),
    (6, "Quantum Computing Explained", 1, 1),
    (7, "Mental Health Matters", 2, 2),
    (8, "Backpacking Southeast Asia", 3, 3),
    (9, "Vegan Delights", 4, 4),
    (10, "Investing in 2024", 5, 5),
]

def seed_data(table_name, data, query):
    """seeding the articles, authors, and magazines tables."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.executemany(query, data)
        conn.commit()
    finally:
        cursor.close()

def seed_authors():
    seed_data(
        "authors",
        authors,
        "INSERT OR IGNORE INTO authors (id, name) VALUES (?, ?);"
    )

def seed_magazines():
    seed_data(
        "magazines",
        magazines,
        "INSERT OR IGNORE INTO magazines (id, name, category) VALUES (?, ?, ?);"
    )

def seed_articles():
    seed_data(
        "articles",
        articles,
        "INSERT OR IGNORE INTO articles (id, title, author_id, magazine_id) VALUES (?, ?, ?, ?);"
    )

#create the database schema and seed the data
run_sql_file('schema.sql')
seed_authors()
seed_magazines()
seed_articles()

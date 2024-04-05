import psycopg2
from psycopg2 import sql

# List of database connection strings
DATABASE_URLS = [
    "postgres://lddwokth:mJvHU-ZoB_5_dvqP_43CM_YWeDIWv9Jf@isilo.db.elephantsql.com/lddwokth", #AuthorDB
    "postgres://hdxwvmpg:GcZMUqM7HoeEYP9cvmxGLR-ufqlqC1Ss@bubble.db.elephantsql.com/hdxwvmpg", #BookDB
]

# SQL command to create the "bike" table
#create_table_command = sql.SQL("""
#CREATE TABLE IF NOT EXISTS bike (
#    bike_id SERIAL PRIMARY KEY,
#    bike_model VARCHAR(255) NOT NULL,
#    bike_price DECIMAL(10, 2)
#)
#""")


# SQL command to create the "author" and "book" table
create_table_command = sql.SQL("""
CREATE TABLE IF NOT EXISTS author (
    author_id SERIAL PRIMARY KEY,
    author_fn VARCHAR(255) NOT NULL,
    author_ln VARCHAR(255) NOT NULL
);                         
CREATE TABLE IF NOT EXISTS book (
    book_id SERIAL PRIMARY KEY,
    book_name VARCHAR(255) NOT NULL,
    author_id INTEGER NOT NULL
);                         
""")

# Function to create table in a given database
def create_table_in_database(db_url):
    try:
        # Connect to the database using the database URL
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        # Execute the create table command
        cur.execute(create_table_command)
        
        # Commit the changes
        conn.commit()
        
        print("Table 'bike' created successfully in database:", db_url)
        
    except psycopg2.DatabaseError as e:
        print(f"An error occurred in database {db_url}: {e}")
    finally:
        # Close communication with the database
        if cur: cur.close()
        if conn: conn.close()

# Iterate over each database URL and create the table
for db_url in DATABASE_URLS:
    create_table_in_database(db_url)

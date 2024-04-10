import psycopg2
from book_data import books_to_insert
from author_data import authors_to_insert

DATABASE_URLS = {
    'AuthorDB': "postgres://lddwokth:mJvHU-ZoB_5_dvqP_43CM_YWeDIWv9Jf@isilo.db.elephantsql.com/lddwokth",
    'BookDB': "postgres://hdxwvmpg:GcZMUqM7HoeEYP9cvmxGLR-ufqlqC1Ss@bubble.db.elephantsql.com/hdxwvmpg"
}

def insert_book_into_database(book_data):

    book_id, book_name, author_id, book_summary = book_data

    
    # Define the insert command template
    insert_command = """
    INSERT INTO book (book_id, book_name, author_id, book_summary) VALUES (%s, %s, %s, pgp_sym_encrypt(%s, 'secret'));
    """
    
    #for role, database_url in DATABASE_URLS.items():
    database_url = DATABASE_URLS['BookDB']
    try:
        # Connect to the database
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
                    
        # Execute the insert command
        cur.execute(insert_command, book_data)
        conn.commit()
        print(f"Book {book_id} named '{book_name}' inserted successfully into '{database_url}' database.")
        
    except psycopg2.DatabaseError as e:
        print(f"An error occurred with the '{database_url}' database: {e}")
    finally:
        # Ensure that the database connection is closed
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()


def insert_author_into_database(author_data):

    author_id, author_fn, author_ln = author_data
    
    # Define the insert command template
    insert_command = """
    INSERT INTO author (author_id, author_fn, author_ln) VALUES (%s, %s, %s);
    """
    
    #for role, database_url in DATABASE_URLS.items():
    database_url = DATABASE_URLS['AuthorDB']
    try:
        # Connect to the database
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
            
        '''
        # Insert the book into the table, adjusting price visibility based on the role
        if role == 'AuthorDB':
            values = ( )
        else:
            values = ( )
        '''
        
        # Execute the insert command
        cur.execute(insert_command, author_data)
        conn.commit()
        print(f"Author {author_id} named '{author_fn}' '{author_ln}' inserted successfully into '{database_url}' database.")
        
    except psycopg2.DatabaseError as e:
        print(f"An error occurred with the '{database_url}' database: {e}")
    finally:
        # Ensure that the database connection is closed
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()


'''
books_to_insert = []

book_file = open("book_data.py", "r")

for book in book_file:
    books_to_insert.append(book)
    print('**', book)
'''

for book in books_to_insert:
    insert_book_into_database(book)

for author in authors_to_insert:
    insert_author_into_database(author)
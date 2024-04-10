import psycopg2
import time

DATABASE_URLS = {
    'AuthorDB': "postgres://lddwokth:mJvHU-ZoB_5_dvqP_43CM_YWeDIWv9Jf@isilo.db.elephantsql.com/lddwokth",
    'BookDB': "postgres://hdxwvmpg:GcZMUqM7HoeEYP9cvmxGLR-ufqlqC1Ss@bubble.db.elephantsql.com/hdxwvmpg"
}

def run_slow_query(db_url, slow_query):
    try:
        # Connect to the database
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()

        # Execute the create table command
        cur.execute(slow_query)
        
        # Commit the changes
        conn.commit()

        print("Slow query executed successfully:", db_url)
        
    except psycopg2.DatabaseError as e:
        print(f"An error occurred in database {db_url}: {e}")
    finally:
        # Close communication with the database
        if cur: cur.close()
        if conn: conn.close()

# A slow query: Intentionally using inefficient LIKE pattern matching and a cross JOIN which multiplies the number of rows.
slow_query = """
SELECT *
    FROM book
    WHERE book_name = 'To Kill a Mockingbird'
    AND author_id = 2
"""
run_slow_query(DATABASE_URLS["BookDB"], slow_query)
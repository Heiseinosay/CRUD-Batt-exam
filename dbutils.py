from mysql.connector import (connection)
from mysql.connector import Error

# DB CONNECTION
def connect_to_db():
    try:
        print("Attempting to connect...")

        mysqldb = connection.MySQLConnection(
            user='root', 
            password='HelloWorld#,12345',                   
            host='localhost',
            database='bookshop' # Use Existing Database
        )
        
        print("Connection successful!")

        # Cursor
        cursor = mysqldb.cursor()

        # Create Database
        # cursor.execute("CREATE DATABASE IF NOT EXISTS bookshop")
        
        # USE Database
        # cursor.execute("USE bookshop")

        return mysqldb, cursor

    except Error as e:
        print(f"Error: {e}")

# CREATE
def create_table():
    mysqldb, cursor = connect_to_db()
    try:
        # Create Table
        cursor.execute(
            """
            Create Table tblbooks(
                BookID INT PRIMARY KEY AUTO_INCREMENT,
                Title VARCHAR(255),
                Genre VARCHAR(255),
                PublicationDate DATE
            )

            """
        )
        print("Table Created!!!")
    except Error as e:
            print(f"Error creating table: {e}")
    finally:
        mysqldb.close()

# SELECT
def search_row(search_term):
    print("searching")
    mysqldb, cursor = connect_to_db()
    try:
       # Correct the query by replacing %s% with %s and formatting the term with wildcards
        read_query = 'SELECT * FROM tblbooks WHERE Title LIKE %s'
        
        # Pass search_term as a tuple with wildcards added
        cursor.execute(read_query, (f"%{search_term}%",))
        
        # Fetch results
        result = cursor.fetchall()
        return result
    except Error as e:
            print(f"Error in searching: {e}")
    finally:
        mysqldb.close()


# DISPLAY ALL
def display():
    mysqldb,cursor = connect_to_db()
    try:
        read_query = "SELECT * FROM tblBooks"
        cursor.execute(read_query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error in selecting: {e}")
    finally:
        mysqldb.close()


# ADD
def insert_row(title, genre, date):
    mysqldb,cursor = connect_to_db()
    try:
        insert_query = 'INSERT INTO tblBooks(Title, Genre, PublicationDate) VALUES (%s, %s, %s)' 
        record = (title, genre, date)
        cursor.execute(insert_query, record)

        mysqldb.commit()
        print("Successfully inserted!")
        return {'status' : 'success'}
    except Error as e:
            print(f"Error in inserting: {e}")
    finally:
        mysqldb.close()


# DELETE
def delete_row(bookID):
    mysqldb, cursor = connect_to_db()
    try:
        delete_query = 'DELETE FROM tblBooks WHERE bookID = %s'
        cursor.execute(delete_query, (bookID,))
        mysqldb.commit()

        print("Successfully Deleted!")
        return {'status' : 'deleted'}
    except Error as e:
        print(f"Error in deleting: {e}")
        return {'status': 'error', 'message': str(e)}
    finally:
        mysqldb.close()


# SELECT
def search_for_id(book_id):
    print("searching")
    mysqldb, cursor = connect_to_db()
    try:
       # Correct the query by replacing %s% with %s and formatting the term with wildcards
        read_query = 'SELECT * FROM tblbooks WHERE bookID = %s'
        
        # Pass search_term as a tuple with wildcards added
        cursor.execute(read_query, (book_id,))
        
        # Fetch results
        result = cursor.fetchall()
        return result
    except Error as e:
            print(f"Error in searching: {e}")
    finally:
        mysqldb.close()

# UPDATE
def update_row(book_id, title, genre, date):
    print("Updating!!!")
    mysqldb, cursor = connect_to_db()
    try:
        update_query = 'Update tblBooks SET title = %s, genre = %s, PublicationDate = %s WHERE bookID = %s'
        cursor.execute(update_query, (title, genre, date, book_id))
        mysqldb.commit()

        return {'status' : 'success'}
    except Error as e:
            print(f"Error in updating: {e}")
    finally:
        mysqldb.close()
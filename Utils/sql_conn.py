# Utils/sql_conn.py
import mysql.connector
from mysql.connector import Error

def connect():
    """Establish and return a connection to the MySQL database using mysql-connector."""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',  # Localhost
            port=3306,  # Default MySQL port
            user='root',  # MySQL root user
            password='powerdata',  # Your MySQL password
            database=''  # Can be left blank if no default schema is needed
        )
        if connection.is_connected():
            print("Successfully connected to the MySQL database.")
            return connection
    except Error as e:
        print(f"Error connecting to the MySQL database: {e}")
        return None

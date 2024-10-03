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
            database=''  # No default database, will select manually
        )
        if connection.is_connected():
            print("Successfully connected to the MySQL database.")
            return connection
    except Error as e:
        print(f"Error connecting to the MySQL database: {e}")
        return None

def drop_all_tables(connection):
    """Drop all tables from the current database."""
    try:
        cursor = connection.cursor()

        # Query to get all table names
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        # Drop each table
        for table in tables:
            drop_table_query = f"DROP TABLE IF EXISTS `{table[0]}`;"
            cursor.execute(drop_table_query)
            print(f"Dropped table: {table[0]}")

        connection.commit()
        cursor.close()
        print("Successfully dropped all tables.")
    except Exception as e:
        print(f"Error dropping tables: {e}")

if __name__ == "__main__":
    connection = connect()

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("USE `PowerData`;")  
            print("Connected to PowerData database.")
            cursor.close()

            # Call the function to drop all tables
            drop_all_tables(connection)

        except Exception as e:
            print(f"Error selecting database: {e}")
        finally:
            connection.close()
    else:
        print("Failed to connect to the database.")

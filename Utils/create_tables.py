import json
import os
from sql_conn import connect

def select_database(connection, db_name):
    """Select the database before executing any SQL commands."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE `{db_name}`;")
        print(f"Database selected: {db_name}")
    except Exception as e:
        print(f"Error selecting database: {e}")

def execute_sql_script(connection, sql_file):
    """Execute the SQL script from the given file to create tables."""
    try:
        with open(sql_file, 'r') as file:
            sql_script = file.read()

        cursor = connection.cursor()
        for result in cursor.execute(sql_script, multi=True):
            if result.with_rows:
                print(f"Executed a statement from {sql_file}: {result.statement}")
        print(f"Successfully executed: {sql_file}")
        cursor.close()
    except Exception as e:
        print(f"Error executing {sql_file}: {e}")

def create_tables():
    """Read the sql_file_paths.json and execute each SQL script to create tables."""
    try:
        with open('Assets/sql_create_queries_file_paths.json', 'r') as json_file:
            sport_sql_files = json.load(json_file)

        connection = connect()

        if connection:
            # Select the PowerData database
            select_database(connection, 'PowerData')
            
            for sport, sql_files in sport_sql_files.items():
                print(f"Creating tables for {sport}...")
                for category, sql_file in sql_files.items():
                    if os.path.exists(sql_file):
                        print(f"Executing {category}: {sql_file}")
                        execute_sql_script(connection, sql_file)
                    else:
                        print(f"SQL file not found: {sql_file}")
            
            connection.close()
        else:
            print("Failed to connect to the database.")
    except Exception as e:
        print(f"Error in create_tables: {e}")

if __name__ == "__main__":
    create_tables()

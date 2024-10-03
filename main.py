import os
import json
import pandas as pd
from Utils.sql_conn import connect

# Load the SQL file paths from the JSON file
with open('Assets/sql_file_paths.json', 'r') as file:
    SQL_FILE_PATHS = json.load(file)

# Example: Squad ID mapping to sports (modify this based on your actual squad IDs)
SQUAD_ID_MAPPING = {
    '1': 'AFL Mens',
    '2': 'AFL Womens',
    '3': 'NRL Mens',
    '4': 'NRL Womens',
    '5': 'Fast5 Mens',
    '6': 'Fast5 Womens',
    '7': 'Netball Mens',
    '8': 'Netball NZ Womens',
    '9': 'Netball Australian Womens',
    '10': 'Netball International Womens',

}

# Function to execute SQL script
def execute_sql_script(cursor, sql_file):
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    try:
        cursor.execute(sql_script)
        print(f"SQL script {sql_file} executed successfully.")
    except Exception as e:
        print(f"Error executing SQL script {sql_file}: {e}")

# Function to process data by identifying squad ID from the CSV file
def process_csv_by_squad_id(csv_file, cursor):
    # Read the CSV to find squad IDs (assuming squad_id is in the CSV)
    df = pd.read_csv(csv_file)
    
    if 'squad_id' not in df.columns:
        print(f"squad_id column not found in {csv_file}")
        return
    
    # Get the first squad ID in the CSV
    squad_id = str(df['squad_id'].iloc[0])  # Assuming the first squad ID is representative
    
    # Map the squad ID to the sport category
    sport_category = SQUAD_ID_MAPPING.get(squad_id)
    
    if not sport_category:
        print(f"No sport category mapping found for squad ID: {squad_id}")
        return
    
    print(f"Processing sport: {sport_category} for squad ID: {squad_id}")
    
    # Get the corresponding SQL file paths for this sport
    sport_sql_files = SQL_FILE_PATHS.get(sport_category)
    
    if not sport_sql_files:
        print(f"SQL files not available for {sport_category}")
        return
    
    # Execute each SQL file for this sport
    for sql_type, sql_file in sport_sql_files.items():
        execute_sql_script(cursor, sql_file)

# Main execution
if __name__ == "__main__":
    connection = connect()  # Connect to your SQL database
    
    if connection:
        cursor = connection.cursor()
        
        # Example: Loop through CSV files in a directory
        csv_directory = 'path_to_csv_files'  # Replace with your actual path
        for csv_file in os.listdir(csv_directory):
            if csv_file.endswith('.csv'):
                csv_path = os.path.join(csv_directory, csv_file)
                process_csv_by_squad_id(csv_path, cursor)
        
        # Commit changes and close connection
        connection.commit()
        connection.close()
        print("All SQL scripts executed successfully.")

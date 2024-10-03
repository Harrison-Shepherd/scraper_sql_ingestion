import os
import pandas as pd
from sql_conn import connect
import json

def load_csv_and_insert(connection, csv_file, sql_insert_query):
    """Loads CSV file and inserts data into the respective table."""
    try:
        print(f"Loading data from {csv_file}...")
        df = pd.read_csv(csv_file)

        # Convert NaN values to None (for SQL NULL)
        df = df.where(pd.notnull(df), None)

        cursor = connection.cursor()

        # Dynamically generate the insert query and match columns
        for index, row in df.iterrows():
            print(f"Inserting row {index + 1} into the database...")
            cursor.execute(sql_insert_query, tuple(row))

        connection.commit()
        print(f"Data from {csv_file} inserted successfully.")
        cursor.close()
    except Exception as e:
        print(f"Error inserting data from {csv_file}: {e}")

def process_csv_files(data_dir, insert_queries_json):
    """Recursively process CSV files and insert them into the respective tables."""
    try:
        connection = connect()  # Establish the DB connection
        if not connection:
            print("Failed to connect to the database.")
            return
        
        # Load the insert SQL queries from the JSON file
        print(f"Loading insert queries from: {insert_queries_json}")
        with open(insert_queries_json, 'r') as file:
            insert_queries = json.load(file)

        print(f"Starting CSV processing for directory: {data_dir}")
        for sport, sport_queries in insert_queries.items():
            sport_dir = os.path.join(data_dir, sport)  # Use the actual folder names
            if os.path.isdir(sport_dir):
                print(f"Processing data for {sport}...")

                for fixture_folder in os.listdir(sport_dir):
                    fixture_path = os.path.join(sport_dir, fixture_folder)
                    if os.path.isdir(fixture_path):
                        print(f"  Processing fixture: {fixture_folder}...")

                        # Now process the match folders inside each fixture folder
                        for match_folder in os.listdir(fixture_path):
                            match_path = os.path.join(fixture_path, match_folder)
                            if os.path.isdir(match_path):
                                print(f"    Processing match: {match_folder}...")

                                # Match Details CSV
                                match_csv = os.path.join(match_path, f'{fixture_folder} match {match_folder.split("_")[1]} details.csv')
                                if os.path.exists(match_csv):
                                    print(f"      Inserting match details from {match_csv}")
                                    load_csv_and_insert(connection, match_csv, sport_queries["match_details"])
                                else:
                                    print(f"      Match details file not found: {match_csv}")

                                # Fixture CSV (present in the fixture folder)
                                fixture_csv = os.path.join(fixture_path, f'{fixture_folder}_fixture.csv')
                                if os.path.exists(fixture_csv):
                                    print(f"      Inserting fixture details from {fixture_csv}")
                                    load_csv_and_insert(connection, fixture_csv, sport_queries["fixtures"])
                                else:
                                    print(f"      Fixture file not found: {fixture_csv}")

                                # Score Flow CSV (inside 'Additional Data' folder)
                                additional_data_path = os.path.join(match_path, 'Additional Data')
                                score_flow_csv = os.path.join(additional_data_path, f'{fixture_folder} match {match_folder.split("_")[1]} score flow.csv')
                                if os.path.exists(score_flow_csv):
                                    print(f"      Inserting score flow details from {score_flow_csv}")
                                    load_csv_and_insert(connection, score_flow_csv, sport_queries["score_flow"])
                                else:
                                    print(f"      Score flow file not found: {score_flow_csv}")

                                # Period Stats CSVs (inside 'Additional Data' folder)
                                if os.path.isdir(additional_data_path):
                                    for file in os.listdir(additional_data_path):
                                        if file.startswith(f'{fixture_folder} match {match_folder.split("_")[1]} period') and file.endswith('.csv'):
                                            period_csv = os.path.join(additional_data_path, file)
                                            print(f"      Inserting period stats from {period_csv}")
                                            load_csv_and_insert(connection, period_csv, sport_queries["period_stats"])
                                        else:
                                            print(f"      Period stats file not found: {file}")
            else:
                print(f"Sport directory not found: {sport_dir}")

        connection.close()  # Close the DB connection after processing
        print("CSV processing complete.")
    except Exception as e:
        print(f"Error processing CSV files: {e}")

# Example main function
if __name__ == "__main__":
    data_directory = "Data/Leagues"  # Path to the folder containing your CSVs
    insert_queries_json = "Assets/sql_insert_queries_file_paths.json"  # Path to the JSON file containing insert queries

    process_csv_files(data_directory, insert_queries_json)

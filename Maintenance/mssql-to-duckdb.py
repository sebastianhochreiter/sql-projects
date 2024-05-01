"""
Script: transfer_tables_to_duckdb.py
Description: This script transfers tables from a Microsoft SQL Server database to DuckDB,
             saving each table as a Parquet file and then importing it into DuckDB.
Author: Sebastian Hochreiter
Date: 01.05.2024
License: Personal Use Only
This script is provided for personal use only. Redistribution or commercial use is strictly 
prohibited without explicit permission from the author. If you intend to use this script for 
commercial purposes, please contact the author for licensing options.
"""

import pyodbc
import duckdb
import pandas as pd
from sqlalchemy import create_engine
import time
import os

def transfer_tables_to_duckdb():
    start_time = time.time()
    
    # MSSQL connection information
    mssql_server = 'localhost\\MSSQLSERVER01'
    mssql_database = 'xxx'
    mssql_username = 'xxx'
    mssql_password = 'xxx'
    
    # Establish connection to MSSQL database using SQLAlchemy
    mssql_connection_url = f"mssql+pyodbc://{mssql_username}:{mssql_password}@{mssql_server}/{mssql_database}?driver=ODBC+Driver+17+for+SQL+Server"
    engine = create_engine(mssql_connection_url)
    print("Connection to MSSQL database successful.")

    # DuckDB connection information
    duckdb_database = 'duckdb_database.db'

    # Connect to DuckDB database
    try:
        duckdb_connection = duckdb.connect(database=duckdb_database)
        print("Connection to DuckDB database successful.")
    except Exception as e:
        print(f"Error connecting to DuckDB database: {e}")
        return

    # Retrieve all table names from MSSQL database
    try:
        table_names_df = pd.read_sql_query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'", engine)
        table_names = table_names_df['TABLE_NAME'].tolist()
        print("Table names successfully retrieved:")
        print(table_names)
    except Exception as e:
        print(f"Error retrieving table names: {e}")
        return

    for table_name in table_names:
        # Fetch data from table in MSSQL
        try:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, engine)
            print(f"Data successfully fetched from table {table_name} in MSSQL.")
            
            # Create Parquet file and write data from DataFrame
            parquet_file_path = f'{table_name.replace(".", "_")}.parquet'
            df.to_parquet(parquet_file_path, index=False)
            print(f"Data successfully saved in {parquet_file_path}.")
            
            # Create table in DuckDB and import data from Parquet file
            duckdb_connection.execute(f"CREATE TABLE IF NOT EXISTS {table_name.replace('.', '_')} AS SELECT * FROM parquet_scan('{parquet_file_path}')")
            print(f"Data successfully imported from {parquet_file_path} into table {table_name.replace('.', '_')} in DuckDB.")
        except Exception as e:
            print(f"Error transferring data from table {table_name} to DuckDB: {e}")

    # Delete Parquet files
    try:
        for table_name in table_names:
            parquet_file_path = f'{table_name.replace(".", "_")}.parquet'
            os.remove(parquet_file_path)
            print(f"{parquet_file_path} successfully deleted.")
    except Exception as e:
        print(f"Error deleting Parquet files: {e}")

    duckdb_connection.close()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total execution time of the script: {total_time} seconds")

# Call the function
transfer_tables_to_duckdb()

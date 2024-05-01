import pyodbc
import duckdb
import pandas as pd
from sqlalchemy import create_engine
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import zlib

def encrypt_and_compress_data(data, password):
    # AES-Schlüssel mit 128 Bits generieren
    key = b'xxx'
    
    # Daten komprimieren
    compressed_data = zlib.compress(data.encode())
    
    # AES-Verschlüsselung
    iv = b'xxx'
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(compressed_data) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # Rückgabe von verschlüsselten Daten
    return encrypted_data

def decrypt_and_decompress_data(encrypted_data, password):
    # AES-Schlüssel mit 128 Bits generieren
    key = b'xxx'
    
    # AES-Entschlüsselung
    iv = b'xxx'
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Entfernen der Padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    
    # Daten dekomprimieren
    decompressed_data = zlib.decompress(unpadded_data).decode()
    
    # Rückgabe von dekomprimierten Daten
    return decompressed_data

def transfer_salesorderdetail_to_duckdb():
    start_time = time.time()
    
    # MSSQL Verbindungsinformationen
    mssql_server = 'localhost\\MSSQLSERVER01'
    mssql_database = 'AdventureWorks2019'
    mssql_username = 'yyy'
    mssql_password = 'zzz'
    
    # Verbindung zur MSSQL-Datenbank über SQLAlchemy herstellen
    mssql_connection_url = f"mssql+pyodbc://{mssql_username}:{mssql_password}@{mssql_server}/{mssql_database}?driver=ODBC+Driver+17+for+SQL+Server"
    engine = create_engine(mssql_connection_url)
    print("Verbindung zur MSSQL-Datenbank erfolgreich.")

    # Daten aus Sales.SalesOrderDetail in MSSQL abrufen
    try:
        query = "SELECT * FROM Sales.SalesOrderDetail"
        df = pd.read_sql(query, engine)
        print("Daten erfolgreich aus MSSQL abgerufen.")
    except Exception as e:
        print(f"Fehler beim Abrufen der Daten aus MSSQL: {e}")
        return

    # DuckDB Verbindungsinformationen
    duckdb_database = 'duckdb_database.db'

    # Verbindung zur DuckDB-Datenbank herstellen
    try:
        duckdb_connection = duckdb.connect(database=duckdb_database)
        duckdb_cursor = duckdb_connection.cursor()
        print("Verbindung zur DuckDB-Datenbank erfolgreich.")
    except Exception as e:
        print(f"Fehler beim Verbinden zur DuckDB-Datenbank: {e}")
        return

    # Parquet-Datei erstellen und Daten aus dem DataFrame schreiben
    parquet_file_path = 'SalesOrderDetail.parquet'
    try:
        # Passwort vom Benutzer eingeben lassen
        password = input("Geben Sie das Passwort für die Verschlüsselung ein: ")
        
        # Daten komprimieren und mit Passwort verschlüsseln
        encrypted_data = encrypt_and_compress_data(df.to_json(), password)

        # Parquet-Datei mit verschlüsselten Daten speichern
        with open(parquet_file_path, 'wb') as f:
            f.write(encrypted_data)

        print(f"Daten wurden erfolgreich in {parquet_file_path} mit Komprimierung und AES-Verschlüsselung gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern der Daten in Parquet: {e}")
        return

    # Tabelle in DuckDB erstellen und Daten aus der Parquet-Datei importieren
    try:
        new_table_name = 'Imported_SalesOrderDetail'
        
        # Parquet-Datei mit verschlüsselten Daten lesen und entschlüsseln
        with open(parquet_file_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = decrypt_and_decompress_data(encrypted_data, password)

        df_decrypted = pd.read_json(decrypted_data)
        duckdb_cursor.execute(f"CREATE TABLE IF NOT EXISTS {new_table_name} AS SELECT * FROM df_decrypted")
        
        print(f"Daten wurden erfolgreich aus {parquet_file_path} in die Tabelle {new_table_name} importiert.")
    except Exception as e:
        print(f"Fehler beim Importieren der Daten aus Parquet: {e}")
    finally:
        duckdb_cursor.close()
        duckdb_connection.close()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Gesamtzeit für die Ausführung des Skripts: {total_time} Sekunden")

# Funktion aufrufen
transfer_salesorderdetail_to_duckdb()

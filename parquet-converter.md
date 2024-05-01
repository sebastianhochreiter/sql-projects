# Custom project MSSQL2019 on Debian 11 converting Parquet files

```python
import pandas as pd
import pyodbc
import pyarrow as pa
import pyarrow.parquet as pq


conn = pyodbc.connect(Driver="ODBC Driver 17 for SQL Server",Server='xxx',Database='ddd',UID="yyy",PWD="zzz")

# SQL-Abfrage ausführen und Daten abrufen
query = 'SELECT * FROM Person.Person'
df = pd.read_sql(query, conn)

# Verbindung schließen
conn.close()

# Daten in Parquet-Datei speichern
pq.write_table(pa.Table.from_pandas(df), 'ausgabe2.parquet')

```

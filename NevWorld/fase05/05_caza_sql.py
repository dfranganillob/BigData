from pathlib import Path

import duckdb
import pandas as pd


DATA_DIR = Path('NevWorld/data/processed')
PARQUET_DIR = DATA_DIR / 'parquet'
PARQUET_DIR.mkdir(exist_ok=True)

names = [
    'hunts',
]

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')

prey_counts = hunts['prey_type'].value_counts()


for name in names:
    csv_path = DATA_DIR / f'{name}.csv'
    parquet_path = PARQUET_DIR / f'{name}.parquet'

    table = pd.read_csv(csv_path)
    table.to_parquet(parquet_path, engine='pyarrow', index=False)

    print(name)
    print('  CSV:', csv_path.stat().st_size, 'bytes')
    print('  Parquet:', parquet_path.stat().st_size, 'bytes')

connection = duckdb.connect()

hunt_query = """
    SELECT
        prey_type,
        COUNT(event_index) AS hunt_count
    FROM read_parquet('NevWorld/data/processed/parquet/hunts.parquet')
    GROUP BY prey_type
    ORDER BY prey_type DESC
"""

hunt_summary = connection.execute(
    hunt_query
).fetchdf()

print('\nRECURSOS CONSULTADOS CON SQL')
print(hunt_summary)

from pathlib import Path

import pandas as pd

DATASET = Path(
    'data/raw/nevworld_9549888358690311366_20261007_190831.jsonl'
)

OUTPUT_DIR = Path('data/processed')


df = pd.read_json(DATASET, lines=True)

base = ['run_id', 'event_index', 'tick']
assert all(column in df.columns for column in [*base, 'type']), \
    'Faltan columnas principales del registro'

def event_table(event_type, columns):

    selected = [*base, *columns]

    available = [column for column in selected if column in df.columns]

    table = df.loc[df['type'] == event_type, available].copy()

    table = table.reindex(columns=selected)


    table['simulation_day'] = table['tick'] // 12000

    
    return table

hunts = event_table('hunt_completed', ['villager_id', 'prey_type'])

required = [*base, 'villager_id', 'prey_type']

assert len(hunts) == (df['type'] == 'hunt_completed').sum(), \
    'El número de cacerías no coincide'

assert not hunts.duplicated(['run_id', 'event_index']).any(), \
    'Hay eventos duplicados'

if not hunts.empty:
    assert hunts[required].notna().all().all(), \
        'Hay cacerías con campos obligatorios ausentes'

assert (hunts['simulation_day'] == hunts['tick'] // 12000).all(), \
    'El día calculado es incorrecto'

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
output = OUTPUT_DIR / 'hunts.csv'
hunts.to_csv(output, index=False)
 
print(output.resolve(), '->', len(hunts), 'filas')

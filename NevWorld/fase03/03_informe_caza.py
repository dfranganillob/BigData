from pathlib import Path

import pandas as pd


DATA_DIR = Path('NevWorld/data/processed')
REPORTS_DIR = Path('NevWorld/fase03/reports')
REPORTS_DIR.mkdir(exist_ok=True)

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')
resources = pd.read_csv(DATA_DIR / 'resources.csv')

hunts_counts = hunts['event_index'].value_counts()
print('\nCacerias completadas')
print(hunts_counts)

hunts_tipo = hunts['prey_type'].value_counts()
print('\nTipo de presa')
print(hunts_tipo)

hunts_proportions = hunts['prey_type'].value_counts(normalize=True)
hunts_percent = (hunts_proportions * 100).round(1)
print('\nPorcentaje')
print(hunts_percent)

hunts_dia = hunts['simulation_day'].value_counts().sort_index()
print('\nCacerias completadas cada dia')
print(hunts_dia)

resource_groups = resources.groupby('resource_type')
delta_groups = resource_groups['amount_delta']
resource_balance = delta_groups.sum()
resource_balance = resource_balance.sort_values(ascending=False)

print('\nBALANCE NETO DE COMIDA')
print(resource_balance)

if hunts_counts.empty:
    print('No hay cacerías completadas')
else:
    first = hunts_counts.iloc[0]
    last = hunts_counts.iloc[-1]

resource_balance = (
    resources[resources['resource_type'] == 'food']
    .groupby('resource_type')['amount_delta']
    .sum()
    .sort_values(ascending=False)
)
print('\nBALANCE NETO DE RECURSOS')
print(resource_balance)

food_resources = resources[resources['resource_type'] == 'food']
gains = food_resources[food_resources['amount_delta'] > 0]
spending = food_resources[food_resources['amount_delta'] < 0].copy()
spending['amount_delta'] = spending['amount_delta'].abs()
print('\nINCREMENTOS REGISTRADOS')
print(gains['amount_delta'].sum())
print('\nREDUCCIONES REGISTRADAS')
print(spending['amount_delta'].sum())

total_counts = hunts_counts.sum()

summary = pd.DataFrame([
    {'metric': 'hunt_counts', 'value': total_counts},
    {'metric': 'hunts_tipo', 'value': hunts_tipo},
    {'metric': 'gains', 'value': len(gains)},
    {'metric': 'spending', 'value': len(spending)},
    {'metric': 'resource_balance', 'value': resource_balance},
])

summary.to_csv(REPORTS_DIR / 'metrics_summary.csv', index=False)
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_DIR = Path('NevWorld/data/processed')
CHARTS_DIR = Path('NevWorld/fase04/reports')
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')

prey_counts = hunts['prey_type'].value_counts()

plt.figure(figsize=(10, 5))

# plot.bar dibuja una barra por categoría; color elige su color.
prey_counts.plot.bar(color='green')
plt.title('Cambios de actividad registrados')
plt.xlabel('Prey_type')
plt.ylabel('Número de eventos')

# Gira las etiquetas 45 grados y las alinea a la derecha.
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
if prey_counts.sum() == 0:
    print(f"No hay datos para mostrar")
else:
    plt.savefig(CHARTS_DIR / '05_hunts_by_prey.png')
    plt.close()
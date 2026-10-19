## 1. Prepara las preguntas y los datos

| Pregunta | Tabla y columnas necesarias | Operación y motivo |
| --- | --- | --- |
| ¿Cuántas cacerías completadas se registraron? | hunts['event_index']| hunts_counts = hunts['event_index'].value_counts()|
| ¿Cuántas corresponden a cada tipo de presa? | hunts['prey_type']| hunts_tipo = hunts['prey_type'].value_counts()|
| ¿Qué porcentaje representa cada presa? | hunts['prey_type']| hunts_proportions = hunts['prey_type'].value_counts(normalize=True), hunts_percent = (hunts_proportions * 100).round(1)|
| ¿Cuántas cacerías se registraron en cada día observado? | hunts['simulation_day']| hunts_dia = hunts['simulation_day'].value_counts()|
| ¿Cuánto aumentó, disminuyó y cambió en términos netos la comida? | resources('resource_type'), resources('amount_delta')| resource_groups = resources.groupby('resource_type'), delta_groups = resource_groups['amount_delta'], resource_balance = delta_groups.sum(),resource_balance = resource_balance.sort_values(ascending=False)|

## 2. Resume el parte de caza

Explica qué representa una fila de hunts.csv y cuál es el denominador de los porcentajes.
Representa una cacería completada, donde dentro podemos encontrar distintas caracteristicas como el tipo de presa o el dia que se produjo esta cacería. El denominador de los porcentajes es 100.

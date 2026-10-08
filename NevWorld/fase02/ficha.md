## 1. Investiga antes de elegir
| Pregunta | Campo o valor elegido | Justificación |
| --- | --- | --- |
| ¿Qué evento demuestra que la cacería terminó? | "type":"hunt_completed"| Selecciona el hecho que interesa|
| ¿Quién la completó? | "villager_id":1989| Identifica quién la completó|
| ¿Qué presa aparece registrada? | "prey_type":"deer"| Conserva el tipo registrado|
| ¿Cuándo ocurrió? | "tick":4260| Muestra el momento de tiempo exacto|
| ¿A qué partida pertenece? | "run_id":"20261007_190831_9549888358690311366_022cb066fbe14b788497c5b18a326a5c"| Muestra el id de partida jugada|
| ¿Cómo localizo el evento original sin confundirlo con otro? | "event_index":127| Permiten ver la línea original|

{"schema_version":2,"run_id":"20261007_190831_9549888358690311366_022cb066fbe14b788497c5b18a326a5c","seed":"9549888358690311366","event_index":127,"tick":4260,"type":"hunt_completed","villager_id":1989,"prey_type":"deer"}

Explica también por qué `activity`, `food_stock` y `amount_delta` no son necesarios para este parte. ¿Permite el evento saber por sí solo cuánta comida produjo la cacería?
El evento no permite por si solo ver la comida que produjo la cacería, pero eso no significa que 'activity' o 'food_stock' sea necesario. Ya que si investigamos unas lineas más abajo y más arriba podemos ver la diferencia de comida, esa diferencia es la cantidad de comida producida.

## 4. Detecta las conclusiones que los datos no sostienen
1. «Hay seis filas, por tanto hay seis cazadores distintos». ¿Es necesariamente cierto?
No es cierto.
2. «Una fila indica que ese aldeano estuvo cazando durante todo el día». ¿Qué registra realmente la fila?
La fila registra todo en un tick, no incluye lo que dura la cacería.
3. «Borro del DataFrame original todas las filas con algún `NaN` y después selecciono las cacerías». ¿Por qué puede desaparecer información válida?
Aunque tenga NaN no significa que sea invalido.
4. «El CSV está vacío, así que nadie intentó cazar». ¿Qué puedes afirmar realmente sobre el registro?
No hay cazas completadas correctamente.

from pathlib import Path
from hashlib import sha256

# Esta ruta se interpreta desde la raíz de bigdata-game.
#path = Path('data/intercambio/envio/partida_A.jsonl')
# La huella representa los bytes del archivo que acabamos de leer.
#huella = sha256(path.read_bytes()).hexdigest()
#print(path.name, path.stat().st_size, huella)

#dos = Path('data/intercambio/envio/partida_B.jsonl')
#huella_dos = sha256(path.read_bytes()).hexdigest()
#print(dos.name, dos.stat().st_size, huella_dos)

folder = Path("data/intercambio/recibido")

expected = {
    "partida_A.jsonl": (257390, "3c6a94f58e15c9afd1c580922be0fb427ee34254b1c0e9078d6ce11b35dd29a5"),
    "partida_B.jsonl": (257390, "3c6a94f58e15c9afd1c580922be0fb427ee34254b1c0e9078d6ce11b35dd29a5"),
}

for name, (size_expected, hash_expected) in expected.items():
    path = folder / name
    
    print(f"=== Comprobando: {name} ===")
    
    if not path.is_file():
        print("Estado: NO RECIBIDO\n")
        continue

    size_received = path.stat().st_size
    hash_calculated = sha256(path.read_bytes()).hexdigest()

    if hash_calculated == hash_expected:
        resultado = "COINCIDE"
    else:
        resultado = "NO COINCIDE"

    print(f"Tamaño esperado : {size_expected} bytes")
    print(f"Tamaño recibido : {size_received} bytes")
    print(f"Huella esperada  : {hash_expected}")
    print(f"Huella calculada : {hash_calculated}")
    print(f"Resultado        : {resultado}\n")
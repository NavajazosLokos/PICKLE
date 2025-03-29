import pickle
import os
archivo = "estado.pkl"
# Cargar estado si existe
if os.path.exists(archivo):
with open(archivo, "rb") as f:
estado = pickle.load(f)
else:
estado = {"contador": 0, "fase": "inicio"} # Estado inicial
print(f"Contador: {estado['contador']}, Fase: {estado['fase']}")
# Simulación de ejecución
estado["contador"] += 1
estado["fase"] = "progreso" if estado["contador"] < 5 else
"finalizado"
# Guardar estado
with open(archivo, "wb") as f:
pickle.dump(estado, f)
print("Estado guardado. Ejecuta de nuevo para continuar.")
import pickle
# Guardar datos
datos = {"nombre": "Juan", "edad": 25}
with open("datos.pkl", "wb") as f:
pickle.dump(datos, f)
# Cargar datos
with open("datos.pkl", "rb") as f:
cargado = pickle.load(f)
print(cargado) # {'nombre': 'Juan', 'edad': 25}
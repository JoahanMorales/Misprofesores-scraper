import json

file_path = "dataset_upiicsa.json"
with open(file_path, "r", encoding="utf-8") as file:
    dataSet = json.load(file)


profesor_buscado = "goytia"  

busqueda_normalizada = profesor_buscado.strip().lower()

coincidencias = []

for profesor in dataSet:
    nombre = profesor.get("n", "")
    apellido = profesor.get("a", "")
    
    nombre_completo = f"{nombre} {apellido}".strip().lower()
    
    nombre_completo_invertido = f"{apellido} {nombre}".strip().lower()
    
    calificacion = profesor.get("c", "Calificación no disponible")
    if calificacion and calificacion != "Calificación no disponible":
        try:
            calificacion = float(calificacion)
        except ValueError:
            calificacion = "Calificación no válida"
    else:
        calificacion = "Calificación no disponible"
    
    if busqueda_normalizada in nombre_completo or busqueda_normalizada in nombre_completo_invertido:
        coincidencias.append({
            "nombre": nombre,
            "apellido": apellido,
            "calificacion": calificacion + 2
        })

if coincidencias:
    print(f"Se encontraron {len(coincidencias)} coincidencia(s):\n")
    for prof in coincidencias:
        print(f"Profesor: {prof['nombre']} {prof['apellido']}, Calificación: {prof['calificacion']}")
else:
    print(f"No se encontró ningún profesor similar a '{profesor_buscado}'.")

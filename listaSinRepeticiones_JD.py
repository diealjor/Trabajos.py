from collections import Counter

nombres = [
    "Alejandro", "Sofía", "Mateo", "Lucía", "Sebastián", "Valentina", "Daniel", "Martina",
    "Pablo", "María", "Álvaro", "Paula", "Adrián", "Julia", "Diego", "Valeria",
    "Javier", "Daniela", "Carlos", "Alba", "Lucas", "Emma", "Hugo", "Carla",
    "Martín", "Sara", "Manuel", "Carmen", "Pedro", "Noa", "David", "Claudia",
    "Mario", "Elena", "Marcos", "Irene", "Nicolás", "Nerea", "Gabriel", "Rocío",
    "Samuel", "Laura", "Gonzalo", "Marta", "Jorge", "Andrea", "Sergio", "Ana",
    "Luis", "Natalia", "Miguel", "Cristina", "Fernando", "Beatriz", "Raúl", "Patricia",
    "Rubén", "Silvia", "Iván", "Raquel", "Óscar", "Mónica", "Enrique", "Alicia",
    "Alberto", "Marina", "Víctor", "Inés", "Francisco", "Celia", "Antonio", "Nuria",
    "José", "Miriam", "Juan", "Lorena", "Andrés", "Eva", "Rafael", "Teresa",
    "Ramón", "Pilar", "Vicente", "Rosa", "Eduardo", "Ángela", "Ignacio", "Blanca",
    "Guillermo", "Clara", "Roberto", "Victoria", "Jaime", "Lidia", "Arturo", "Verónica",
    "Emilio", "Susana", "Tomás", "Isabel", "Héctor", "Yolanda", "César", "Sonia",
    "Julio", "Olga", "Salvador", "Carolina", "Agustín", "Vanesa", "Félix", "Gema",
    "Rodrigo", "Estefanía", "Iker", "Aitana", "Unai", "Laia", "Aitor", "Ane",
    "Biel", "Ona", "Pol", "Jana", "Arnau", "Abril", "Marc", "Iria",
    "Joel", "Nora", "Eric", "Vera", "Bruno", "Triana", "Leo", "Candela",
    "Gael", "Vega", "Thiago", "Alma", "Dylan", "Lola", "Enzo", "Jimena",
    "Darío", "Olivia", "Álex", "Chloe", "Ian", "Mía", "Oliver", "Zoe",
    "Alejandro", "Lucía", "Mateo", "María", "Daniel", "Sofía", "Pablo", "Paula",
    "Carlos", "Carmen", "Javier", "Laura", "Manuel", "Marta", "David", "Elena",
    "Lucas", "Sara", "Hugo", "Valeria", "Martín", "Alba", "Adrián", "Julia",
    "Diego", "Daniela", "Álvaro", "Martina", "José", "Ana", "Juan", "Isabel",
    "Antonio", "Cristina", "Francisco", "Patricia", "Miguel", "Beatriz", "Luis", "Silvia",
    "Alejandro", "María", "Lucía", "Carlos", "Sofía", "Daniel", "Paula", "Javier",
    "Carmen", "Manuel", "Laura", "David", "Marta", "Pablo", "Elena", "Mateo"
]

# VERSIÓN 1: dejar una sola aparición de cada nombre.
# dict.fromkeys conserva el orden original de la lista.
nombres_sin_repetidos = list(dict.fromkeys(nombres))

print("Lista dejando una aparición de cada nombre:")
print(nombres_sin_repetidos)
print("Cantidad de nombres:", len(nombres_sin_repetidos))

# VERSIÓN 2: eliminar todos los nombres que aparecen más de una vez.
frecuencias = Counter(nombres)
nombres_sin_duplicados = [
    nombre for nombre in nombres if frecuencias[nombre] == 1
]

print("\nLista eliminando todas las apariciones de los nombres repetidos:")
print(nombres_sin_duplicados)
print("Cantidad de nombres:", len(nombres_sin_duplicados))

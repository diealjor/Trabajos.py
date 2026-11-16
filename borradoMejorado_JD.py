import random

notas = []

while len(notas) < 100:
    nota = random.randint(0, 10)
    notas.append(nota)

print("En mi lista tengo", notas.count(0), "ceros.")

# Creamos una nueva lista sin los ceros en una sola pasada
notas = [nota for nota in notas if nota != 0]

print(len(notas), notas)

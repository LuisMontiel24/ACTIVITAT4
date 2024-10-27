def crear_matriu_diagonal():
    # Crear una matriu 7x7 amb zeros i valors de 0 a 49 a la diagonal
    matriu = [[0] * 7 for _ in range(7)]
    for i in range(7):
        matriu[i][i] = i * 7
    return matriu

def guardar_matriu(matriu, filename):
    # Guardar la matriu en un fitxer de text
    with open(filename, 'w') as file:
        for fila in matriu:
            file.write(" ".join(map(str, fila)) + "\n")

# Genera i guarda la matriu
matriu = crear_matriu_diagonal()
guardar_matriu(matriu, "exercici1.txt")
print("Matriu diagonal guardada a 'exercici1.txt'")

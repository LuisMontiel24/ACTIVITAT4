def crear_matriu_diagonal():
    # Creo una matriu de 7x7 amb 0s i només permetre valors ascendents en diagonal
    matriu = [[0 for _ in range(7)] for _ in range(7)]
    for i in range(7):
        # Els valors que vull que surtin han d'arribar al 49 i 7 es el seu multiple
        matriu[i][i] = i * 7 
    return matriu

def guardar_matriu(matriu, filename):
    # Guardo el resultat de la matriu en un fitxer txt que serà creat al executar el programa
    with open(filename, 'w') as file:
        for row in matriu:
            file.write(" ".join(map(str, row)) + "\n")

# Executo la funció i guardo la matriu
matriu = crear_matriu_diagonal()
guardar_matriu(matriu, "exercici1.txt")
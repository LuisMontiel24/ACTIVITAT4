import random

def crear_matriu_3x4():
    # Creo una matriu amb numeros aleatoris de 0 al 80
    matriz = [[random.randint(0, 80) for _ in range(4)] for _ in range(3)]
    print("Matriu 3x4 principal:")
    for fila in matriz:
        print(fila)
    return matriz

def modificar_a_4x3(matriz):
    
    # Converteixo la matriu anterior en una de 4x3 convertint els numeros de l'ultima fila en els numeros de l'ultima columna.
    matriz_modificada = [[matriz[j][i] for j in range(3)] for i in range(3)]
    
    # Afegeixo l'última fila de la matriu principal com a l'ultima columna
    for i in range(3):
        matriz_modificada[i].append(matriz[2][i])

    # Afegeixo una quarta fila amb els valors de l'ulitma columna
    matriz_modificada.append([matriz[2][i] for i in range(4)])

    print("\nMatriu modificada a 4x3 (última fila com última columna):")
    for fila in matriz_modificada:
        print(fila)
    
    return matriz_modificada

def igualar_ultima_columna(matriz):
    # El mateix que l'exercici anterior pero en aquest cas serà de 4x4 i l'ultima columna tindrà el valor del primer numero de l'ultima columna de la matriu anterior.
    valor_igualado = matriz[0][3]
    for i in range(4):
        matriz[i][3] = valor_igualado
    
    print("\nMatriu final:")
    for fila in matriz:
        print(fila)
    
    return matriz

# Execució de les funcions
if __name__ == "__main__":
    matriu_3x4 = crear_matriu_3x4()
    matriu_4x3 = modificar_a_4x3(matriu_3x4)
    matriu_final = igualar_ultima_columna(matriu_4x3)

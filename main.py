from exercici1 import crear_matriu_diagonal, guardar_matriu
from exercici2 import crear_matriu1, crear_matriu2, crear_matriu3
from exercici3 import crear_matriu_aleatoria, redimensionar_matriu, valor_maxim, valor_minim
from exercici4_nomAlumne import crear_matriu_3x4, modificar_a_4x3, igualar_ultima_columna

def main():
    # Exercici 1
    matriu1 = crear_matriu_diagonal()
    guardar_matriu(matriu1, "exercici1.txt")
    print("Exercici 1 - Matriu diagonal guardada a exercici1.txt")

    # Exercici 2
    print("\nExercici 2:")
    print("Matriu 1:", crear_matriu1())
    print("Matriu 2:", crear_matriu2())
    print("Matriu 3:", crear_matriu3())

    # Exercici 3
    print("\nExercici 3:")
    matriu3 = crear_matriu_aleatoria(3, 3)
    print("Matriu Aleatòria:", matriu3)
    print("Valor Màxim:", valor_maxim(matriu3))
    print("Valor Mínim:", valor_minim(matriu3))

    # Exercici 4
    print("\nExercici 4:")
    matriu4 = crear_matriu_3x4()
    print("Matriu 3x4 original:", matriu4)
    matriu4_modificada = modificar_a_4x3(matriu4)
    print("Matriu modificada a 4x3:", matriu4_modificada)
    matriu4_final = igualar_ultima_columna(matriu4_modificada)
    print("Matriu final amb última columna igualada:", matriu4_final)

if __name__ == "__main__":
    main()

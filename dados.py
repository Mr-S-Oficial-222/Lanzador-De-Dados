import random

while True:
    var = int(input("Cuantas Cara Tiene Tu Dado(pon 0 si quieres salir): "))
    if var >= 1:
        var2 = int(input("Cuantos Dados Quieres Lanzar: "))
        for i in range(1, var2 + 1):
            numero_aleatorio = random.randint(1,var)
            print(numero_aleatorio)
            print(f"numero de dados restantes {i} su valor es {numero_aleatorio}")
            
    else:
        break

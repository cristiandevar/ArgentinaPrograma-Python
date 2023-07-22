# Pedimos informacion al usuario
num_1 = int(input("Ingrese el dividendo: "))
num_2 = int(input("Ingrese el divisor: "))

if num_2 == 0:
    print("Error no es posible dividir por 0")
else:
    print(num_1 / num_2)
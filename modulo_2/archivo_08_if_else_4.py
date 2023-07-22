# Pedimos informacion al usuario
num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))

if num_1 < num_2:
    print(str(num_1) + " es menor que " + str(num_2))

elif num_2 < num_1:
    print(str(num_1) + " es mayor que " + str(num_2))

else:
    print("Los numeros son iguales")
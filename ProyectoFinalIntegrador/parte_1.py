import numpy as np

# Ingresamos los sueldos a mano en un diccionario para mantener la organizacion
sueldo_por_mes = {
    'Enero': 300,
    'Febrero': 300,
    'Marzo': 300,
    'Abril': 300,
    'Mayo': 300,
    'Junio': 300,
    'Julio': 500,
    'Agosto': 500,
    'Septiembre': 500,
    'Octubre': 500,
    'Noviembre': 700,
    'Diciembre': 700,
}

# Almacenamos los sueldos en una lista
lista_sueldo = []
for s in sueldo_por_mes.values():
    lista_sueldo.append(s)

# Mostramos los sueldos
print(f'La lista de sueldos: {lista_sueldo}')

# Calculamos el promedio
promedio_sueldo = sum(lista_sueldo)/len(lista_sueldo)
# Tambien podemos hacerlo usando la libreria numpy
# promedio_sueldo = np.mean(lista_sueldo)

# Mostramos el mensaje final
if promedio_sueldo < 300:
    print(f'Sueldo bajo')
elif promedio_sueldo >= 300 and promedio_sueldo <= 900:
    print(f'Sueldo normal')
else:
    print(f'Sueldo mejor de lo normal')
print(f'Debido a que el sueldo promedio es: {promedio_sueldo}')
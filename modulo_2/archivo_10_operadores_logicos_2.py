# Conjuncion y Disyuncion
a = True
b = False

print(a and a) # True and True

print(a and b) # True and False

print(a or b) # True or False

print(b or b) # False or False

print((3 < 4) and (4 < 5)) # True and True
print((6 < 4) and (3 < 5)) # True and False


# Negacion --> not
resultado = a and a # True and True
print(not resultado)

resultado = a and b # True and False
print(not resultado)


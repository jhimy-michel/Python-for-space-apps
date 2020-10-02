# CONDICIONALES
a = 2
if a>3:
    print ("a es mayor que 3")
else:
    print ("a no es mayor que 3")

# ejemplo 1
# saber si soy mayor de edad
a = int(input("Ingresa tu edad: "))

if a >= 18:
    print ("eres mayor de edad")
else:
    print ("no eres mayor de edad")


# ejemplo 2
# saber si soy jurado electoral
nombre = input("Ingresa tu nombre: ")

# primera condicional
if nombre == "Pedro":
    print ("eres jurado electoral")
# segunda condicional
elif nombre == "Jaime":
    print ("eres jurado electoral")
# tercera condicional
elif nombre == "Juan":
    print ("eres jurado electoral")
else:
    print ("no eres jurado electoral")

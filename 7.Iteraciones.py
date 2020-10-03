# ITERACIONES

# WHILE
# repite un bloque mientrar la condicion
# logica devuelva True

contador = 0

while contador < 5:
    print (contador)
    contador = contador + 1

#FOR
# es un "bucle definido", es decir,
# que se pre establece las condiciones de 
# la interacion por adelantado

frutas = ["mango","naranjas","sandia"]

for fruta in frutas:
    print (fruta)

# range function
for x in range(6):
  print(x)


# ejemplo #2:  range function
# a = 3 / acum = 1 + 2 + 3
print ("Another example:")
a = 3
acum = 0
for x in range(a):
  a = x + a
print(a)
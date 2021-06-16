# -*- coding: utf-8 -*-

'''
En "00-sintaxis" ya se ha visto un poco como se declaran variables, y no hay mucho más.
Pero para que esté todo organizado, pues se les dedica un archivo.

Al tratarse de un lenguaje de propósito general, tenemos lo más típico:
	- Enteros
	- Flotas (Números reales)
	- Booleanos (Verdarero/Falso)
	- Arrays/Listas. En Python los Arrays se llaman Listas.

Por lo tanto, aqui van algunos ejemplos:

Estos son números enteros '''
numEntero = 5
numEntero2 = 10 + 15 * 34

#Si realizamos ahora
division  = numEntero/numEntero2
#Al ser ambos números enteros, el resultado será un número entero. Si se quieren
#realizar operaciones con decimales ambos deben ser floats.

numFloat = 5.0
#En este caso numFloat2, sí que será un numero float, con valor 2.5 concretamente.
numFloat2 = 5.0/2.0

#Forma básica

print("hola")
a = "hola"
print(a)
print("Para concatenar valores como "+a+"se usa el +")

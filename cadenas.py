#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Ejercicios básicos de cadenas
# Llenar el código de las funciones abajo. main() ya está armado
# para llamar a las funciones con algunas entradas,
# imprime 'OK' cuando cada función es correcta.
# El código inicial para cada función incluye un 'return'
# que es sólo un comodín para tu código.


# A. donuts
# dado un contador entero de un número de donas, retornar una cadena
# de la forma 'Numero de donas: <contador>', donde <contador> es el
# número pasado. Sin embargo, si el contador es 10 o más, entonces usar
# la palabra "muchas" en vez del contador verdadero.
# Así donuts(5) devuelve 'Numero de donas: 5'
# y donuts(23) devuelve 'Numero de donas: muchas'
def donuts(contador):
    
contador= input ("Ingrese el numero de donas: ")
if contador >= 10:
	print "Numero de donas: muchas"
else:
	print "Numero de donas: " + str(contador)	



# B. both_ends
# Dada una cadena s, devuelva una cadena hecha de los primeros 2
# y los últimos 2 caracteres de la cadena original,
# así 'spring' devuelve 'spng'. Sin embargo, si la longitud de la cadena
# es menos de 2, returnar una cadena vacía en su lugar.
def both_ends(s):
    # +++tu código aquí+++
   s = raw_input ("Ingrese cadena: ")
f = len (s)
r = s[0]
s= s.replace (s[0],"*")
valor= r + s[1:f]
print valor

# C. fix_start
# Dada una cadena s, devuelva una cadena
# donde todas las ocurrencias del primer caracter han
# cambiado a '*', excepto por el primer caracter mismo.
# ej: 'babble' retorna 'ba**le'
# Asuma que la cadena es de 1 o más caracteres.
# Ayuda: s.replace(stra, strb) retorna una versión de la cadena s
# donde todas las instancias de stra han sido reemplazadas por strb.



# D. MixUp
# Dadas las cadenas a y b, retornar una cadena simple con a y b separados
# pon un espacio '<a> <b>', excepto que hay que intercambiar los 
# 2 primeros caracteres de cada cadena.
# ej.
#     'mix', pod' -> 'pox mid'
#     'dog', 'dinner' -> 'dig donner'
# Asumir a y b tienen una longitud de 2 o más.
def mix_up(a, b):
    # +++tu código aquí+++
def fix_start(s):
    a = raw_input("cadena a:")
b = raw_input("cadena b:")
c = a[0]

a = b[0]+ a[1:100] 
b = c[0]+ b[1:100] 
r = a + " " + b
    return r
# Función simple test() utilizada en main() para mostrar
# lo que retorna cada función vs lo que debería retornar.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '    X '
    print '%s obtuvo: %s se esperaba: %s' % (prefix, repr(got), repr(expected))


# Función main() llama a las funciones de arribacon entradas interesantes,
# utilizando test() para verificar si cada resultado es correcto o no.
def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Numero de donas: 4')
    test(donuts(9), 'Numero de donas: 9')
    test(donuts(10), 'Numero de donas: many')
    test(donuts(99), 'Numero de donas: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

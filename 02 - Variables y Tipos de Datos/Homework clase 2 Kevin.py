import math

variable1 = 11 #punto 1

print (8.5) #punto 2

print (type(variable1)) #punto 3

variable2 = 'Kevin' #punto 4

variable3 = 4 + 6j #punto 5

print (type(variable3)) #punto 6

variable4 = round(math.pi, 4) #punto 7

variable5 = True
variable6 = 'True' #punto 8

print (type(variable5))
print (type(variable6)) #punto 9

variable7 = 10 + 10.5 #punto 10

print ((1 + 2j) + (1 + 3j)) #punto 11

print (10.5 + (1 + 2j)) #punto 12

print (4 * 5) #punto 13

print (2**8) #punto 14

variable8 = 27 / 4
print (variable8) #punto 15

variable9 = 27 // 4
print (variable9) #punto 16

variable10 = 27 % 4
print (variable10) #punto 17

print (4 * variable9 + variable10) #punto 18

variable11 = 'barra ' + 'libre'
print(variable11) #punto 19

variable12 = '2' == 2
print (variable12) #punto 20 son diferentes porque '2' es un string y 2 es un intiger

variable13 = '2' == str(2)
print (variable13) #punto 21 cambiando el 2 de intiger a string, podes hacer es lo mismo

#punto 22 porque tiene una coma en vez de un punto y una variable flotante o fraccionaria lleva un punto

variable14 = 3
variable14 -= 3
print (variable14) #punto 23

print (1 << 2) #punto 24 1 es 001 en binario de 3 bits, si desplazas el 1 dos espacios a la izquierda te queda 100, que es 4 en binario

#punto 25 ----- (2 + '2') no esta permitido porque el primero es un integer y el segundo un string. Si ambos fuesen integer el resultado seria 4 en integer y si ambos fuesen string el resultado seria 22 en string

variable15 = 2 != '2'
print (variable15) #punto 26 podes comparar integer y string
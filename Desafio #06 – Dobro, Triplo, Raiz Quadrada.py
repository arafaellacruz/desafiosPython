#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math
n = int(input('Informe um número: '))
d = n * 2
t = n * 3
r = math.pow(n, 1/2)

print('Informações sobre ', n, ', abaixo: \n Dobro = {} \n Triplo = {} \n Raiz Quadrada = {:.3f}'.format(d, t, r))

#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exemplo: Digite um número: 6.124
#O número 6.124 tem a parte inteira 6.

import math

n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, math.floor(n)))
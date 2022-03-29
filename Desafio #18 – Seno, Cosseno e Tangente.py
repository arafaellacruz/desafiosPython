# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor so seno, cosseno e tangente desse ângulo.
import math

a = float(input('Informe o valor do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O ângulo de {} tem o SENO igual a {:.2f}.'.format(a, s))
print('O ângulo de {} tem o COSSENO igual a {:.2f}.'.format(a, c))
print('O ângulo de {} tem a TANGENTE igual a {:.2f}.'.format(a, t))
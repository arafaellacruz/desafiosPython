#Faça um algoritmo que leia o salário de um funcionário e mostre
# o seu novo salário com 15% de aumento.

sa = float (input('Informe seu salário para descobrir quanto ficará com o aumento de 15%: R$ '))

ns = sa + (sa * 0.15)

print('Parabéns pelo aumento! Seu novo salário é de R$ {}'.format(ns))
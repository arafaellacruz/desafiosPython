# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int (input('Informe um número para descobrir seu sucessor e antecessor: '))

s = n + 1
a = n - 1

print('O sucessor de {} é {} e o seu antecessor é {}.'.format(n,s,a))

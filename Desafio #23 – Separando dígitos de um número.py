# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = input('Digite um número de 0 a 9999: ')
print('O número {} tem: '.format(n))
print(('{} unidade(s).'.format(n[3])))
print(('{} dezena (s).'.format(n[2])))
print(('{} centena (s).'.format(n[1])))
print(('{} milhar (es).'.format(n[0])))
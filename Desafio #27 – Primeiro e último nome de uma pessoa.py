#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

x = input('Informe seu nome completo: ').strip()
nome = x.split()
print('Olá! Seu primeiro nome é {} e seu último nome é {}.'.format(nome[0], nome[len(nome) -1 ]))
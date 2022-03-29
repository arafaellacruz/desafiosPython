#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Informe seu nome completo: ').strip()
print('Seu nome tem SILVA? {}.'.format('SILVA' in nome.upper())) #In é um operador do Python
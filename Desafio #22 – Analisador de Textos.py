# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras sem considerar os espaços.)
# – Quantas letras tem o primeiro nome.

nome = input('Informe seu nome completo: ').strip()
print('Nome com letras maiúsculas: {}. '.format(nome.upper()))
print('Nome com letras minúsculas: {}. '.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#Desafio 04: Faça um programa que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')
print('O tipo primitivo do que você digitou é: ', type(x))
print('O que você digitou é um número? ',x.isnumeric())
print('O que você digitou é alfabético? ', x.isalpha())
print('O que você digitou é decimal? ', x.isdecimal())
print('O que você digitou é um alfanúmerico? ', x.isalnum())
print('O que você digitou está em letras maúsculas? ', x.isupper())
print('O que você digitou está em letras minúsculas? ',x.islower())
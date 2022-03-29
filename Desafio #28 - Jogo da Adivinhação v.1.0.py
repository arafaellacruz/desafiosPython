# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

import random

pc = random.randint(0, 5) #Faz o computador sortear um número.
print('=-=' * 22)
print('Estou pensando no número entre 0 e 5. Vamos ver se você adivinha? ')
print('=-=' * 22)
player = int(input('Em qual número eu estou pensando? '))

if pc == player:
    print('Droga! Você acertou, eu pensei no número {}, conseguiu me vencer!'.format(pc))
else:
    print('HAHA! Você perdeu! Eu pensei em {}, tente novamente!'.format(pc))
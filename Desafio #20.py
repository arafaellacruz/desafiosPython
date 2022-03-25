#O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalho dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.

import random
print('==== SORTEIO DE APRESENÇÃO DOS TRABALHOS ====')
a1 = input('Informe o nome do Aluno 1: ')
a2 = input('Informe o nome do Aluno 2: ')
a3 = input('Informe o nome do Aluno 3: ')
a4 = input('Informe o nome do Aluno 4: ')

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresenção será : \n {}'.format(lista))
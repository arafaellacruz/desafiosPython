#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece
# a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite a frase: ').upper().strip()
print('A letra "A" aparece {} vez (es) na frase informada.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind('A')+1))
#A função 'rfind' procura um # item começando pela direita;
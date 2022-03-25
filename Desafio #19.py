#Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

print('==== Informe os nomes para realizar o sorteio ====')
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

alunos = [a1, a2, a3, a4]
sorteio = random.choice(alunos)

print('O aluno sorteado foi: {}'.format(sorteio))



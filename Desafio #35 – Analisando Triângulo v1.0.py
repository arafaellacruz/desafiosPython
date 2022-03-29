# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Para formar um triângulo, cada segmento deve ser MENOR que a soma dos outros 2.
print('=*=' * 20)
print('               ANALISADOR DE TRIÂNGULOS       ')
print('=*=' * 20)
a = float(input('Informe o valor do 1º segmento: '))
b = float(input('Informe o valor do 2º segmento: '))
c = float(input('Informe o valor do 3º segmento: '))

if a < (b + c) and b < (a + c) and c < (b + a):
    print('Os segmentos podem formar um triângulo.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
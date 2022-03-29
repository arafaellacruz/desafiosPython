# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# um triângulo retângulo, calcule e mostre o compromento da hipotenusa.
import math

print('==== Descubra o comprimento da hipotenusa ==== ')
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

#Exemplos de como resolver:
#soma = (co ** 2) + (ca ** 2)
#h = math.sqrt(soma)
#print('A hipotenusa vai medir {:.2f}.'.format(h))  //

h = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(h))


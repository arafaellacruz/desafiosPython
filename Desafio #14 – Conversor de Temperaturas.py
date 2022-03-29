#Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.

c = int (input('Informe a temperatura em graus Cº: '))

F = (1.8 * c) + 32

print('{} Cº é igual a {:.1f} Fº.'.format(c,F))
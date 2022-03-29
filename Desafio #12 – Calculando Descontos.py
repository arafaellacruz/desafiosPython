# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

pa = float (input('Informe o preço do produto para receber o desconto: R$ '))
pn = pa - (pa * 0.05)

print('Este produto sairá por R$ {:.2f}'.format(pn))
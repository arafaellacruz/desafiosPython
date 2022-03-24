# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.

dinheiro = float (input('Informe o valor que você possui na carteira: R$ '))

dolares = dinheiro / 3.27

print('Você pode comprar: $ {:.2f} dólar(es).'.format(dolares))
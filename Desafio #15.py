# Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule
# o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe a quantidade de quilometros percorridos: '))
dias = int(input('Informe a quantidade de dias de locação do veículo: '))

precoKm = km * 0.15
precoDias = dias * 60
total = precoKm + precoDias

print('O valor total a ser pago: R$ ',total)
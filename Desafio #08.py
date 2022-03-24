# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

M = float (input('Informe um valor em metros para realizar a conversão: '))
c = M * 100
m = M * 1000

print('{} metro (s) equivalem a: \n {} centímetros. \n {} milímetros.'.format(M, c, m))
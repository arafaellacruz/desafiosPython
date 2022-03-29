# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

print('=-=' * 20)
print('     CALCULE O PREÇO DA PASSAGEM PARA SUA VIAGEM     ')
print('=-=' * 20)

km = float(input('Informe quantos Km terá sua viagem: '))

if km <= 200:
    kmA= km * 0.50
    print('Você irá pagar R$ {:.2f} na sua passagem.'.format(kmA))
else:
    kmB = km * 0.45
    print('Você irá pagar R$ {:.2f} na sua passagem.'.format(kmB))
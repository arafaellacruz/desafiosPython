# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('=*=' * 20)
print('                     AUMENTO DE SALÁRIO       ')
print('=*=' * 20)
salario = float (input('Informe o seu salário atual: R$ '))

if salario > 1250:
    novoSalario = salario + (salario * 0.10)
else:
    novoSalario = salario + (salario * 0.15)

print('Seu novo salário é de R$ {}. Parabéns!'.format(novoSalario))
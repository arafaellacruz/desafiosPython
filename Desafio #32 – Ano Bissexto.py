# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Informe o ano que gostaria de analisar ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Irá pegar a data na máquina que o programa está sendo rodado.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É bissexto.'.format(ano))
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Informe o nome da sua cidade: ').strip()

#print('SANTO' in cidade[0:5].upper()
print(cidade[:5].upper() == 'SANTO' )
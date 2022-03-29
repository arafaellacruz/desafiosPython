n1 = float (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua média foi de : {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Puxa, não foi dessa vez que você conseguiu! Estude mais! ♥')
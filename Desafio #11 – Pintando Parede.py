#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo
#que cada litro de tinta pinta uma área de 2m².

print('===== Calcule a quantidade de tinta para pintar sua parede =====')
L = int (input('Informe a largura da parede (em metros): '))
A = int(input('Informe a altura da parede (em metros): '))

a = L * A
t = a / 2
print('A parece tem {} m², você precisará de {} litro(s) de tinta.'.format(a,t))
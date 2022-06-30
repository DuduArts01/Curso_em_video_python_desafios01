l = float(input('Qual é altura da parede? '))
h = float(input('Qual é largura da parede? '))
a = l * h
t = a / 2
#Cada litro de tinta pinta uma área de 2m²
print('A quantidade de tinta necessára é de {:.2f} l'.format(t))
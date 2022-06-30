from math import pow
co = float(input('Digite o valor do Cateto oposto: '))
ca = float(input('Digite o valor do Cateto adjacente: '))
# Teorema de Pitágoras: a² = b² + c²
h = pow(co, 2) + pow(ca, 2)
h = pow(h, 2)
print('A hipotenusa do triângulo retângulo de comprimento do Cateto Oposto {} e Cateto Adjacente {} é {:.3f}'.format(co, ca, h))

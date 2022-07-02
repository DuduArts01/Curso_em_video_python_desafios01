d = float(input('Qual é a distância de uma viagem em KM: '))
if 0 <= d <= 200:
    p = d * 0.50
    print(f'O preço da viagem vai ficar R${p:.2f}')
else:
    p = d * 0.45
    print(f'O preço da viagem vai ficar R${p:.2f}')

v = int(input('Digite a velocidade do carro: '))

if v > 80:
    valor_pagar = (v - 80) * 7
    print('Você foi multado no valor de R${:.2f}'.format(valor_pagar))
else:
    print('Você não foi multado, continue asssim, dirigindo de forma segura!')

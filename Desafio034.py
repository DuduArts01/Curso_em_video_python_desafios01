s = float(input('Qual o valor do seu salário? R$'))
if s > 1250.00:
    print('O seu salário de R${:.2f}, terá um aumento de 10% e seu novo salário será de R${:.2f} '.format(s, s + (s * 10 / 100)))
else:
    print('O seu salário de R${:.2f}, terá um aumento de 15% e seu novo salário será de R${:.2f}.'.format(s, s + (s * 15 / 100)))

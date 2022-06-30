s = float(input('Qual é o seu salário? R$'))
a = (s * 15)/100
ns = s + a
print('Seu salário é R${:.2f} e terá um aumento de 15%, o valor do aumento é R${:.2f}, e seu novo salário é R${:.2f} '.format(s, a, ns))
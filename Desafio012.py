p = float(input())
porcentagem = (p * 5)/100
descontado = p - porcentagem
print('O preço do produto é R${:.2f} e teve o desconto de 5%, que o valor do desconto é R${:.2f} e que o valor do produto com desconto é R${:.2f}'.format(p, porcentagem, descontado))
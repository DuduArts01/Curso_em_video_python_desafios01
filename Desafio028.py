from random import randint
num = randint(0,5)
print('-' * 50, '\nDescubra o número que o computador escolheu')
print('_' * 50)
descobrir = int(input('Adivinhe um número escolhido pelo computador:  '))
if descobrir == num:
    print('Você ganhou! \nO número escolhido pelo computador foi {}'.format(num))
else:
    print('Você Perdeu! \nO número escolhido pelo computador foi {}'.format(num))
print('-' * 50)

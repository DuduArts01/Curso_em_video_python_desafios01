num = input('Digite um número de 0 à 9999: ')
numero = int(num)
if (1000 <= numero <= 9999):
    print('unidade: {}'.format(num[3]))
    print('dezena: {}'.format(num[2]))
    print('centena: {}'.format(num[1]))
    print('milhar: {}'.format(num[0]))
else:
    if(100 <= numero < 1000):
        print('unidade: {}'.format(num[2]))
        print('dezena: {}'.format(num[1]))
        print('centena: {}'.format(num[0]))
        print('milhar: 0')
    else:
        if(0 <= numero < 100):
            print('unidade: {}'.format(num[1]))
            print('dezena: {}'.format(num[0]))
            print('centena: 0')
            print('milhar: 0')

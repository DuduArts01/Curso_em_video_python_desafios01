n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
else:
    if n2 > n1 and n2 > n3:
        print(f'O maior número é {n2}')
    else:
        if n3 > n1 and n3 > n2:
            print(f'O maior número é {n3}')

if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')
else:
    if n2 < n1 and n2 < n3:
        print(f'O menor número é {n2}')
    else:
        if n3 < n1 and n3 < n2:
            print(f'O menor número é {n3}')
name = input('Digite seu nome completo: ')
print(name.upper())
print(name.lower())
nome = name.strip().split()
nome_usuario = ''.join(nome)
print(len(nome_usuario))
print(len(nome[0]))
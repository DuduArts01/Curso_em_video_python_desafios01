'''  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''
nome = input('Digite seu nome completo: ')
print('primeiro = {}'.format(nome.strip().split()[0]))
print('último = {}'.format(nome.strip().split()[-1]))

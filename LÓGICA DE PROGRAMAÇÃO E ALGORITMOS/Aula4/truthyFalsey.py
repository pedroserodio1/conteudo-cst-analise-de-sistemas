'''
Dados não booleanos também podem ser
tratados como True ou False em uma
condição, seja esta de uma estrutura
condicionada ou de um laço
Falsey/False
Número zero (int ou float) e string vazia
Truthy/True
Qualquer outro dado
'''

nome = ''
while not nome:
    nome = input('Digite seu nome: ')

valor = int(input('Digite um numero: '))
if valor:
    print('Você digitou um valor diferente de 0')
else:
    print('Você digitou 0')
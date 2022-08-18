'''
Escreva um algoritmo que
realize um login em um
sistema
O usuário deve informar
seu nome e senha
'''

while True:
    nome = input('Digite seu nome: ')
    if nome != 'Serodinho':
        continue
    senha = input('Digite a senha: ')
    if senha == '1234':
        break
print('Acesso liberado')
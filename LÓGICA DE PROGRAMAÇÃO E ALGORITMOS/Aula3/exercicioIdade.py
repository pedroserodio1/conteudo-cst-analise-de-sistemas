"""
Escreva um algoritmo que lê um nome e uma
idade
Caso o nome digitado seja Vinicius, escreva
isso na tela
Caso o usuário digite qualquer outro nome,
verifique sua idade. Se for menor que 18
anos, informe que é de menor. Se for maior
que 100 anos, informe que esta pessoa
possivelmente não existe
"""
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome == 'Vinicius':
    print('Ola vinicius')
elif idade < 18:
    print('Você é de menor')
elif idade > 100:
    print('Essa pessoa possivelmente não existe')

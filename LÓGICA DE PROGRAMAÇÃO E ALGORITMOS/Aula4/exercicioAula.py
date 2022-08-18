'''
Escreva um algoritmo que imprima
na tela somente valores dentro de
um intervalo especificado pelo
usuário e que sejam número pares
'''

inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))

x = inicio

while(x <= fim):
    if x % 2 == 0:
        print(x)
    x = x + 1

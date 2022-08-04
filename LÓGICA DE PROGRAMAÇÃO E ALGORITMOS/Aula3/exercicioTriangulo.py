"""
Faça um algoritmo que receba três valores,
representando os lados de um triângulo
fornecidos pelo usuário. Verifique se os
valores formam um triângulo e classifique
como:
a) Equilátero (três lados iguais)
b) Isósceles (dois lados iguais)
c) Escaleno (três lados diferentes)
"""

l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if not(l1 == 0 or l2 == 0 or l3 == 0):
    if not(l1+l2<l3 or l2+l3<l1 or l1+l3<l2):
        if l1 == l2 and l1 == l3 and l2 == l3:
            print('Triangulo equilatero')
        elif (l1 == l2) or (l1 == l3) or (l2 == l3):
            print('Triangulo isosceles')
        elif not (l1 == l2 and l1 == l3 and l2 == l3):
            print('Triangulo escaleno')
    else:
        print('um lado não pode ser maior do que a soma dos outros dois')
else:
    print('O lado não pode ser 0')



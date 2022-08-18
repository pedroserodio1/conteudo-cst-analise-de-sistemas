'''
Escreva um algoritmo que leia um valor
e que imprima a quantidade de cédulas
necessárias para pagar esse mesmo valor.
Para simplificar, vamos trabalhar apenas
com valores inteiros e com cédulas de R$
100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1
'''

valor = int(input('Digite o valor em reais: '))

while True:
    if valor >=100:
        qtd100 = valor // 100
        valor -= qtd100 * 100
        print('Serão {} cedulas de 100'.format(qtd100))
        if not valor:
            break
    if valor >= 50:
        qtd50 = valor // 50
        valor -= qtd50 * 50
        print('Serão {} cedulas de 50'.format(qtd50))
        if not valor:
            break
    if valor >= 20:
        qtd20 = valor // 20
        valor -= qtd20 * 20
        print('Serão {} cedulas de 20'.format(qtd20))
        if not valor:
            break
    if valor >= 10:
        qtd10 = valor // 10
        valor -= qtd10 * 10
        print('Serão {} cedulas de 10'.format(qtd10))
        if not valor:
            break
    if valor >= 5:
        qtd5 = valor // 5
        valor -= qtd5 * 5
        print('Serão {} cedulas de 5'.format(qtd5))
        if not valor:
            break

    if valor:
        qtd1 = valor
        print('Serão {} cedulas de 1'.format(qtd1))
        break
    
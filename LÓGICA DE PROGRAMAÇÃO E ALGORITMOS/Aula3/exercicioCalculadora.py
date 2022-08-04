"""
Escreva um algoritmo que leia dois valores
numéricos e que pergunte ao usuário qual
operação ele deseja realizar: adição (+),
subtração (-), multiplicação (*) ou divisão
(/). Exiba na tela o resultado da operação
desejada (exercício da apostila – aula 3)
"""

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

operacao = int(input('Qual operacao você deseja fazer\n'
                 '1-Adição\n'
                 '2-Subtração\n'
                 '3-Divisão\n'
                 '4-Multiplicação\n'))

if operacao == 1:
    print('O valor da operacao é {:.2f}'.format(valor1 + valor2))
elif operacao == 2:
    print('O valor da operacao é {:.2f}'.format(valor1 - valor2))
elif operacao == 3:
    print('O valor da operacao é {:.2f}'.format(valor1 / valor2))
elif operacao == 4:
    print('O valor da operacao é {:.2f}'.format(valor1 * valor2))
else:
    print('Essa opção não existe')
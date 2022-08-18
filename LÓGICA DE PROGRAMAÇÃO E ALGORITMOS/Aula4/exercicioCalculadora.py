'''
Escreva um algoritmo que leia dois valores
numéricos e que pergunte ao usuário qual
operação ele deseja realizar: adição (+),
subtração (-), multiplicação (*), divisão (/)
e sair. Exiba na tela o resultado da operação
desejada
Repita até que a opção saída seja escolhida
(Exercício construído na aula prática 3)
'''

while True:
    opcao = int(input('Escolha uma opção\n'
                  '1 - Adição \n'
                  '2 - Subtração\n'
                  '3 - Divisão\n'
                  '4 - Multiplicação\n'
                  '6 - Sair\n'))
  
    if opcao == 6:
        break
    
    valor1 = float(input('Digite o primeiro numero: '))
    valor2 = float(input('Digite o segundo numero: '))



    if opcao == 1:
        print('O valor da operacao é {:.2f}'.format(valor1 + valor2))
    elif opcao == 2:
        print('O valor da operacao é {:.2f}'.format(valor1 - valor2))
    elif opcao == 3:
        print('O valor da operacao é {:.2f}'.format(valor1 / valor2))
    elif opcao == 4:
        print('O valor da operacao é {:.2f}'.format(valor1 * valor2))
    else:
        print('Essa opção não existe')

print('Fechando o programa')
    
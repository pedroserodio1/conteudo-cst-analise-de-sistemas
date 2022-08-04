print('----------------------------\n'
      'Escolha o que deseja comprar\n'
      '1- Maça\n'
      '2- Banana\n'
      '3- Laranja\n'
      '----------------------------\n')
produto = int(input('Digite sua opção: '))
qtd = int(input('Digite a quantidade: '))
if(produto == 1):
    valor = qtd* 2.3
    print('Você comprou {} maças e deu {} reais'.format(qtd, valor))
elif(produto == 2):
        valor = qtd*3.6
        print('Você comprou {} bananas e deu {} reais'.format(qtd, valor))
elif(produto == 3):
    valor = qtd* 1.85
    print('Você comprou {} laranjas e deu {} reais'.format(qtd, valor))
else:
    print('Opção inexistente')
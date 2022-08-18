#declaração de variaveis
valor = 0

print('Bem-Vindo a Pizzaria do Pedro Henrique Serôdio de Oliveira')
print('----------------------Cardápio-----------------------\n'
      '| Código | Descrição  | Pizza Média  | Pizza Grande |\n'
      '|   21   | Napolitana |     R$ 20,00 |     R$ 26,00 |\n'
      '|   22   | Margherita |     R$ 20,00 |     R$ 26,00 |\n'
      '|   23   | Calabresa  |     R$ 25,00 |     R$ 32,50 |\n'
      '|   24   | Toscana    |     R$ 30,00 |     R$ 39,00 |\n'
      '|   25   | Portuguesa |     R$ 30,00 |     R$ 39,00 |\n'
      '-----------------------------------------------------\n')

while True: #While pra só para quando o break for utilizado
      tamanho = input('Qual o tamanho da pizza que deseja (M/G): ')  #Pergunta o tamanho da pizza e atribui a variavel tamanho
      #verifica se o tamanho pedido esta correto
      if tamanho.upper() == 'M' or tamanho.upper() == 'G':
            cod = int(input('Entre com o código do sabor desejado: ')) #Pergunta o codigo da pizza e atribui a variavel cod
            #verifica qual pizza a pessoa pediu
            if cod == 21:
                print('Você pediu uma Pizza Napolitana') #Diz qual pizza o usuario pediu
                #verifica qual o tamanho pedido e atribui o valor certo
                if tamanho.upper() == 'M':
                    valor +=  20
                elif tamanho.upper() == 'G':
                      valor += 26
            elif cod == 22:
                  print('Você pediu uma Pizza Margherita') #Diz qual pizza o usuario pediu
                #verifica qual o tamanho pedido e atribui o valor certo
                  if tamanho.upper() == 'M':
                    valor +=  20
                  elif tamanho.upper() == 'G':
                      valor += 26

            elif cod == 23:
                  print('Você pediu uma Pizza Calabresa') #Diz qual pizza o usuario pediu
                  #verifica qual o tamanho pedido e atribui o valor certo
                  if tamanho.upper() == 'M':
                    valor +=  25
                  elif tamanho.upper() == 'G':
                      valor += 32.50

            elif cod == 24:
                  print('Você pediu uma Pizza Toscana') #Diz qual pizza o usuario pediu
                  #verifica qual o tamanho pedido e atribui o valor certo
                  if tamanho.upper() == 'M':
                    valor +=  30
                  elif tamanho.upper() == 'G':
                      valor += 39

            elif cod == 25:
                  print('Você pediu uma Pizza Portuguesa') #Diz qual pizza o usuario pediu
                  #verifica qual o tamanho pedido e atribui o valor certo
                  if tamanho.upper() == 'M':
                    valor +=  30
                  elif tamanho.upper() == 'G':
                      valor += 39

            else: #caso a opção não exista, ele diz opção invalida e repete o programa
                  print('Opção invalida')
                  continue
            
            #Perfunta se o usuario quer sair ou pedir mais alguma coisa
            opcao = int(input('Deseja pedir mais alguma coisa?\n'
                            '1 - Sim\n'
                            '0 - Não\n'))

            #verifica qual opcao escolheu e sai ou continua o programa dependendo da escolha
            if opcao == 1:
                continue
            elif opcao == 0:
                break
      else: #caso o tamanho não exista, ele repete o programa
            print('Opção invalida')
            continue
print('O total a ser pago é: {:.2f}'.format(valor))
                
                
                
    
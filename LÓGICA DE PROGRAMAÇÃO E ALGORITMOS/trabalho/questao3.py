#Função para perguntar a devolver o valor do volume da feijoada conforme a tabela
def volumeFeijoada():
    while True: #Cria um laço de repetição infinito 
        try: #Tenta executar as ações
            print('Menu Volume Feijoada')
            opcao = int(input('Entre com a quantidade que deseja(ml): '))
            # Verifica se a quantidade digitada esta entre 300 e 5000
            if opcao < 300: 
                print('Não aceitamos porções menores que 300ml ou maiores 5l. Tente novamente!')
                continue
            elif opcao > 5000: 
                print('Não aceitamos porções menores que 300ml ou maiores 5l. Tente novamente!')
                continue
            else:
                return opcao * 0.08
        except ValueError: #Disparado se o valor digitado não estiver correto
            print('Esse não é um valor aceito')
            continue
#Fim da função

#Função para ver qual a opção da feijoada
def opcaoFeijoada():
    while True: #cria um loop infinito
        print('Menu Opção Feijoada')
        print('Entre com a opção de Feijoada')
        opcao = input('b - Basica (Feijão + paiol + costelinha) \np - Premium (Feijão + paiol + costelinha + partes de porco) \ns -Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)\n')
        
        #Verifica as opções escolhidas e retorna o multiplicador correspondente a tabela
        if opcao.upper() == 'B':
            return 1
        elif opcao.upper() == 'P':
            return 1.25
        elif opcao.upper() == 'S':
            return 1.50
        else:
            print('Você não digitou uma opção valida')
            continue
#Fim da função

#Função que ve qual o acompanhamento da feijoada
def acompanhamentoFeijoada():
    valor = 0 #variavel que soma o valor dos acompanhamentos
    
    while True:
        print('Deseja mais algum acompanhamento:')
        opcao = int(input('0- Não desejo mais acompanhamentos (encerrar pedido)\n1- 200g de arroz\n2- 150g de farofa especial\n3- 100g de couve cozida\n4- 1 laranja descascada\n'))
        
        #Verifica a opção escolhida e soma o valor na variavel "valor", caso a opção seja 0, retorna o valor total de acompanhamento 
        if opcao == 1:
            valor = valor + 5
            continue
        elif opcao == 2:
            valor =valor + 6
            continue
        elif opcao == 3:
            valor= valor + 7
            continue
        elif opcao == 4:
            valor = valor + 3
            continue
        elif opcao == 0:
            return valor
        else:
            print('Opção invalida')
            continue
    

#programa principal
print('Bem-vindo ao Programa de Feijoada do Pedro Henrique Serôdio de Oliveira')


#Chama as funções e atribui as variaveis
valorVolume = volumeFeijoada()
valorOpcao = opcaoFeijoada()
valorAcrescimo = acompanhamentoFeijoada()

#faz o calculo do valor final da feijoada
valorTotal = (valorVolume * valorOpcao) + valorAcrescimo

#Diz pro usuarios a formula usada e os valores
print('O valor a ser pago é R${:.2f} (volume * opcao) + acompanhamento = ({:.2f} * {:.2f}) + {:.2f}'.format(valorTotal, valorVolume, valorOpcao, valorAcrescimo))


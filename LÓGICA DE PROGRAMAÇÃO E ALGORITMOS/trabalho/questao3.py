#Função para perguntar a devolver o valor do volume da feijoada conforme a tabela
def volumeFeijoada():
    while True: #Cria um laço de repetição infinito 
        try: #Tenta executar as ações
            print('Menu Volume Feijoada')
            opcao = int(input('Entre com a quantidade que deseja(ml): '))
            if opcao < 300: # se a a quantidade escolhida for menor que 300 retorna erro e volta pro começo do loop
                print('Não aceitamos porções menores que 300ml ou maiores 5l. Tente novamente!')
                continue
            elif opcao > 5000:
                print('Não aceitamos porções menores que 300ml ou maiores 5l. Tente novamente!')
                continue
            else:
                return opcao * 0.08
        except ValueError:
            print('Esse não é um valor aceito')
            continue
        

def opcaoFeijoada():
    while True:
        print('Menu Opção Feijoada')
        print('Entre com a opção de Feijoada')
        opcao = input('b - Basica (Feijão + paiol + costelinha) \np - Premium (Feijão + paiol + costelinha + partes de porco) \ns -Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)')
        
        if opcao.upper() == 'B':
            return 1
        elif opcao.upper() == 'P':
            return 1.25
        elif opcao.upper() == 'S':
            return 1.50
        else:
            print('Você não digitou uma opção valida')
            continue
        
def acompanhamentoFeijoada():
    valor = 0
    
    while True:
        print('Deseja mais algum acompanhamento:')
        opcao = int(input('0- Não desejo mais acompanhamentos (encerrar pedido)\n1- 200g de arroz\n2- 150g de farofa especial\n3- 100g de couve cozida\n4- 1 laranja descascada\n'))
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

valorVolume = volumeFeijoada()
valorOpcao = opcaoFeijoada()
valorAcrescimo = acompanhamentoFeijoada()

valorTotal = (valorVolume * valorOpcao) + valorAcrescimo

print('O valor a ser pago é R${:.2f} (volume * opcao) + acompanhamento = ({:.2f} * {:.2f}) + {:.2f}'.format(valorTotal, valorVolume, valorOpcao, valorAcrescimo))


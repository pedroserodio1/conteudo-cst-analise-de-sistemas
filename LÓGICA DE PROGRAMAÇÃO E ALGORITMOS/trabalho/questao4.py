#Programa de Pedro Henrique Serôdio de Oliveira
#Declaração de variaveis
codProd = 0
produto = []

#Função para cadastar produtos
def cadastarProduto(cod):
    print("Você selecionou a opção de cadastrar produto")
    print("Codigo do produto {}".format(cod))
    #pergunta os valores do produto
    nome = input("Por Favor entre com o NOME do Produto: ")
    fabricante = input("Por Favor entre com o FABRICANTE do Produto: ")
    valor = float(input("Por Favor entre com o VALOR do Produto: "))
    
    #criação do dicionario do produto
    produtoDic = {
        "codigo": cod,
        "nome": nome,
        "fabricante":fabricante,
        "valor": valor
    }
    
    #adicionando o dicionario do produto na lista de produtos
    produto.append(produtoDic.copy())
#fim cadastro produto
    
    
#Função para consultar produtos
def consultarProdutos():
    print("Você selecionou a Opção de Consultar Produto")
    while True:
        opcao = int(input("Escolha a opção desejada\n"
                          "1-Consultar todos os produtos\n"
                          "2-Consultar produtos por codigo\n"
                          "3-Consultar produtos por fabricante\n"
                          "4-Retornar\n"))
        if opcao == 1:
            for produtos in produto: #anda em todas as posições da lista de produtos
                print('--------------------------')
                for key, value in produtos.items(): #anda em todas os valores do dicionario e imprime na tela
                    print("{} : {}".format(key, value))
            print('--------------------------')
        elif opcao == 2:
            cod = int(input("Digite o CODIGO do Produto: "))
            for produtos in produto: #anda em todas as posições da lista de produtos
                if produtos['codigo'] == cod: #verifica se o codigo do dicionario é igual ao digitado pelo usuario
                    print('--------------------------')
                    for key, value in produtos.items(): #anda em todas os valores do dicionario e imprime na tela
                        print("{} : {}".format(key, value))
            print('--------------------------')
            
        elif opcao == 3:
            fab = input("Digite o FABRICANTE do Produto: ")
            for produtos in produto: #anda em todas as posições da lista de produtos
                if produtos['fabricante'] == fab: #verifica se o fabricante do dicionario é igual ao digitado pelo usuario
                    print('--------------------------')
                    for key, value in produtos.items(): #anda em todas os valores do dicionario e imprime na tela
                        print("{} : {}".format(key, value))
            print('--------------------------')
        elif opcao == 4:
            break
        else:
            print("Opção não existe")
#fim consultar Produtos
            
#Função de remover produto
def removerProduto():
    print("Você selecionou a opção de remover produto")
    cod = int(input("Digite o codigo a ser removido: "))
    for produtos in produto: #anda em todas as posições da lista de produtos
        if produtos['codigo'] == cod: #verifica se o codigo do dicionario é igual ao digitado pelo usuario
            produto.remove(produtos) #remove o item que tem o codigo do dicionario igual ao digitado da lista
#Fim remover produto

#Começo do bloco main
print("Bem vindo ao controle de estoque da Mercearia do Pedro Henrique Serôdio de Oliveira") 
while True:
    print("Escolha a Opção desejada")
    opcao = int(input('1-Cadastrar Produto\n'
                      '2-Consultar Produto\n'
                      '3-Remover Produto\n'
                      '4-Sair\n'))
    if opcao == 1:
        codProd += 1 #incrementa na variavel de codigo
        cadastarProduto(codProd)
        continue
    elif opcao == 2:
        consultarProdutos()
    elif opcao == 3:
        removerProduto()
    elif opcao == 4:
        break
    else:
        print("Opção inexistente")
    
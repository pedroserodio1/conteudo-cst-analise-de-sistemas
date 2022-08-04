print('Bem vindo a loja do Pedro Henrique Serôdio de Oliveira')
valorProd = float(input('Digite o valor do produto: ')) #le o valor do produto
qtd = int(input('Digite a quantidade: ')) #Le quantos produtos vao ser comprados

if qtd<=4: #verifica se a quantidade de produto é até 4
    valorTotal = qtd * valorProd #multiplica o valor do produto pela quantidade
    print('O valor sem desconto é R${:.2f}'.format(valorTotal)) #mostra na tela o valor total do produto sem desconto
    print('O valor com desconto é R${:.2f} (desconto de 0%)'.format(valorTotal)) #mostra na tela o valor total do produto com desconto
elif 5 <= qtd < 20 : #verifica se a quantidade de produto esta entre 5  e 19
    desconto = valorProd * (3/100) #Calcula  quantos é 3% do valor unitario do produto
    valorTotalComDesc = (valorProd - desconto) * qtd #Calcula o valor com desconto da compra
    valorTotalSemDesc = valorProd * qtd #Calcula o valor sem desconto da compra
    print("O valor sem desconto do produto é R${:.2f}".format(valorTotalSemDesc)) #Mostra na tela o valor do produto sem desconto
    print("O valor com desconto do produto é R${:.2f} (desconto de 3%)".format(valorTotalComDesc)) #Mostra na tela o valor do produto com desconto
elif 20<= qtd <100: #Verifica se a quantidade de produto esta entre 20 e 99
    desconto = valorProd * (6 / 100)  # Calcula  quantos é 6% do valor unitario do produto
    valorTotalComDesc = (valorProd - desconto) * qtd  # Calcula o valor com desconto da compra
    valorTotalSemDesc = valorProd * qtd  # Calcula o valor sem desconto da compra
    print("O valor sem desconto do produto é R${:.2f}".format(valorTotalSemDesc))  # Mostra na tela o valor do produto sem desconto
    print("O valor com desconto do produto é R${:.2f} (desconto de 6%)".format(valorTotalComDesc))
else: #caso não entre em nenhuma das condições acima o valor da quantidade é 100, então entrara aqui
    desconto = valorProd * (10 / 100)  # Calcula  quantos é 10% do valor unitario do produto
    valorTotalComDesc = (valorProd - desconto) * qtd  # Calcula o valor com desconto da compra
    valorTotalSemDesc = valorProd * qtd  # Calcula o valor sem desconto da compra
    print("O valor sem desconto do produto é R${:.2f}".format(valorTotalSemDesc))  # Mostra na tela o valor do produto sem desconto
    print("O valor com desconto do produto é R${:.2f} (desconto de 10%)".format(valorTotalComDesc)) #mostra na tela o valor do produto com desconto

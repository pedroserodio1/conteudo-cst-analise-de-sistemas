'''
Desenvolva um algoritmo que solicite
ao usuário o preço de um produto e um
percentual de desconto a ser aplicado a ele.
Calcule e exiba o valor do desconto e o preço
final do produto. (exercício da apostila – aula 2)
'''

preco = float(input('Digite o preço do produto: '))
perceDesconto = float(input('Digite o desconto(em %): '))

desconto = preco * (perceDesconto / 100)
precoFinal = preco - desconto

print('O produto ficou por {} (desconto de {} (em reais))'.format(precoFinal, desconto))

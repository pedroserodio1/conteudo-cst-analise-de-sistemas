'''
Escreva um programa que pergunte a
quantidade de km percorridos por um
carro alugado pelo usuário, assim como a
quantidade de dias pelos quais o carro foi
alugado. Calcule o preço a pagar, sabendo
que o carro custa R$ 60 por dia e R$ 0,15
por km rodado
'''

kmRodados = int(input('Digite quantos Kilometros (em KM) foi rodado: '))
diasAlugados = int(input('Quantos dias o carro ficou alugado: '))

precoKm = kmRodados * 0.15
precoDias = diasAlugados * 60
precoTotal = precoKm + precoDias

print('O valor total do aluguel ficou R${}\no valor por Km rodados ficou R${} e o de dias alugados R${}'.format(precoTotal, precoKm, precoDias))
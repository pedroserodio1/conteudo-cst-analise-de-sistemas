'''
Crie uma variável de string que receba uma
frase qualquer. Crie uma segunda variável,
agora contendo a metade da string digitada.
Imprima na tela somente os dois últimos
caracteres da segunda variável do tipo string
'''

frase = input('Digite uma frase qualquer: ')
tamString = len(frase)

metadeFrase = frase[:int(tamString/2)]

print(metadeFrase[-2:])
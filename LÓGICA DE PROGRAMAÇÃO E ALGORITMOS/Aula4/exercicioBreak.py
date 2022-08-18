'''
Escreva um algoritmo que fique
recebendo frases ou palavras
digitadas pelo usuário
Encerre o algoritmo quando a
palavra sair for digitada
'''

print('Digite qualquer palavra que irei repetir para você')
print('Digite "Sair" para encerrar')

while True:
    texto = input('')
    print(texto)
    if texto.upper() == 'SAIR':
        break
print('Saindo...')
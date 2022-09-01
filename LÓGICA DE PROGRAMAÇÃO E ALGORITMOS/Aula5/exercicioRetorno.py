"""
Escreva uma função para validar uma string.
Essa função recebe como parâmetro a string,
o número mínimo e máximo de caracteres.
Retorne verdadeiro se o tamanho da string
estiver entre os valores de mínimo e máximo,
e falso, caso contrário (elaborado com base
em Menezes, s. d.)
"""

def validaString(string, numMin, numMax):
    tam = len(string)
    if tam:
        if numMin <= tam <= numMax:
            return True
        else:
            return False
        
texto = input('Digite uma frase ou palavra: ')
min = int(input('Digite o numero minimo de caracteres: '))
max = int(input('Digite o numero maximo de caracteres: '))

res = validaString(texto, min, max)
print(res)

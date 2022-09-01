"""
Escreva uma rotina que crie uma borda ao
redor de uma palavra para destacá-la como
sendo um título. A rotina deve receber como
parâmetro a palavra a ser destacada. O
tamanho da caixa de texto deverá ser
adaptável de acordo com o tamanho da
palavra. Por exemplo:

+ -------+ +---+
|Vinícius| |Olá|
+ -------+ +---+
"""

def rotina(string):
    if len(string):
        print('+','-'*len(string) ,'+')
        print('| {} |'.format(string))
        print('+','-'*len(string) ,'+')

palavra = input('Digite alguma palavra: ')
rotina(palavra)
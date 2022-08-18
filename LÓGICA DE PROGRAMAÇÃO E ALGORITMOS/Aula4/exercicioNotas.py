'''
Escreva um algoritmo que calcule
a sua média de notas em
determinada disciplina
Vamos assumir que a média final
é dada pela média aritmética de
cinco notas digitadas
'''

cont = 0
somaNota = 0

while cont < 5:
    nota = float(input('Digite sua {}ª Nota: '.format(cont+1)))
    somaNota = somaNota + nota
    cont = cont+1
    
media = somaNota / 5

print('Sua media foi de {:.2f}'.format(media))
    
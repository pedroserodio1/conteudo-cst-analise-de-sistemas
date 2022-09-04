mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')

print(mochila[0])

for item in mochila:
    print('Na minha mochila tem: {}'.format(item))
    
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade
mochila_grande_invertida = upgrade + mochila

print(mochila)
print(upgrade)
print(mochila_grande)
print(mochila_grande_invertida)

#desempacotemento de parametro
def soma(*num):
    soma = 0
    print('Tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma

print('Resultado: {}'.format(soma(1, 2)))
print('Resultado: {}'.format(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

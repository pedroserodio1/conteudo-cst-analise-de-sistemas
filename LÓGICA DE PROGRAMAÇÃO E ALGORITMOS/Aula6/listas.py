mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print('Tupla: ', mochila)
mochila_lista = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila_lista)

#Adicionando item
mochila_lista.append('Ovos')
print('Lista: ', mochila_lista)

#Adicionando em posição especifica
mochila_lista.insert(1, 'Canivete')
print('Lista: ', mochila_lista)

#apagando posição especifica
del mochila_lista[1]
print('Lista: ', mochila_lista)

#Apagando item especifico
mochila_lista.remove('Ovos')
print('Lista: ', mochila_lista)



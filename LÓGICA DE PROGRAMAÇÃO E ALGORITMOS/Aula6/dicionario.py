game = {
    'nome': 'Super Mario',
    'Desenvolvedora': 'Nintendo',
    'ano': 1990
}

print(game)

print(game['nome'])
print(game['Desenvolvedora'])
print(game['ano'])

print(game.values())

for i in game.values():
    print(i)

print(game.keys())

for i in game.keys():
    print(i)

print(game.items())

for i, j in game.items():
    print('{} = {}'.format(i,j))
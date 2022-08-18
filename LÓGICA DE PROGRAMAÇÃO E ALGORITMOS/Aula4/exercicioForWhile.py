#Realize a sequência de print com for e while:

#Inteiros de 3 até 12, com 12 incluso
#Com for:
print('Com for: ')
for i in range(3, 13,1):
    print(i)

#Com while
print('Com While: ')
contA = 3
while contA < 13:
    print(contA)
    contA += 1
    
#Inteiros de 0 até 9, excluindo 9, com passo de 2
#Com for:
print('Com for: ')
for i in range(0, 9, 2):
    print(i)

#com while
print('Com while: ')
contB = 0
while contB < 9:
    print(contB)
    contB += 2
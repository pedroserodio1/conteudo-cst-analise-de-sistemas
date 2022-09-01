"""
Escreva uma função que calcule o fatorial
de um número recebido como parâmetro e
retorne o seu resultado
Faça uma validação dos dados por meio de
uma outra função, permitindo que somente
valores positivos sejam aceitos
Crie o help da sua função (exercício da
apostila – aula 5)
"""

def calculaFatorial(num, pos):
    """Função para calcular fatorial

    Args:
        num (int): numero que o fatorial sera calculado
        par (def): função para verificar se o numero é positivo

    Returns:
        int: resultado do fatorial
        string: Numero não positivo
    """
    
    res = 1
    if pos(num):
        for i in range(num, 0, -1): 
            res = res * i
        return res
    else:
        return 'Numero não positivo'

def ePositivo(num):
    if(num > 0):
        return True
    else: 
        return False

num = int(input('Digite um'))

print(calculaFatorial(3, ePositivo))
help(calculaFatorial)
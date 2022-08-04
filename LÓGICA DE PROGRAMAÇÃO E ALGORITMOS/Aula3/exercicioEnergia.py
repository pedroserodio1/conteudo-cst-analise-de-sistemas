"""
Escreva um programa que calcule o preço a
pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o
tipo de instalação: R para residências, I para
indústrias e C para comércios

Calcule o preço de acordo com a tabela a
seguir:
Preço por tipo e faixa de consumo
Tipo Faixa (kWh) Preço (R$)
Residencial
Até 500 0,40
Acima de 500 0,65
Comercial
Até 1000 0,55
Acima de 1000 0,60
Industrial
Até 5000 0,55
Acima de 5000 0,60
"""

consumo = float(input('Digite o valor da quantidade de consumo (em Kwh): '))
tipoInstalacao = input("Diga o tipo de residencia\n"
                       "R - Residencias\n"
                       "I = Industrias\n"
                       "C - Comercios\n")

if tipoInstalacao.upper() == 'R':
    if consumo <= 500:
        valor = consumo * 0.40
        print("Você ira pagar R${:.2f}".format(valor))
    else:
        valor = consumo * 0.65
elif tipoInstalacao == 'C':
    if consumo <= 1000:
        valor = consumo * 0.55
        print("Você ira ira pagar R${:.2f}".format(valor))
    else:
        valor = consumo * 0.60
        print("Você ira pagar R${:.2f}".format(valor))
elif tipoInstalacao == 'I':
    if consumo <= 5000:
        valor = consumo * 0.55
        print("Você ira pagar R${:.2f}".format(valor))
    else:
        valor = consumo * 0.60
        print("Você ira pagar R${:.2f}".format(valor))
else:
    print("Opção inexistente")
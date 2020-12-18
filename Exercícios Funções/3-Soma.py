# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def calcular(valor, valor2, valor3):
    return ( valor + valor2 + valor3)

valor = int(input("Insira o 1º valor: "))
valor2 = int(input("Insira o 2º valor: "))
valor3 = int(input("Insira o 3º valor: "))

print ('Soma dos Valores: ', calcular(valor, valor2, valor3))

# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     1   2   3  4
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprime(n):
    for i in range(1,  n + 1 ):
        print('')
        for j in range(1,  i +1):
              print (j, end=" ")   




n = int(input("Informe o número: "))
imprime(n)

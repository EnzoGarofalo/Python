# Implementar uma função que retorne verdadeiro se o número for primo
# (falso caso contrário). Testar de 1 a 100.

def  Éprimo(n):

    if  n < 2:       
        return False
    
    for i in (2,  n):
        if  (n % i == 0):
            return False
        else:
            return True

    n = 1
    for n in range(n, 101):
        if Éprimo(n):
            print ("Este Número: ", n, "é primo")
        else:
            print ("Este Número: ", n, " não é primo")   


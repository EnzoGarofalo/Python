# Implementar duas funções:
# ▪ Uma que converta temperatura em graus Celsius para Fahrenheit.
# ▪ Outra que converta temperatura em graus Fahrenheit para Celsius.

def  fahrenheit_celsius(temp): 
  
  #o Round() -- arredonda os números flutuantes
   return round(5 * (temp- 32) / 9)

def celsius_fahrenheit(temp):

   return  round(9 * temp / 5 + 32)


print ( 'Temperatura Celsius para Fahrenheit: ', celsius_fahrenheit(252.5), 'ºF')
print ( 'Temperatura Fahrenheit para Celsius: ', fahrenheit_celsius(65.5), 'ºC')
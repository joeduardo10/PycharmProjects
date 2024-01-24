import math
#from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # arredonda pra cima
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) # arredonda pra  baixo
print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) # arredonda :.2f
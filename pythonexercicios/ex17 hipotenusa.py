'''co = float(input('comprimento do cateto oposto: '))
ca = float (input('comprimeto do cateto adjacente: '))
hi= (co ** 2 + ca ** 2)** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float (input('comprimeto do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))




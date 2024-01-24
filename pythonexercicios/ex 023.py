'''nr = str(input('numero: '))
#print('a unidade é {},\na Dezena  é {}\na Centena é {}\na Milhar é {}'.format(nr[0], nr[1], nr[2], nr[3]))
print('milhar   {}, '.format(nr[:1]))
print('centena  {}, '.format(nr[1:2]))
print('dezena   {}, '.format(nr[2:3]))
print('unidade  {}, '.format(nr[3:4]))'''
num = int(input('informe o numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('analisando o numero {}'.format(num))
print('a unidade {}'.format(u))
print('a dezena  {}'.format(d))
print('a centena {}'.format(c))
print('a milhar  {}'.format(m))


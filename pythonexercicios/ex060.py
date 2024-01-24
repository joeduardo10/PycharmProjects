n = int(input('Digite um numero inteiro: '))
cont = n
fatorial = 1
while True:
     fatorial = fatorial * cont
     cont = cont - 1
     if cont < 1:
         break
print('Fatorial de {} é {}'.format(n, fatorial))




n = int(input('Digite um numero inteiro: '))
cont = n
s = 0
while True:
     s = s + cont
     cont = cont - 1
     if cont < 1:
         break
print(f'A soma de {n} é {s}')

n1=int(input('Digite o primeiro valor:'))
n2=int(input('Digite o segundo  valor:'))
n3=int(input('Digite o terceiro valor:'))

menor = n1
if n2 < n1  and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('o menor valor digitado foi {}'.format(menor))
print('O maior malor digitado foi {}'.format(maior))



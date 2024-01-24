n1 = int(input('Digite o Primeiro Valor: '))
n2 = int(input('Digite o Segundo Valor : '))
if n1 > n2:
    print('{} é maior {}'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}'.format(n1, n2))
else:
    print('{} é igual a {}'.format(n1, n2))
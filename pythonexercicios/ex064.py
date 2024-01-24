n = cont = soma = 0
print('999 para sair ')
n = int(input('Digite um numero inteiro: ' ))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero inteiro: '))
print('Foram digitados {}'.format(cont))
print('A soma dos valores digitados {} '.format(soma))


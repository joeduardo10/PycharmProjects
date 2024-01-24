opcao = ''
soma = n = x = maior = menor = media = 0
while opcao != 'N':        # while opcao in 'Nn':
    n = int(input('digite um numero inteiro: '))
    soma += n
    x += 1
    if x == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Deseja continuar[S/N]:')).strip().upper()[0]
media = soma / x
print('A media dos valores é {}'.format(media))
print('O maior valor digitado foi {}, e o menor valor foi {}'.format(maior, menor))

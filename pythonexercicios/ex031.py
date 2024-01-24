print('\n', '---' * 5, 'Jeito Normal', '---' * 5,'\n' )
distancia = float(input('Informe a distancia: '))
if distancia <= 200:
    print('O valor da passagem para {} é de R$ {:.2f}'.format(distancia, distancia * 0.50))
else:
    print('O Valor da passagem para {} é de R$ {:.2f}'.format(distancia, distancia * 0.45))
 # modo simplificado
print('\n', '---' * 5, 'Jeito simplificado', '---' * 5,'\n' )
print('voce esta prestes a começar uma viagem de {} Kms'.format(distancia))
preco = distancia * 0.50 if distancia <=200 else distancia * 0.45 # if simplificado
print('O valor da passagem é: R$ {:.2f}'.format(preco))
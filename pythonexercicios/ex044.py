print('{:=^40}'.format('Lojas Guanabara'))
preço = (float(input('Informe o preço: R$ ')))
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço formal')
print('[4] 3x ou mais no cartão: 20% de juros')
print('-=' * 10)
opcao = str(input("escolha a opção: "))
if opcao == '1':
    print('R$ {:.2f} à vista dinheiro/cheque: 10% de desconto {:.2f}'.format(preço, (preço * 0.90)))
elif opcao == '2':
    print('R$ {:.2f} à vista no cartão: 5% de desconto {:.2f}'.format(preço, (preço * 0.95)))
elif opcao == '3':
    print('R$ {:.2f} em até 2x no cartão: preço formal 2x {:.2f}'.format(preço,(preço/2)))
elif opcao == '4':
    nr_parc = (int(input('Quamtas parcelas: ')))
    parcela = (preço * 1.2) / nr_parc
    print('R$ {:.2f} em {} parcelas no cartão: 20% de juros. valor da parcela R$ {:.2f}'.format(preço, nr_parc,parcela))
else:
    print('opção de pagamento invalida')


Val_casa = float(input('Informe o valor da casa: R$ '))
Salario = float(input('Informe o salário:       R$ '))
tempo = int(input('Informe o numero de anos que pretende pagar: '))
tempo = tempo * 12
prestacao = Val_casa/tempo
limite = Salario * 0.30
if prestacao >= limite:
    print('Emprestimo negado ... limite é {:.2f} e a prestação {:.2f}'.format(limite, prestacao))
else:
    print('Emprestimo aprovado...prestação {:.2f}'.format(prestacao))
'''print('valor da casa {:.2f}'.format(Val_casa))
print('Salario {:.2f}'.format(Salario))
print('Limite da prestaçaõ {}'.format(limite))
print('Prestaçao {:.2f}'.format(prestacao))'''

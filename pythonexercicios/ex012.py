preco = float(input('informe o preço:  '))
desc = (preco * 5 )/100
preco = preco - desc
print('seu desconto é de: R$ {:.2f} e seu preço com desconto é de: R$ {}'.format(desc, preco))


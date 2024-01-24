# Dica 4 - list comprehension
# para criar uma lista de preços reajustados em 10% (mesmo que * 1.1)
lista_produtos = ['celular', 'tablet', 'fone de ouvido', 'camera', 'microfone']
lista_precos = [1000, 1200, 300, 500, 600]
preco_reajustado = [preco * 1.1 for preco in lista_precos]
print(preco_reajustado)
# mais fácil do que fazer um for para isso.

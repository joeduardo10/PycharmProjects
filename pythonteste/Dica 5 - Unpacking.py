# Dica 5 - Unpacking
lista_produtos = [
('celular', 1000),
('tablet', 1200),
('fone de ouvido', 300),
('camera', 500),
('microfone', 600)
]
for produto, preco in lista_produtos:
    print(f"{produto} com imposto custa {preco * 1.1}")
# ao invés de:
for item in lista_produtos:
    produto = item[0]
    preco = item[1]
print(f"{produto} com imposto custa {preco * 1.1}")
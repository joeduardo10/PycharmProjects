lista = [1, 2, 3, 'Gabriel']
print(lista)

lista1 = [[10], [1], [2,3,4],[3],['Gabriel']]
print(lista1) #lista completa
print(lista1[0]) # 1 elemento da lista
print(lista1[1])
print(lista1[4])
for i in lista1:
    if 'Gabriel' in i:
        print(f'achei voooce')

parentes = {'mamãe': 'Anile'}
print(parentes)
print(parentes.keys())
print(parentes.values())
print(parentes.items())
nossa_casa = [] # ou pode fazer assim  nossa_casa = list()
#nossa_casa = [{'': ''}, {'': ''}, {'': ''}]
nossa_casa = [{'mamãe': 'Anile'}, {'papai': 'Eduardo', 'peso': '95'}, {'filho': 'Lucas'}]
print(nossa_casa)

for i in nossa_casa:
    for k, v in i.items():
        if 'filho' in k:
            print(v)


gaveta = {'um': 'pincel'}
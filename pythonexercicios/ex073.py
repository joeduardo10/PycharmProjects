times =('Corintians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama',
        'Chapecoense', 'Atletico', 'Botafogo', 'Aletico-PR', 'Bahia', 'São Paulo', 'Fluminense',
        'Sport Recife', 'EC Vitoria', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico - GO')
print('-=' * 15)
print(f'Lista de Times do Brasileirão {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os últimos 4 colocados {times[-4:]}')''
print('-=' * 15)
print(f'times em ordem alfabetica {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está em  {times.index("Chapecoense")+1} Posição')

#for t in times:
#     print(t)

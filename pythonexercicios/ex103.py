#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretament
def ficha(jog = '<Desconecido>', gol=0):
    print(f'O jogador {jog} fez  {gol} gols no campeonato')


# Programa principal
n = str(input('Digite o nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol= g)
else:
    ficha(n, g)

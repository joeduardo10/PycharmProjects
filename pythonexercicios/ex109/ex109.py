#Exercício Python 109: Modifique as funções que form criadas no desafio 107
# para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda
preço = float(input('Digite um preço: R$ '))
print(f'O preço de  {moeda.moeda(preço)} aumentado em 10% é de:   {moeda.aumentar(preço, 10, True)}')
print(f'O preço de  {moeda.moeda(preço)} diminuido em 10% é de:   {moeda.diminuir(preço, 10, False)}')
print(f'O dobro de preço é:                              {moeda.dobro(preço, True)}')
print(f'O metade de preço é:                             {moeda.metade(preço, False)}')
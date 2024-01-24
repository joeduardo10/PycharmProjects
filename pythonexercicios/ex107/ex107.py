#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
preço = float(input('Digite um preço: R$ '))
print(f'O preço de R$ {preço} aumentado em 10% é de:  R$ {moeda.aumentar(preço, 10):.2f}')
print(f'O preço de R$ {preço} diminuido em 10% é de:  R$ {moeda.diminuir(preço, 10):.2f}')
print(f'O dobro de preço é:             R$ {moeda.dobro(preço):.2f}')
print(f'O metade de preço é:            R$ {moeda.metade(preço):.2f}')

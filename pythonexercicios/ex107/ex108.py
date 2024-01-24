#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
import moeda
preço = float(input('Digite um preço: R$ '))
print(f'O preço de  {moeda.moeda(preço)} aumentado em 10% é de:   {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'O preço de  {moeda.moeda(preço)} diminuido em 10% é de:   {moeda.moeda(moeda.diminuir(preço, 10))}')
print(f'O dobro de preço é:                              {moeda.moeda(moeda.dobro(preço))}')
print(f'O metade de preço é:                             {moeda.moeda(moeda.metade(preço))}')

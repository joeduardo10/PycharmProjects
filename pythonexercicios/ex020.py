from random import  shuffle
n1 = str(input('primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = shuffle(lista)
print('A ordem de apresentação sera:')
print (lista)
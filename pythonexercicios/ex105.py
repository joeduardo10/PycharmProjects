#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas  / – A maior nota    / – A menor nota   / – A média da turma / – A situação (opcional)
def notas(*n, sit=True):
    '''
    --> Função para analisar notas de varias palunos
    :param n:uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional
    :return:dicionário com várias informações sobre  a situação  do aluno
    '''
    r = dict()
    r['total'] = len(n)
    r['maior']  =max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'

    return r

#programa principal
resp = notas(5.5, 2.5, 8.5)
print(resp)
help(notas)

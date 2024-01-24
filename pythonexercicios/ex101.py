#Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.

def voto(ano):
    from datetime import datetime
    hoje = datetime.now().year
    dif_idade = hoje - ano
    if dif_idade < 16:
        return f'"você tem {dif_idade} anos"  Negado'
    elif dif_idade >= 18 and dif_idade < 65:
        return f'"você tem {dif_idade} anos" Voto Obrigatório'
    elif 16 <= dif_idade < 18 or dif_idade > 65:    #dif_idade < 18 or dif_idade > 65:
        return f'"você tem {dif_idade} anos"  Voto Opcional '


# Programa principal
ano_nasc = int(input('Em que ano você nasceu?  '))
print(voto(ano_nasc))

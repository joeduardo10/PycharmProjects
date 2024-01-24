from ex115.lib.interface import *
from time import sleep
while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    if resposta == 1:
        cabeçalho('opção 1')
    elif resposta == 2:
        cabeçalho('opção 2')
    elif resposta == 3:
        cabeçalho('saindo do sistema')
        break
    else:
        print('\033[31mDigite uma opção Valida\033[m')
        sleep(2)


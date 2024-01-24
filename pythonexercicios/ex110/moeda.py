def aumentar(vlr=0 , taxa=0, formato=False):
    res = vlr + (vlr * taxa)/100
    return res if formato is False else moeda(res)


def diminuir(vlr=0, taxa=0, formato=False):
    res = vlr - (vlr * taxa)/100
    return res if not formato  else moeda(res) # alternativo


def dobro(vlr=0, formato=False):
    res = vlr *2
    return res if formato is False else moeda(res)


def metade(vlr=0, formato=False):
    res = vlr /2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda= 'R$ '):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço = 0, taxaa = 10, taxar = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t {moeda(preço)}')
    print(f'O dobro do preço:\t {dobro(preço, True)}')
    print(f'A metade do preço:\t {metade(preço, True)}')
    print(f'com {taxaa}% de aumento\t {aumentar(preço, taxaa, True )}')
    print(f'com {taxar}% de redução:\t {diminuir(preço, taxar, True)}')

    print('-' * 30)




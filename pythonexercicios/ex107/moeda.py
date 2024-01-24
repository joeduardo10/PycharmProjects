def aumentar(vlr=0 , taxa=0):
    res = vlr + (vlr * taxa)/100
    return res


def diminuir(vlr=0, taxa=0):
    res = vlr - (vlr * taxa)/100
    return  res


def dobro(vlr=0):
    res = vlr *2
    return res


def metade(vlr=0):
    res = vlr /2
    return res


def moeda(preço=0, moeda= 'R$ '):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

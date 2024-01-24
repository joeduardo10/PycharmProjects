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

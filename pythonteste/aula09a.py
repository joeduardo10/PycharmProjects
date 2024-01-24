frase = 'Curso em video Python'
print ('imprime frase                                      ', frase)
print('impreme o caracter de nro indice 9                  ', frase[9])
print('seleciona do 9 ao 12   1 menos no final             ', frase[9:13])
print('seleciona do 9 ao 20   1 menos no final             ', frase[9:21])
print('seleciona do 9 ao 20   pulando de 2 em 2            ', frase[9:21:2])
print('seleciona do 0 ao 5                                 ', frase[:5])
print('seleciona do 15 ao final                            ', frase[15:])
print('seleciona 9 ao fim pulando de 3 em 3                ', frase[9::3])
print('conta qts caracteres tem a frase                    ', len(frase))
print('conta qts caracteres o  tem a frase                 ', (frase.count('o')))
print('conta qts caracteres o  tem de 0 a 12               ', (frase.count('o',0 ,13)))
print('conta em caractere começa .deo.                     ', (frase.find('deo')))
print('Verifica se existe a frase true/false               ', ('Curso'in frase))
print('troca Python por Android                            ', frase.replace('Python','Android'))
print('Transforma tudo em maiusculo                        ', frase.upper())
print('Transforma tudo em minusculo                        ', frase.lower())
print('Transforma o primeiro caracter em maiusculo         ', frase.capitalize())
print('Transforma em minusculo palavra por palavra         ', frase.title())
frase_1 = '   Aprenda Python  '
print('                                                     ', frase_1)
print('remove espaços no começo e no final                  ', frase_1.strip())
print('remove espaços do fim                                ', frase_1.rstrip())
print('remove espaços do começo                             ', frase_1.lstrip())
print('junção com "-" que pode ser trocado por espaço       ', '-'.join(frase))






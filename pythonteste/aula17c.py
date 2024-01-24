a = [2, 3, 4, 7]
b = a[:]  #  b = a  #altera as duas listas sempre que vc  iguala as duas listas mas,  b = a[:] cria uma copia de a
b[2] = 8
print(f' lista A {a}')
print(f' lista B {b}')

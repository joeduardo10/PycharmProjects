n = (input("digite um texto: "))
result = ' '.join(format(ord(c), 'b') for c in n)
print(result)
#print('{}'.format(bin(n)[2:]))
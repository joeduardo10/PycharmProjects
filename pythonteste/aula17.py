num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
#num.sort(reverse=True)
num.insert(2, 0)
#num.pop(2)
num.insert(1, 2)
#num.remove(2) # remove o primeiro repetido
print(num)
print(f'essa lista tem {len(num)} elementos')
if 4 in num:
    num.remove(4)
else:
    print('não achei o valor 4')
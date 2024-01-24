lanche = ('hanburguer', 'suco', 'pizza', 'pudin', 'batata frita')

for cont in range (0,len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
print('~~~~~~' * 20)
for comida in lanche:
       print(f'Eu vou comer {comida}')
print('~~~~~~' * 20)
for pos, comida in enumerate (lanche):
       print(f'Eu vou comer {comida} na posição {pos}')

print("eu comi pra caralho")

print (sorted(lanche))
media = 0
maior_homem = 0
nome_velho = ''
tot_mulher20 = 0
for i in range (1, 5):
    print('--'*10, '{}ª Pessoa'.format(i), '--'*10)
    nome = str(input('informe o nome: ')).strip()
    idade = int(input('Informe a idade: '))
    sexo = str(input('informe o sexo [M / F ] : ')).strip()
    media += idade
    if i == 1 and sexo in 'Mm':
        maior_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_homem:
        maior_homem = idade
        nome_velho =  nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1


print('A média de idade do grupo é: {}'.format(media/4))
print('O homem mais velho te {} e se chama {}'.format(maior_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot_mulher20))


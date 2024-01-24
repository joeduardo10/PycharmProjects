pessoas = {}
pessoas = {'nome':'José Eduardo','Idade':'25','sexo':'nasculino'}
print(pessoas)
print(pessoas['nome'])
print(pessoas['Idade'])
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k, end=" ")
print()
for p in pessoas.values():
    print(p, end=" ")
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
    
del pessoas['sexo']
print (pessoas)

pessoas['nome'] = 'Mariane'
print(pessoas)

pessoas['peso']=98.5
print(pessoas)

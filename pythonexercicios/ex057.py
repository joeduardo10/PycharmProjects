sex = str(input('informe o sexo M/F: ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('dados invalidos')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sex))


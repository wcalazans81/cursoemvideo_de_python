sexo = str(input('Quer continuar? [M/F] ')).strip().upper()[0]
while sexo not in 'SsNn':
    sexo = str(input('Por favor digite um sexo válido! [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')

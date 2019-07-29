tot_pessoas18 = 0   # total de pessoas maiores que 18
totalH = 0  # total homens cadastrados
totalm = 0  # total mulheres cadastradas com menos de 20
while True:
    print('---' * 10)
    print('Cadastre uma pessoa')
    print('---' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/f]')).upper().strip()[0]
    print('---' * 10)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer Continuar: [S/N]')).upper().strip()[0]
    if continuar == 'S':
        if idade > 18:
            tot_pessoas18 = tot_pessoas18 + 1
        if sexo == 'M':
            totalH = totalH + 1
        if sexo == 'F' and idade < 20:
            totalm = totalm + 1
    else:
        break
print('Total de pessoas maiores que 18 é {} '.format(tot_pessoas18))
print('Ao todo temos {} homens cadastrado'.format(totalH))
print('E temos {} mulheres com menos de 20 anos '.format(totalm))



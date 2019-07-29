soma = 0
media = 0
toth = 0
nomev = ''
totm = 0
for c in range(1, 5):
    print('--' * 4, '{}º pessoa'.format(c), '--' * 4)
    nome = (input('Nome:')).strip()
    idade: int = int(input('IDADE:'))
    sexo = str(input('Sexo [M/F]:').strip())
    soma = soma + idade
    if c == 1 and sexo in 'Mm':
        toth = idade
        nomev = nome
    if sexo in 'Mm' and idade > toth:
        toth = idade
        nomev = nome
    if sexo in 'Ff' and idade > 20:
        totm = totm + 1
media = soma / 4
print('A média de idade  do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(toth, nomev))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm))


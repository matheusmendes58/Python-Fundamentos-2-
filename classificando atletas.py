import datetime
anonacs = int(input('digite o ano de nascimento:'))
ano_atual = datetime.date.today()
idade = ano_atual.year - anonacs
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: JUNIOR')
elif idade > 14 and idade <= 25:
    print('Classificação: SENIOR')
elif idade > 25:
    print('Classificação: MASTER')
#   outra opção else print(' Classificação: MASTER')

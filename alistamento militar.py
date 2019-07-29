import datetime
hj = datetime.date.today()
ano = int(input('ano de nascimento:'))
alist = hj.year - ano   # anos que a pessoa tem
x = alist - 18
ano_alistamento = hj.year - alist   # ano que foi o alismento
if alist > 18:
    print('quem nasceu em {} tem {} anos em {}.'
          '\nVocê ja deveria ter se alistado há {} anos.'
          '\nSeu alistamento foi em {}.'.format(ano, alist, hj.year, x, hj.year - x))
elif alist == 18:
    print('quem nasceu em {} tem {} anos em {}.'
          '\nVoçê tem que se alistar IMEDIATAMENTE.'.format(ano, alist, hj.year))
else:
    print('Quem nasceu em {} tem {} anos em {}.'
          '\nAinda faltam {} anos para o alistamento'
          '\nSeu alistamento será em {}.'.format(ano, alist, hj.year, (18 - alist), (18 - alist) + hj.year))


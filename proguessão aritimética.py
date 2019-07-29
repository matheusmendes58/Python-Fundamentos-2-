print('==' * 50)
print('10 TERMOS DE UMA PA')
print('==' * 50)
primeiro_termo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
for c in range(0, 10):
    print(' {} '.format(primeiro_termo + c * razao), end='->')
print(' ACABOU')



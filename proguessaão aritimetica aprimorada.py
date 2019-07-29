print('Gerador de PA')
print('-=-=-=' * 10)
n1 = int(input('primeiro termo:'))
r = int(input('razão da PA:'))
print(n1, end=' -> ')
x = 0
total = 0
c = 8
while c != 0:
    total = total + c
    while x <= total:
        x = x + 1
        print('{}'.format(n1 + x * r), end=' -> ')
    print('pausa')
    c = int(input('quantos termos você que mostrar a mais :'))
print('progama finalizado {} termos estabelecidos'.format(total + 2))

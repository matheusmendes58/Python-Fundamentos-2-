print('=' * 30)
print('{:^30}'.format('BANCO CCC'))
print('=' * 30)
saque = int(input('Que Valor vcoçê quer sacar R$:'))
total = saque
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula = total_cedula + 1
    else:
        if total_cedula > 0:
            print('Total de {} cédulas de R$ {}'.format(total_cedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 30)
print('Obrigado VOLTE SEMPRE !')

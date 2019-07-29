num = int(input('digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[34m', end=' ')
    print(c, end=' ')
print('\n\33[m o número {} foi divido {} vezes'.format(num, tot))
if tot == 2:
    print(' Esse número é primo')
else:
    print(' Esse número não é primo')


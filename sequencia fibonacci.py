print('---' * 50, '\nSequencia fibonacci ')
print('---' * 50)
x = int(input('Quantos termos quer mostrar : '))
t1 = 0
t2 = 1
print('~' * 50)
print('{} -> {} '.format(t1, t2), end='')
c = 3
while c <= x:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
print('-> fim')




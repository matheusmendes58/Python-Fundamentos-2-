s = 0
for x in range(1, 7):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
     s = s + num
print('a soma dos números pares são: {}'.format(s))
if s == 0:
    print('todos os números são impares ')





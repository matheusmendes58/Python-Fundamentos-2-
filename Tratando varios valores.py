c = 0
total = 0
numeros_digitados = 0
while c != 999:
    c = int(input('digite um numero [999 para parar]:'))
    numeros_digitados = numeros_digitados + 1
    total = total + c
print('voce digitou {} numeros e a soma entre eles foi {}'.format(numeros_digitados - 1, total - 999))


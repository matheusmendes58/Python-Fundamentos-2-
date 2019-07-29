total_numeros_digitados = 0
soma = 0
while True:
    n = int(input('digite um numero: (digite 999 para sair)'))
    if n == 999:
        break
    total_numeros_digitados = total_numeros_digitados + 1
    soma = soma + n
print('a soma de {} valores é {}'.format(total_numeros_digitados, soma))
print('FIM')

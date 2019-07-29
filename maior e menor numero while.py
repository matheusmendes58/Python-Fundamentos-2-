continuar = 'S'
numeros_digitados = 0
media = 0
divisor = 0
numero_maior = 0
numero_menor  = 0
while continuar == 'S':
    numero = int(input('digite um numero:'))
    continuar = input('deseja continuar [S/N]:').upper().strip()[0]
    numeros_digitados = numeros_digitados + 1
    media = media + numero  # somatoria dos numeros em loop
    divisor = divisor + 1   # somatoria do loop igual numeros digitados acima para formar media
    if numeros_digitados == 1:
        numero_maior = numeros_digitados
        numero_menor = numeros_digitados
    else:
        if numeros_digitados > numero_maior:
            numero_maior = numeros_digitados
        if numeros_digitados < numero_menor:
            numero_menor = numero
    '''
    condições "if" errada erro lógico oculto no loop
    '''
print('voce digitou {} numeros e a média foi {}'.format(numeros_digitados, media / divisor))
print('o maior valor é {} e menor valor é {}'.format(numero_maior, numero_menor))



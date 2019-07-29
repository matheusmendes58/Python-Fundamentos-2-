import random
from time import sleep

print('vamos jogar PAR ou IMPAR')
print('-=' * 30)
v = 0
while True:
    computador = random.randint(0, 10)
    user = int(input('digite um valor:'))
    print('---' * 30)
    PI = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    if PI != 'P' and PI != 'I':
        print('Coloque apenas P ou I')
        print('Renicie o game')
        break
    soma = user + computador
    par = soma % 2 == 0
    impar = soma % 2 == 1
    if par == True:
        print('Voçê jogou {} e o computador jogou {} Total deu {} PAR'.format(user, computador, soma))
        if PI == 'P':
            print('Voçê ganhou')
            print('Vamos jogar novamente...')
            sleep(3)
            print('---' * 30)
            v = v + 1
        else:
            print('Você perdeu')
            break
    elif impar == True:
        print('Voçê jogou {} e o computador jogou {} Total deu {} impar'.format(user, computador, soma))
        if PI == 'I':
            print('Voçê ganhou')
            print('---' * 30)
            v = v + 1
        else:
            print('Você perdeu')
            break
print('---' * 30)
print('O game acabou voce venceu {} vezes'.format(v))

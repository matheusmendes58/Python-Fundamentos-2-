import random
import time
print('suas opções:'
      '\n[ 0 ] pedra'
      '\n[ 1 ] papel'
      '\n[ 2 ] tesoura')
op = int(input('Qual é sua jogada:'))
time.sleep(1)
print('Jo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('Po')
print('=' * 50)
maquina = [0, 1, 2]
maquina = random.choice(maquina)
if maquina == 0:
    print('Computador escolheu "pedra"')
elif maquina == 1:
    print('computador escolheu "papel"')
elif maquina == 2:
    print('Computador escolheu "tesoura"')
if op == 0:
    print('O jogador escolheu "pedra"')
    if maquina == 0:
        print('=' * 50)
        print('EMPATADO')
    elif maquina == 1:
        print('=' * 50)
        print('O Computador ganhou')
    elif maquina == 2:
        print('=' * 50)
        print('O jogador ganhou')
elif op == 1:
    print('O jogador escolheu "papel"')
    if maquina == 0:
        print('=' * 50)
        print('O Jogador ganhou')
    elif maquina == 1:
        print('=' * 50)
        print('EMPATADO')
    elif maquina == 2:
        print('=' * 50)
        print('O Computador ganhou')
elif op == 2:
    print('O jogador escolheu "tesoura"')
    if maquina == 0:
        print('=' * 50)
        print('O Computador ganhou')
    elif maquina == 1:
        print('=' * 50)
        print('O Jogador ganhou')
    elif maquina == 2:
        print('=' * 50)
        print('EMPATOU')
else:
    print('escolha a opção correta')








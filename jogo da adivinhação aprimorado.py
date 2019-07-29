from time import sleep
import random

print('Sou seu computador...')
sleep(5)
n = random.randint(0, 10)
print('Acabei de pensar em um número de 0 a 10'
      '\nSera que voçê consegue adinvinhar qual foi')
x = int
tentativas = 0
while x != n:
    jogador = int(input('Qual é seu palpite:'))
    tentativas = tentativas + 1
    if jogador > n:
        print('Menos... Tente mais uma vez')
    elif jogador < n:
        print('Mais... Tente mais uma vez:')
    if jogador == n:
        sleep(2)
        print('Acertou Parabéns')
        break
sleep(2)
print('Voçê acertou na {}º tentativa'.format(tentativas))

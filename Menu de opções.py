from time import sleep
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo número:'))
x = 0
while x != 5:
    print('\n[ 1 ] somar'
          '\n[ 2 ] multiplicar'
          '\n[ 3 ] maior'
          '\n[ 4 ] novos números'
          '\n[ 5 ] sair do progama')
    x = int(input('>>> Qual é sua opção:'))
    print('===' * 50)
    if x == 1:
        soma = n1 + n2
        print('a soma entre {} e {} é {}'.format(n1, n2, soma))
        print('===' * 50)
    elif x == 2:
        multi = n1 * n2
        print('a multiplicação entre o numero {} e {} é {}'.format(n1, n2, multi))
        print('===' * 50)
    elif x == 3:
        if n1 > n2:
            maior = 0
            maior = n1
            print('o numero maior é {}'.format(maior))
        else:
            maior = n2
            print('o numero maior é {}'.format(maior))
    elif x == 4:
        print('digite os numeros novamente')
        print('===' * 50)
        n1 = float(input('Digite o primeiro numero:'))
        n2 = float(input('digite o segundo número:'))
    elif x == 5:
        print('processando...')
        sleep(5)
        print('Fim do progama')
    else:
        print('opção errada tente novamente')








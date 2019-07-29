while True:
    n_digitado = int(input('Quer ver a tabuada de qual valor: '))
    if n_digitado < 0:
        break
    print('-' * 30)
    for c in range(0, 11):
        resultado = n_digitado * c
        print('{} x {} = {}'.format(n_digitado, c, resultado))
    print('-' * 30)
print('PROGAMA TABUADA ENCERRADO. Volte sempre')



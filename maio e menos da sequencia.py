totmaior = 0
totmenor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}º pessoa:'.format(c)))
    if c == 1:
        totmaior = peso
        totmenor = peso
    else:
        if peso > totmaior:
            totmaior = peso
        if peso < totmenor:
            totmenor = peso
print('maior peso lido foi {}Kg \nmenor peso lido foi {}Kg'.format(totmaior, totmenor))

p1 = float(input('digite o primeiro segmento:'))
p2 = float(input('digite o segundo segmento:'))
p3 = float(input('digite o terceiro segmento:'))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos FORMAM TRIANGULO', end='')
    if p1 == p2 and p2 == p3:
        print(' EQUILATERO')
    elif p1 == p2 and p2 == p3 or p1 != p2 or p2 != p3:
        print(' ISÓCELES')
    elif p1 != p2 and p2 != p3 and p3 != p1:
        print(' ESCALENO')
else:
    print('Os segmentos não formam triangulo')
'''
maneira mais correta primeiro elif por o codigo do escaleno 
e por fim else print('isóceles').
'''

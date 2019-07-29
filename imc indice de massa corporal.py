kg = float(input('Qual é o seu peso: (KG):'))
alt = float(input('Qual é o sua altura (m):'))
imc = kg / (alt ** 2)
print('O imc desta pessoa é de {:.2f}'.format(imc))
if imc >= 18.5 and imc <= 25:
    print('PARABÉNS, voçê está na faixa de peso NORMAL')
elif imc > 25 and imc <= 30:
    print('Voçê está na faixa de SOBREPESO')
elif imc > 30 and imc <= 40:
    print('Voçê esta na faixa da OBESIDADE')
elif imc > 40:
    print('Cuidado você esta com OBESIDADE MORBIDA')
else:
    print('PRECISA ENGORDAR')



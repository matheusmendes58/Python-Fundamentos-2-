from datetime import date

ano_atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('em que ano a {}º pessoa nasceu:'.format(c)))
    idade = ano_atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade '
      '\nE também tivemos {} pessoas menores de idade'.format(totmaior, totmenor))

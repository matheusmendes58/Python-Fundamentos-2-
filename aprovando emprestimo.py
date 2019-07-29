vc = float(input('Qual valor da casa: R$'))
s = float(input('Qual o seu salario: R$'))
f = int(input('quantos anos de financiamento: R$'))
pre = vc / (f * 12)
po = (s * 30) / 100
print('Para pagar uma casa de R${} em {} anos '
      '\na prestação será de R$ {:.2f}'.format(vc, f, pre))
if pre <= po:
    print('emprestimo pode ser  concedido ')
else:
    print('emprestimo não pode ser  concedido')



print('=' * 20, 'Loja Qualquer', '=' * 20)
p = float(input('Qual valor das compras R$:'))
print('\n[ 1 ] à vista dinheiro/cheque'
      '\n[ 2 ] à vista cartão'
      '\n[ 3 ] 2x no cartão'
      '\n[ 4 ] 3x ou mais no cartão')
op = int(input('Qual é a opção:'))
d = int     # variavel qualquer para calculo desconto etc
if op == 1:
    d = (p * 10) / 100
    d = p - d
    print('o valor da sua compra é R${:.2f} com desconto a vista é R${:.2f}'.format(p, d))
elif op == 2:
    d = (p * 5) / 100
    d = p - d
    print('o valor da sua compra é R${:.2f} com desconto no cartão a vista é R${:.2f}'.format(p, d))
elif op == 3:
    d = p / 2
    print('o valor da sua compra é R${:.2f} com pagamento no cartão em 2x é R${:.2f}'.format(p, d))
elif op == 4:
    x = int(input('quantas parcelas:'))
    # x = variavel para parcelamento
    if x >= 3:
        j = float     # variavel para juros
        j = (p * 20) / 100
        d = (p * 20) / 100
        d = p + d
        print('sua compra sera parcelada em {}x de R${:.2f} com juros'
              '\nSua compra de R${:.2f} vai custar R${:.2f} no final'.format(x, (p + j) / x, p, d))
    else:
        j = p / x   # calculo do parcelamento
        print('sua compra sera parcelada em {}x de R${:.2f} Sem juros'.format(x, j))
else:
    print('o valor da sua compra é R${:.2f}'.format(p))
    print('escolha uma opção viavel')









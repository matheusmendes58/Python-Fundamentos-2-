total_compra = 0
maior_mil = 0
produto = 0
menor_preco = 0
n_produto_barato = ''
print('---' * 30)
print('LOJA loja '.center(45))
print('---' * 30)
while True:
    n_produto = str(input('Nome do produto'))
    preco = float(input('Preço: '))
    produto = produto + 1
    total_compra = total_compra + preco
    if preco > 1000:
        maior_mil = maior_mil + 1
    if produto == 1:
        menor_preco = preco
        n_produto_barato = n_produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            n_produto_barato = n_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer contiuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('O total da compra  foi RS:{:.2f}'.format(total_compra))
print('Temos {} custando mais de 1000 reais'.format(maior_mil))
print('O produto mais barato foi {} que custa RS{:.2f}'.format(n_produto_barato, menor_preco))
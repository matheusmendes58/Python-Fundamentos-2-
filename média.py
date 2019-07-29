nota1 = float(input('digite a primeria nota:'))
nota2 = float(input('digite a segunda nota:'))
m = (nota1 + nota2) / 2  # m = média
print('tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, m))
if m < 5:
    print('O aluno esta REPROVADO')
elif m >= 5 and m < 7:
    print('O aluno esta de RECUPERAÇÂO')
elif m >= 7:
    print('O aluno esta APROVADO')

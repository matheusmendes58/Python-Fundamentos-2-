frase = str(input('digite uma frase:')).upper().strip()
print('O inverso de "{}" é "{}"'.format(frase, frase[::-1]))
palavra = frase.split()     # divisão dos espaços
juntar_palavras = ''.join(palavra)  # junta todos os espaços letras etc
if juntar_palavras == juntar_palavras[::-1]:
    print('Temos um palindromo ')
else:
    print('A frase digitada não é um palindromo')


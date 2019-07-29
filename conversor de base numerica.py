num = int(input('digite um numero inteiro:'))
print('escolha uma das bases para conversão:'
      '\n[1] para binario'
      '\n[2] para octal'
      '\n[3] para hexadecimal')
opcao = int(input('sua opção:'))
if opcao == 1:
    print('{} convertido para binario é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida tente novamente')

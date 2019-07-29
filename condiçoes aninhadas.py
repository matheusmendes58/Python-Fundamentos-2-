nome = str(input('qual é o seu nome: ')).strip().upper()
if nome == 'MATHEUS':
    print('Que nome bonito')
elif nome == 'MARCOS' or nome == 'MIGUEL' or nome == 'MILTON' or nome == 'GIL':
    print('Seu nome é maravilhoso')
elif nome in 'JULIANA ANA MARIA GLORIA':
    print('belo nome feminino')
else:
    print('seu nome é bem normal')
print('tenha um bom dia {}!'.format(nome))

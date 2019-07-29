v = ''
v = str(input('digite seu sexo [M/F]:')).upper().strip()[0]
while v != 'M' and v != 'F':
    v = str(input('Dados invalidos. Por favor, informe seu sexo:')).upper().strip()[0]
if v == 'M':
    v = 'Masculino'
else:
    v = 'Feminino'
print('Sexo {} cadastrado com sucesso'.format(v))

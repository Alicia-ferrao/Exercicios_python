sexo = ''
sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = input('Digite o seu sexo: [M/F] ').upper().strip()

if sexo == 'F':
    sexo = 'Feminino'
elif sexo == 'M':
    sexo = 'Masculino'

print('Sexo registado: {}'.format(sexo))
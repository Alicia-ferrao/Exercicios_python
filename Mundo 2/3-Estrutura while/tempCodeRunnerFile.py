sexo = ''
while sexo !='F' and sexo != 'M' :
    sexo = str(input('Digite o seu sexo : [M/F]')).upper().strip()

    if sexo == 'F'.upper():
        sexo ='Feminino'
    elif sexo == 'M'.upper():
        sexo ='Masculino'

print('Sexo resgistado {}' .format(sexo))
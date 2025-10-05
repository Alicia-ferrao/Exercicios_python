nome = str(input('Qual o seu nome ? : '))
if nome == 'Gustavo':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("O teu nome é bem popular em Portugal")
elif nome in 'Alicia Fatinha Luzinha Chana ':
    print('Belo nome feminino!')

else:
    print('O teu nome é bem normal.')
print('Tenha um bom dia {} !' .format(nome))


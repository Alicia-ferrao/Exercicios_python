
nome = str(input('Digite o seu nome : '))

print('O seu nome em maiucula é {}' .format(nome.upper()))
print('O seu nome minuscula é : {}'.format(nome.lower()))
print('O seu nome tem {} letras' .format(len(nome)))
print('O seu nome tem {} letras' .format(len(nome.strip())))
nome_dividido = nome.split()
print('o primeiro nome tem {} letras' .format(len(nome_dividido)))


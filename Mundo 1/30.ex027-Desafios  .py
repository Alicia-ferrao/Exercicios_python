nome = str(input('Digite o seu nome: '))

dividido = nome.split()
print("Muito prazer te conhecer {} " .format(dividido[0]))
print("O seu primeiro nome é {}" .format(dividido[0]))
print("O seu ultimo nome é {}" .format(dividido[len(dividido)-1]))
print(dividido)


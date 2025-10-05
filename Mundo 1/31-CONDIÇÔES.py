nome  = str(input('Qual é o seu nome : '))
if nome == 'Alicia':
    print("Que nome lindo tu tens !")
   
else:
    print("O teu nome é tão normal ")
print('Ola {}' .format(nome))




nota1 = float(input('Digite a primeira nota : '))
nota2 = float(input('Digite a segunda nota : '))
media = (nota1 + nota2)/2
print('A sua media é de {:.1f}' .format(media))

if media >= 10 :
    print('Aluno aprovado')
else:
    print('Aluno reprovado')


num = int(input("Digite um numero :"))

if num % 2 == 0 :
    print('numero par')
else:
    print('numero impar')

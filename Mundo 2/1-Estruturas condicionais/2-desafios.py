salario = float(input('Digite o valor do seu salário: '))
casa = float(input('Digite o valor da casa que pretende : '))
anosP = float(input('Vai pagar em quanto tempo ? '))

prestação = casa / (anosP * 12)
minimo = salario * 30 / 100

print('Para pagar a casa de {:.2f} euros em {} anos, a prestação será de {:.2f} euros' .format(casa, anosP, prestação))

if prestação <= minimo :
    print('O seu crédito foi aprovado')
else:
    print('O seu crédito foi negado!')
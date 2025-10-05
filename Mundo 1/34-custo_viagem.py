viagem = float(input('Qual a distância da sua viagem :'))
print("Você está prestes a comecar uma viagem de {} km" .format(viagem))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco= viagem*0.45
print('O preço da sua passagem é de {:.2f}' .format(preco))
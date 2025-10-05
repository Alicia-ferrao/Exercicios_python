vel = int(input('Qual é a velocidade atual do seu carro : '))


if vel <= 30 :
    print('Parabens , estás a conduzir com uma velocidade adequada.')
else:
    if vel >= 30 and vel < 50 :
        print('ATENÇÃO!! conduz com cuidado. Estás quase a ultrapassar o limite de velocidade')
    else:
        print('MULTADO!  Você escedeu o limite permitido que é 80 km/h')
        multa = (vel-80) * 7
        print('Você deve pagar uma multa de {} euros' .format(multa))

print('Tenha bom dia, conduza com segurança!!!')
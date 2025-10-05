


while True :
    tab = int(input("Queres ver a tabuada de que valor ? "))
    if tab < 0 :
        break

    print(f'Tabuada do {tab}')
    cont = 1
    while cont <= 10:
        print(f'{cont} x {tab} = {cont*tab}')
        cont += 1
    print('-'*20)
print('Programa encerrado! Volte Sempre.')
  



cont =s = 0

while True :
    num = int(input('Digite um numero : '))
 
   
    if num == 999:
        break
    s = s + num
    cont = cont +1


print(f'Foram digitados {cont} numeros')
print(f'A soma dos valores é {s}')



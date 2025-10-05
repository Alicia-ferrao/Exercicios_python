for c in range(1,10):
    print(c)


c = 1
while c<10 :
    print(c)
    c = c +1
print(c)


n = 1
while n != 0:
    n = int(input('Digite um valor : '))

r = 'S'
while r == 'S':
    n = int(input('Digite um valor : '))
    r = str(input('Quer continuar ? [S/N]')).upper()
print('FIM')


p = 0
i =0
n = 1
while n != 0:
    n = int(input('Digite um valor : '))
    if n % 2 == 0:
        p = p + 1
    else :
        i = i + 1

print('Obtivemos {} numeros pares' .format(p)) 
print('Obtivemos {} numeros impares ' .format(i))
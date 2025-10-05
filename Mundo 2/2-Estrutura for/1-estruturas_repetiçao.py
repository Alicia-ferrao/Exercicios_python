i = int(input("Início : "))
f = int(input('Fim : '))
p = int(input('Passo : '))


for c in range(i, f , p):
    print(c)
print("Fim")

s= 0
for c in range(0,3):
    n = int(input('Digite um valor :'))
    s += n
print("O somatorio de todos os numeros é : {}" .format(s))
print('FIM')

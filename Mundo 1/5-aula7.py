# nome = input("Qual é o seu nome : ")
# print("Prazer em te conhecer {:=^20}!" .format(nome))

n1= int(input("Digite um valor : "))
n2 = int(input("Outro valor : "))
s= n1 + n2
m = n1 * n2
d = n1/n2
di = n1//n2
e = n1**2
r = n1%n2
print(" A soma é {},\n a divisão é {:.3f},\n a multiplicação é {}" .format(s, d, m), end="")
print("Divisão inteira {} ,\n potência {} ,\n resto da divisão {}" .format(di, e, r))

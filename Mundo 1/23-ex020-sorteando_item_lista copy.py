import math
import random


a1 = str(input("Primeiro aluno "))
a2 = str(input("Segundo aluno "))
a3 = str(input("Terceiro aluno "))
a4 = str(input("Quarto aluno "))
a5 = str(input("Quinto aluno "))

lista = [a1,a2,a3,a4, a5]
random.shuffle(lista)
print("A ordem de apresntação será : ")
print(lista)



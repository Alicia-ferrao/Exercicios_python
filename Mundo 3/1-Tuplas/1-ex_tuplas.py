lanche = ('Burger', 'Sumo', 'Pizza', 'Pudim')

# Tuplas são imutáveis
print(lanche)
print(lanche[-2:])


lanche = ('Burger', 'Sumo', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):
    print(f'Na posição {cont} eu tenho {lanche[cont]}')

# for comida in lanche :
#     print(f'Eu vou comer {comida}')
# print('Comi para caramba')

lanche = ('Burger', 'Sumo', 'Pizza', 'Pudim')
for pos, comida, in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi para caramba')

lanche = ('Burger', 'Sumo', 'Pizza', 'Pudim')
print(sorted(lanche))

a = (2,4,5)
b = (5,8,1,2)
c = a + b
print(len(c))
print(c.count(5))
print(c.index(8))








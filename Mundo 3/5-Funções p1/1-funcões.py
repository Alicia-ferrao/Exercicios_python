
def lin():    
    print('-' *30)


def titulo(msg):
       print('-' *30)
       print(msg)
       print('-' *30)

titulo('Curso em video')
titulo('Pyhton é muito bom')



# titulo('Aprenda Python')
# titulo('Alicia Silva')







# Programa Principal
# lin()
# lin()
titulo('Curso em video')
# lin()
# lin()

titulo('Aprenda Python')
# lin()
# lin()
titulo('Alicia Silva')
# lin()
# lin()


def somar(a,b):
    return a+b

print(somar(9,9))



def soma(a,b) :
     print(f' A = {a} e B = {b}')
     s = a +b
     print(f'A soma A + B = {s}')

soma(4, 5)

# empacontamento

def contador(*num):
     for valor in num :
          print(f'{valor}', end='')
     print('FIM')




def contador(*num):
     tam = len(num)
     print(f'Recebi os valores {num} e são ao todo {tam} numeros')
     

contador(2,5,3)
contador(8,0)
contador(4,4,7,6)

def dobre(lst):
     pos = 0
     while pos < len(lst):
          lst[pos] *= 2
          pos +=1
valores = [5,7,3,6,8,2]
dobre(valores)
print(valores)






def soma(*valores):
     s = 0
     for num in valores:
          s += num
     print(f'Somando os valores {valores} temos {s}')

     
soma(5,2)
soma(2,9,4)






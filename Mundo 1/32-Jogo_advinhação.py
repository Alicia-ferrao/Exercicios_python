from time import sleep

from random import randint

computador = randint(0,5) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5 . Tente advinhar ...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei ?'))
print('Processando...')
sleep(3)
if jogador == computador :
    print('Parabéns você conseguir me vencer !')
else:
    print('GANHEI! eu pensei no numero {} e não no {}' .format(computador,jogador))
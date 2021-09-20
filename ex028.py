# AULA 10 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
r = 's'
while r == 's':
    print('Vamos brincar! \nTente adivinhar o número de 0 a 5')
    n = int(input('Digite um número: '))
    num = randint(0, 5)
    if n != num:
        print('O número que você digitou é diferente! \nO número correto é {} '.format(num))
    else:
        print('PARABENS! Você acertou!')
    r = str(input('Deseja continuar? [S/N]')).lower().strip()
else:
    print('Foi um prazer brincar com você, até a proxima!')

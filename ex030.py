# AULA 10 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número qualquer: '))
num = n % 2
if num == 1:
    print('O número {} é ÍMPAR! '.format(n))
else:
    print('O número {} é PAR! '.format(n))

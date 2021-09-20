# AULA 10 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.
ra = float(input('Digite o valor da reta A: '))
rb = float(input('Digite o valor da reta B: '))
rc = float(input('Digite o valor da reta C: '))
if (ra+rb) > rc:
    print('O tamanho das retas formam um triângulo')
else:
    print('O tamanho das retas não formam um triângulo')

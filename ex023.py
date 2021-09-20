# AULA 9 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = str(input('Digite um número entre 0 a 9999: ')).strip()

print("""A unidade é = {}
A dezena é = {}
A centena é = {}
A milhar é = {}""".format(num[3], num[2], num[1], num[0]))

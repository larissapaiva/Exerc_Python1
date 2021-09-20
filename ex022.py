# AULA 9- Crie um programa que leia o nome completo de uma pessoa e mostre:
# A – O nome com todas as letras maiúsculas e minúsculas.
# B – Quantas letras ao todo (sem considerar espaços).
# C – Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome todo em maiusculo: {} \nSeu nome todo em minusculo: {}'.format(nome.upper(), nome.lower()))
print('Seu nome todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))

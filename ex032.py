# AULA 10 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite o ano para descobrir se é bissexto: '))

if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

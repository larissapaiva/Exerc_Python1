# AULA 7 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual o valor do produto? '))
print('O valor com desconto de 5% é de {} reais'.format(p-((5 / 100)*p)))

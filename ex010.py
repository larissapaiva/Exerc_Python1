# AULA 7 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode
# comprar //CONSIDERE O DÓLAR US$1.00 = R$3,27
r = float(input('Digite o valor em Real: '))
print('Esse valor em Real equivale a {:.2f} em dólar'.format(r / 3.27))

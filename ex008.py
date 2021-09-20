# AULA 7 - Escreva um programa que leia um valor em metros e o exiba convertidos em centímetros e milímetros
m = float(input('Digite o valor em metros: '))
print('{} metros equivalem a {:.0f} centímetros e {:.0f} milímetros'.format(m, m*100, m*1000))

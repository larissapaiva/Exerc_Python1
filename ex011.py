# AULA 7 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
b = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
A = b * h
print('Essa parede tem {}m², sendo necessário {}l de tinta '.format(A, (A/2)))

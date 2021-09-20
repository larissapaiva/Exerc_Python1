# AULA 8 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
# ângulo.
from math import radians, sin, cos, tan
a = float(input('Digite um Ângulo: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O SENO é: {:.2f}\nO COSSENO é {:.2f}\nA TANGENTE é {:.2f}'.format(sen, cos, tan))

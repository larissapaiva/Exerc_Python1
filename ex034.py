# AULA 10 -Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Digite seu salário: '))
if sal <= 1250:
    print('Seu salário é de {:.2f} e com aumento de 15% passa a ser R$ {:.2f}'. format(sal, sal + ((15 / 100) * sal)))
else:
    print('Seu salário é de {:.2f} e com aumento de 10% passa a ser R$ {:.2f}'.format(sal, sal + ((10 / 100) * sal)))

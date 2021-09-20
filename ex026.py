# AULA 9 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição
# ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite algo: ')).lower().strip()
print('A letra "a" aparece {} vezes nessa frase, a primeira vez é na posição'
      ' {} e a ultima vez na posição {}!'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))

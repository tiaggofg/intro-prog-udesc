"""
Escreva um programa que receba um número real (na chamada), encontre e mostre:

a) a parte inteira desse número;
b) a parte fracionária desse número;
c) o arredondamento desse número para uma casa decimal;
d) o arredondamento desse número para um número inteiro.
"""

import sys
from os import system, name

if name == 'nt':
    system('cls')
else:
    system('clear')

numero_real = float(sys.argv[1])

print(f'A parte inteira do número passado como parâmetro é {numero_real // 1}')
print(f'A parte fracionária do número passado como parâmetro é {numero_real % 1}')
print(f'O arrdondamento do número passado como parâmetro com 1 casa decimal é {round(numero_real, 1)}')
print(f'O arredondamento desse número para um número inteiro é {int(numero_real)}')
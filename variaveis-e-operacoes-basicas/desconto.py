"""
Escreva um programa que leia o preço de uma mercadoria e o percentual de desconto (na chamada).
Exiba o valor do desconto e o preço a pagar.
"""
import sys
from os import system, name

if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

preco_mercadoria = float(sys.argv[1])
desconto_percentual = float(sys.argv[2])

valor_desconto = preco_mercadoria * desconto_percentual
preco_total = preco_mercadoria - valor_desconto

print(f'Valor do desconto: $ {valor_desconto}\nValor a pagar: $ {preco_total}')
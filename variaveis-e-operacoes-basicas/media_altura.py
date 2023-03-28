"""
Escreva um programa que receba (na execução) a altura de quatro pessoas e exiba em tela a média de
altura do grupo.
"""

print('Digite a altura de quatro pessoas (em metros)', end='\n')

try:
    altura_pessoa_1 = float(input('Pessoa 1: '))
    altura_pessoa_2 = float(input('Pessoa 2: '))
    altura_pessoa_3 = float(input('Pessoa 3: '))
    altura_pessoa_4 = float(input('Pessoa 4: '))
except ValueError:
    print('A execução do programa foi interrompida devido ter sido preenchido um valor inválido em uma das alturas!')
    exit()

altura_media = (altura_pessoa_1 + altura_pessoa_2 + altura_pessoa_3 + altura_pessoa_4) / 4

print(f'\nA média da altura das 4 pessoas é: {altura_media} m.')
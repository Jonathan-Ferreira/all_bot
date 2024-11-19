import random
import re

def dado(vlr):
    i = 1
    total = 0
    lista = []
    qtd, dado = parte_string(vlr)
    while i <= qtd:
        resultado = random.randint(1,dado)  
        total += resultado
        lista.append(resultado)       
        # print('Iteração nro: ', i , 'Resultado: ', resultado, 'Tipo de Dado: ', dado, 'Total: ', total) 
        i += 1

    print(total, '<-', lista,vlr)
    # print(f'{0} -> ',vlr,total)
    # print(random.randint(1,6))f

def parte_string(input_string):
    match = re.match(r"(\d+)([a-zA-Z])(\d+)", input_string)
    if match:
        parte1 = int(match.group(1))  # Nro antes de 'd'
        parte2 = int(match.group(3))  # Nro depois de 'd'
        return parte1, parte2
    else:
        raise ValueError("Formato Errado")

roll = input('Digite a qtd e o tipo de dado que quiser rolar: ')

dado(roll)

import random
import re

def concatena(lista):
    try:
        # Junta os elementos e converte para string
        return int("".join(lista))
    except ValueError:
        # Except para valores inválidos
        return "Erro: lista contém valores inválidos."

def tipo_rolagem(comando):
    tp_rolagem, qtd_dados, tp_dados = parte_string(comando)
    match tp_rolagem:
        case "!":
            print(rolagem_comum(comando, qtd_dados, tp_dados))
        case _:
            print('Ainda não Implementado')
    #     case "2":
    #         print(22)
    #     case "3":
    #         print(33)    
    #     case "4":
    #         print(44)!
    #     case "5":
    #         print(55)
    #     case "6":
    #         print(66)

# Função para partir o comando em quantidade de dados, tipo de dados e tipo de rolagem
def parte_string(input_string):    
    tp_rolagem = input_string[0]
    lista_qtd_dado = []
    lista_tp_dado = []

    for i in range(1,len(input_string)):    
        if input_string[i].lower() == "d":
            break
        lista_qtd_dado.append(input_string[i].lower())

    for i in range(1,len(input_string)):    
        if input_string[i].lower() == "d":
            vlr = i

    for i in range(vlr+1, len(input_string)):
        lista_tp_dado.append(input_string[i])
    
    # Função de concatenar para obter os valores reais de quantidade e tipo de dado
    qtd_dado = concatena(lista_qtd_dado)
    tp_dado = concatena(lista_tp_dado)

    return tp_rolagem, qtd_dado, tp_dado

def rolagem_comum(comando, qtd_dados, tipo_dados):
    i = 1
    total = 0
    lista = []
    try:
        # Passando pra int
        qtd_dados = int(qtd_dados)
        tipo_dados = int(tipo_dados)
        while i <= qtd_dados:
            resultado = random.randint(1,tipo_dados)  
            total += resultado
            lista.append(resultado)       
            # print('Iteração nro: ', i , 'Resultado: ', resultado, 'Tipo de Dado: ', dado, 'Total: ', total) 
            i += 1
        # Return the result instead of printing it
        return f"{total} <- {lista} {comando}"
    except ValueError:
        # Handle cases where conversion to integer fails
        return "Erro: Valores Inválidos."
    except TypeError:
        # Handle any unexpected TypeError
        return "Erro: Valores Inválidos."
    except Exception as e:
        # Handle other unexpected exceptions
        return f"Erro inesperado: {e}"

cmd = ''

while cmd != "Sair":
    cmd = input('Digite a qtd e o tipo de dado que quiser rolar: ')
    tipo_rolagem(cmd)


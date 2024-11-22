import random

def concatena(lista):
    try:
        # Junta os elementos e converte para string
        return int("".join(lista))
    except ValueError:
        # Except para valores inválidos
        return "Erro: lista contém valores inválidos."

def tipo_rolagem(comando):
    tp_rolagem, qtd_dados, tp_dados = parte_string(comando)
    resultado = ''
    match tp_rolagem:
        case "@":
            resultado = rolagem_comum(comando[1:], qtd_dados, tp_dados)
        case _:
            resultado = 'Ainda não Implementado'
    return resultado

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
        # Conversão para int para captar possíveis erros no comando
        qtd_dados = int(qtd_dados)
        tipo_dados = int(tipo_dados)
        while i <= qtd_dados:
            resultado = random.randint(1,tipo_dados)  
            total += resultado
            lista.append(resultado)       
            i += 1            
        return f"{total} <- {lista} {comando}"
    
    except ValueError:
        # Caso a conversão falhe
        return "Erro: Valores Inválidos."
    except TypeError:
        # Outros erros de Tipo que podem ocorrer
        return "Erro: Valores Inválidos."
    except Exception as e:
        # Tratativa para erros gerais
        return f"Erro inesperado: {e}"


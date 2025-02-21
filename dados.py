import random

def concatena(lista):
    try:
        if lista == 'f':
            return 'f'
        # Junta os elementos e converte para string
        return int("".join(lista))
    except ValueError:
        # Except para valores inválidos
        return "Erro: lista contém valores inválidos."

# Método para definir qual tipo de rolagem fazer
def tipo_rolagem(comando):
    if comando == "status":
        resultado = rolagem_status()
    elif comando == "destino":
        resultado = rolagem_destino(comando[1:])
    else:
        tp_rolagem, qtd_dados, tp_dados = parte_string(comando)
        resultado = ''
        match tp_rolagem:
            case "@":
                resultado = rolagem_comum(comando[1:], qtd_dados, tp_dados)
            case "#":
                resultado = rolagem_explosiva(comando[1:], qtd_dados, tp_dados)
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
            vlr = i
            break
        lista_qtd_dado.append(input_string[i].lower())

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
    
def rolagem_explosiva(comando, qtd_dados, tipo_dados):
    i = 1
    total = 0
    qtd_total_dados = 0
    lista = []
    try:
        # Conversão para int para captar possíveis erros no comando
        qtd_dados = int(qtd_dados)
        tipo_dados = int(tipo_dados)
        while i <= qtd_dados:
            resultado = random.randint(1,tipo_dados)  
            while resultado == tipo_dados:                
                total += resultado
                lista.append(resultado)
                qtd_total_dados += 1
                resultado = random.randint(1,tipo_dados)  
            total += resultado
            lista.append(resultado) 
            qtd_total_dados += 1      
            i += 1            
        return f"{total} <- {comando} {lista} | Total de dados: {qtd_total_dados}"
    
    except ValueError:
        # Caso a conversão falhe
        return "Erro: Valores Inválidos."
    except TypeError:
        # Outros erros de Tipo que podem ocorrer
        return "Erro: Valores Inválidos."
    except Exception as e:
        # Tratativa para erros gerais
        return f"Erro inesperado: {e}"
    
def rolagem_destino():
    i = 1
    total = 0
    lista = []
    try:
        while i <= 4:
            resultado = random.randint(1,3)-2  
            total += resultado
            lista.append(resultado)       
            i += 1            
        return f"{total} <- {lista} "
    
    except ValueError:
        # Caso a conversão falhe
        return "Erro: Valores Inválidos."
    except TypeError:
        # Outros erros de Tipo que podem ocorrer
        return "Erro: Valores Inválidos."
    except Exception as e:
        # Tratativa para erros gerais
        return f"Erro inesperado: {e}"
   
def rolagem_status():
    resultados = []
    try:
        for _ in range(6):
            rolagens = [random.randint(1, 6) for _ in range(4)]
            menor = min(rolagens)
            total = sum(rolagens) - menor  # Soma sem o menor valor
            resultados.append(f"{total} <- {rolagens} (removendo {menor})")    
    except ValueError:
        # Caso a conversão falhe
        return "Erro: Valores Inválidos."
    except TypeError:
        # Outros erros de Tipo que podem ocorrer
        return "Erro: Valores Inválidos."
    except Exception as e:
        # Tratativa para erros gerais
        return f"Erro inesperado: {e}"
    
    return "\n".join(resultados)
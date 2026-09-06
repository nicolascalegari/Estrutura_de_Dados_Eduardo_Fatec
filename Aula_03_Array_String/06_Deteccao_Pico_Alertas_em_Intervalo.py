# Exercício 06: Detecção de Pico de Alertas em Intervalo Fixo (Janela Deslizante)

# Em um servidor, os registros de log são representados por uma 
# string logs, onde 'A' representa um alerta e 'N' representa tráfego normal. 
# Implemente a função maximo_alertas_janela(logs, k) que encontre o número 
# máximo de alertas 'A' presentes em qualquer intervalo contíguo de tamanho k .

# Exemplos:

#     Entrada: logs = "NNANAAANNN", k = 4 ⟶ Saída: 3 (trecho "ANAA")
#     Entrada: logs = "NNNN", k = 2 ⟶ Saída: 0

def maximo_alertas_janela(logs: str, k: int) -> int:

    if not logs or k <= 0 or k > len(logs):
        return 0

    # Conta alertas na primeira janela k
    alertas_atuais = logs[:k].count('A')
    max_alertas = alertas_atuais

    # Janela Deslizante
    for i in range(k, len(logs)):

        # Se char saindo esquerda for A, decrementa
        if logs[i - k] == 'A':
            alertas_atuais -= 1

        # Se char entrando direita dor A, incrementa
        if logs[i] == 'A':
            alertas_atuais += 1

        # Atualiza o max encontrado
        if alertas_atuais > max_alertas:
            max_alertas = alertas_atuais

    return max_alertas

# Tempo = O(N)
# Espaço = O(1)
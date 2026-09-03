# Exercício 08: Relatório de Faturamento por Intervalo (Prefix Sum)

# Um sistema financeiro armazena os balanços diários na lista balancos. 
# Implemente a classe ConsultaFaturamento que receba a lista no construtor 
# e disponibilize o método somar_periodo(inicio, fim) para retornar a soma 
# dos balanços do dia inicio até o dia fim inclusive em tempo O ( 1 ) por consulta.

# Exemplo:

# cf = ConsultaFaturamento([10, -5, 20, 15, -10])
# print(cf.somar_periodo(0, 2))  # 10 + (-5) + 20 = 25
# print(cf.somar_periodo(1, 3))  # -5 + 20 + 15 = 30

class ConsultaFaturamento:
    def __init__(self, balancos: list[int]):
        # Cria uma lista de somas acumuladas (Prefix Sum)
        # O elemento extra 0 no início facilita o cálculo de intervalos que 
        # começam no índice 0
        self.prefix_sum = [0] * (len(balancos) + 1)

        # Preenche a lista com as somas acumuladas
        for i in range(len(balancos)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + balancos[i]
        
    def somar_periodo(self, inicio: int, fim: int) -> int:
        # A soma do intervalo [inicio, fim] é calculada subtraindo os prefixos correspondentes
        return self.prefix_sum[fim + 1] - self.self.prefix_sum[inicio]

# Tempo = O(N)
# Espaço = O(N)
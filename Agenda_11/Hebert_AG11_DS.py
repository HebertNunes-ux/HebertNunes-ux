from colorama import Fore, Style, init

# Inicializa o colorama para o terminal
init(autoreset=True)

# 1. Lista armazenando os níveis e as respetivas situações
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
]

# 2. Função responsável por exibir a situação com a cor correta
def monitorar_reservatorio(dados_nivel):
    print(
        dados_nivel["cor"]
        + f"Nível {dados_nivel['nivel']}: {dados_nivel['situacao']}"
    )

# 3. Simulação do sistema percorrendo os níveis
print("--- SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ---")
for item in niveis_reservatorio:
    monitorar_reservatorio(item)

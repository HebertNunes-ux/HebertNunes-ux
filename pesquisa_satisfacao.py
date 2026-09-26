# Inicialização dos contadores
excelente = 0
ruim = 0

# Teste com 10 entrevistados conforme instrução de teste
TOTAL_ENTREVISTADOS = 10

print("--- PESQUISA DE SATISFAÇÃO - TUDOWEB ---")

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\nEntrevistado {i}:")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE | 2 - BOM | 3 - RUIM")
    opiniao = int(input("Sua opção (1, 2 ou 3): "))
    
    # Estrutura de decisão para contagem
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

# Exibição dos resultados finais
print("\n" + "="*30)
print("RESULTADO DA PESQUISA")
print("="*30)
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
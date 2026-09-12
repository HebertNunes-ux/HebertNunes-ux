# ==============================================================================
# Sistema de Desconto Progressivo - Loja Online
# Disciplina: Desenvolvimento de Sistemas I - Agenda 06
# ==============================================================================

# Entrada de dados: solicita o valor total da compra ao usuário
valor_compra = float(input("Digite o valor total da compra (R$): "))

# Estrutura de decisão (condicionais) para definir a taxa de desconto
if valor_compra < 200.00:
    percentual_desconto = 0.05  # 5% de desconto para compras abaixo de R$ 200,00
elif valor_compra < 300.00:
    percentual_desconto = 0.10  # 10% de desconto para compras entre R$ 200,00 e R$ 299,99
else:
    percentual_desconto = 0.15  # 15% de desconto para compras a partir de R$ 300,00

# Processamento: cálculos do valor economizado e do valor final a pagar
valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto

# Saída de dados: exibição dos resultados formatados com 2 casas decimais
print("\n--- RESUMO DA COMPRA ---")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {int(percentual_desconto * 100)}% (R$ {valor_desconto:.2f})")
print(f"Valor total a pagar: R$ {valor_final:.2f}")
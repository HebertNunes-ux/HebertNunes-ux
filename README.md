# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

## 📌 Sobre o Projeto
A **Calculadora de Consumo Elétrico** é uma ferramenta simples em Python desenvolvida para ajudar os usuários a estimar o consumo mensal de energia elétrica de seus eletrodomésticos, além de calcular uma estimativa do custo na fatura final.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **IDE recomendada:** VS Code
- **Versionamento:** Git & GitHub

## 📐 Fórmula de Cálculo
O programa utiliza a seguinte fórmula matemática para encontrar o consumo mensal em quilowatts-hora ($kWh$):

$$consumoMensal = \frac{potencia \times horasDia \times 30}{1000}$$

*Onde:*
- `potencia`: Potência do aparelho em Watts ($W$).
- `horasDia`: Tempo médio de uso diário em horas.
- `30`: Quantidade de dias no mês.

---

## 🚀 Como Executar o Programa

### Pré-requisitos
Ter o [Python 3](https://www.python.org/) instalado em seu computador.

### Passos
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/consumo-energia.git](https://github.com/seu-usuario/consumo-energia.git)
Navegue até a pasta do projeto:

Bash
cd projetos/consumo-energia
Execute o script em Python:

Bash
python app.py
💻 Exemplo de Uso
Plaintext
Digite o nome do aparelho (ex.: Geladeira): Geladeira
Digite a potência do aparelho em watts (W): 150
Digite o tempo médio de uso diário em horas: 10

--- Resultado do Consumo Elétrico ---
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo mensal estimado: R$ 33.75
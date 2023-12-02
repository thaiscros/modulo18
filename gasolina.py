import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha
sns.set(style='whitegrid')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')

# rótulos
plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço')

# Salvar o gráfico
plt.savefig('gasolina.png')

plt.show()

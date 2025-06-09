import pandas as pd

# Exemplo de DataFrame
df = pd.DataFrame({'salario': [2000, 2500, 3000, 100000, 2800]})

print("Média:", df['salario'].mean())      # A média é afetada por outliers
print("Mediana:", df['salario'].median())  # Melhor em dados distorcidos
print("Moda:", df['salario'].mode()[0])
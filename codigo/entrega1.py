import pandas as pd

c = "calles_de_medellin_con_acoso.csv"
df = pd.read_csv(c, sep=";")
rellenar = df.fillna({"harassmentRisk":df['harassmentRisk'].mean()})

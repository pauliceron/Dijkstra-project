import pandas as pd

file = "calles_de_medellin_con_acoso.csv"
df = pd.read_csv(file, sep=";")
average = df["harassmentRisk"].mean()
fill = df.fillna({"harassmentRisk": average})
graph = {}

for line in fill.index:
    if fill["oneway"][line]:
        graph[fill["origin"][line]] = [fill["destination"][line], fill["harassmentRisk"][line], fill["length"][line]]
    else:
        graph[fill["origin"][line]] = [fill["destination"][line], fill["harassmentRisk"][line], fill["length"][line]]
        graph[fill["destination"][line]] = [fill["origin"][line], fill["harassmentRisk"][line], fill["length"][line]]

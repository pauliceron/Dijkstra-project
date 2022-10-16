import pandas as pd

df = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=';')
fill = df.fillna({"harassmentRisk": df['harassmentRisk'].mean()})
g = {}
for l in fill.index:
    value = ((fill["harassmentRisk"][l] + fill["length"][l]) / 2, fill["geometry"][l])
    origin = fill["origin"][l]
    destination = fill["destination"][l]
    if origin not in g:
        g[origin] = {destination: value}
    else:
        g[origin][destination] = value
    if fill["oneway"][l]:
        if destination not in g:
            g[destination] = {origin: value}
        else:
            g[destination][origin] = value


def dijkstra(start, goal):
    dist = {}
    pre = {}
    unseen = g
    path = []
    inf = 99999999999999999
    for l in unseen:
        dist[l] = inf
    dist[start] = 0
    while unseen:
        before = None
        for o in unseen:
            if before is None or dist[o] < dist[before]:
                before = o
        options = g[before].items()
        for child, weight in options:
            if weight[0] + dist[before] < dist[child]:
                dist[child] = weight[0] + dist[before]
                pre[child] = before
        unseen.pop(before)
    current = goal
    while current is not start:
        try:
            path.insert(0, current)
            current = pre[current]
        except KeyError:
            break
    path.insert(0, start)
    if dist[goal] is not inf:
        print("Shortest distance and harassment is", dist[goal])
        print("Optimal path is", path)
    else:
        print("Path is not reachable")


dijkstra("(-75.5728593, 6.2115169)", "(-75.5705604, 6.2105262)")

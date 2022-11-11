class general:

    def grafo(df, i):
        g = {}
        for l in df.index:
            valor = ((df["harassmentRisk"][l] + df["length"][l]) / 2, df["length"][l], df["harassmentRisk"][l])
            origen = df["origin"][l]
            destino = df["destination"][l]
            if origen not in g:
                g[origen] = {destino: valor[i]}
            else:
                g[origen][destino] = valor[i]
            if df["oneway"][l]:
                if destino not in g:
                    g[destino] = {origen: valor[i]}
                else:
                    g[destino][origen] = valor[i]
        return g

    def dijkstra(grafo, inicio, meta):
        rutaCorta = {}
        rutaRecorrida = {}
        noVisitados = grafo
        inf = 9999999
        ruta = []

        for lugar in noVisitados:
            rutaCorta[lugar] = inf
        rutaCorta[inicio] = 0

        while noVisitados:
            distMin = None
            for lugar in noVisitados:
                if distMin is None:
                    distMin = lugar
                elif rutaCorta[lugar] < rutaCorta[distMin]:
                    distMin = lugar
            opcionesRutas = grafo[distMin].items()

            for actual, indice in opcionesRutas:
                if indice + rutaCorta[distMin] < rutaCorta[actual]:
                    rutaCorta[actual] = indice + rutaCorta[distMin]
                    rutaRecorrida[actual] = distMin
            noVisitados.pop(distMin)

        lugarActual = meta
        while lugarActual != inicio:
            try:
                ruta.insert(0, lugarActual)
                lugarActual = rutaRecorrida[lugarActual]
            except KeyError:
                print("La ruta no es valida :(")
                break
        ruta.insert(0, inicio)
        if rutaCorta[meta] != inf:
            print("La ruta tiene", rutaCorta[meta], "metros")
            return ruta

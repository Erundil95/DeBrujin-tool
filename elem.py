class Vertice:
    # Vertice del grafo
    def __init__(self, l):
        self.label = l
        self.in_archi = 0
        self.out_archi = 0

class Arco:
    #Arco del grafo
    def __init__(self, e):
        self.etichetta = e

class Grafo:
    #composto grafo
    def __init__(self, v, e):
        self.vertices = v
        self.edges = e


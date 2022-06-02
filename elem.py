class Vertice:
    # Vertice del grafo
    def __init__(self, label):
        self.label = label
    
    def __hash__(self):
        return hash(self.label)

class Grafo:
    #composto grafo
    def __init__(self, v, e):
        self.vertices = v
        self.edges = e


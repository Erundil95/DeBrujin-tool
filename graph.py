import graph

class DB_Graph:

    class Vertice:
    # Vertice del grafo
        def __init__(self, label):
            self.label = label         #kmer label
            self.in_degree = 0
            self.out_degree = 0
            
        def isBalanced(self):
            if(self.in_degree - self.out_degree) == 1:
                return True
            return False
        
        def isSemiBalanced(self):
            if(self.in_degree == self.out_degree):
                return True
            return False           
        def __hash__(self):
            return hash(self.label)


    def __init__(self, kmers, k):    #TODO: is this even needed?
        self.archi = {}      
        self.vertici = {}         

        for kmer in kmers:
            kmer_L, kmer_R = kmer[:-1], kmer[1:]                         #divido in k-1 mers
            vertice_L, vertice_R = None, None
            if kmer_L in self.vertici:                                        #per evitare vertici duplicati ne si controllo l'esistenza
                vertice_L = self.vertici[kmer_L]
            else:
                vertice_L = self.vertici[kmer_L] = graph.Vertice(kmer_L)      #maybe dumb this one down into two commands

            if kmer_R in self.vertici:          
                vertice_R = self.vertici[kmer_R]
            else:
                vertice_R = self.vertici[kmer_R] = graph.Vertice(kmer_R)
            self.archi.setdefault(kmer_L, []).append(kmer_R)                  #creazione arco tra i due k-1 mer

    def eulerianVisit(self):
        """Return eulerian path of graph"""
        #assert self.isEulerian()                #TODO: idk if this check is too much 
        a = self.archi
        











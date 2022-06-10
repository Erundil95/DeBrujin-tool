class DeBruijnGraph:

    class Vertice:
    # Vertice del grafo
        def __init__(self, label):
            self.label = label         #kmer label
            self.in_degree = 0         #num arco entranti e uscenti
            self.out_degree = 0
            
        def isSemiBalanced(self):
            if(abs(self.in_degree - self.out_degree)) == 1:
                return True
            return False
        
        def isBalanced(self):
            if(self.in_degree == self.out_degree):
                return True
            return False    
               
        def __hash__(self):
            return hash(self.label)

        def __str__(self):
            return self.label


    def __init__(self, kmers): 
        self.archi = {}                    #multi-mappa nodo-list(nodo)     
        self.vertici = {}                  #mappa dei nodi
        self.archi_og = {}
        self.head, self.tail = None, None        

        for kmers in kmers:
            kmer_L, kmer_R = kmers[:-1], kmers[1:]                #divido in k-1 mers
            vertice_L, vertice_R = None, None
            if kmer_L in self.vertici:                                   #per evitare vertici duplicati ne si controllo l'esistenza
                vertice_L = self.vertici[kmer_L]
            else:
                vertice_L = self.vertici[kmer_L] = self.Vertice(kmer_L)    

            if kmer_R in self.vertici:          
                vertice_R = self.vertici[kmer_R]
            else:
                vertice_R = self.vertici[kmer_R] = self.Vertice(kmer_R)

            if not (self.isDupe(vertice_L, vertice_R)):
                vertice_L.out_degree += 1
                vertice_R.in_degree += 1
            
            self.archi.setdefault(vertice_L, []).append(vertice_R)

        self.archi_og = self.archi.copy()         #Salvo mappa archi originale per disegno
        c = 1
        for node in iter(self.archi.keys()):
            l = self.archi[node]
            c += 1
            dup = list(dict.fromkeys(l))
            self.archi.update({node : dup})

        self.balanceCount()

    def isDupe(self, verticeL, verticeR):
        edges = self.archi.get(verticeL, [])
        flag = False
        for elem in edges:
            if elem == verticeR:
                flag = True
        return flag      
 
    def balanceCount(self):
        self.num_semi = 0
        self.num_bal = 0
        self.num_notBal = 0

        for vertice in self.vertici.values():
            if vertice.isBalanced():
                self.num_bal += 1
            elif vertice.isSemiBalanced():
                if vertice.in_degree == vertice.out_degree + 1:
                    self.tail = vertice
                if vertice.in_degree == vertice.out_degree - 1:
                    self.head = vertice
                self.num_semi += 1
            else:
                self.num_notBal += 1


    def eulerianPath(self):
        assert self.isEulerian()          #ADD EXCEPTION MAYBE TO EXPLAIN ERROR
        if self.hasEulerianPath():
            assert self.head is not None
            assert self.tail is not None
            self.archi.setdefault(self.tail, []).append(self.head)   #aggiungo ciclo euleriano per avere l'ultimo nodo nel cammino
        result = []
        src = iter(self.archi.keys()).__next__()
        def visita(n):
            while len(self.archi[n]) > 0:
                dst = self.archi[n].pop()     #visita ricorsiva per ogni arco
                visita(dst)
            result.append(n)
        visita(src)
        result = result[::-1][:-1]
            
        if self.hasEulerianPath():
            sti = result.index(self.head)
            result = result[sti:] + result[:sti]
        return list(map(str, result))
        
        
    def isEulerian(self):
        return self.isBalanced() or self.isSemiBalanced()

    def isSemiBalanced(self):
        return self.num_notBal == 0 and self.num_semi == 2

    def isBalanced(self):
        return self.num_notBal == 0 and self.num_semi == 0

    def hasEulerianPath(self):
        """ Return true iff graph has Eulerian path. """
        return self.num_notBal == 0 and self.num_semi == 2
    
    def hasEulerianCycle(self):
        """ Return true iff graph has Eulerian cycle. """
        return self.num_notBal == 0 and self.num_semi == 0

    def printGraph(self, output, weights=False):
        """ Write graph in dot represantion so that it
            might be dsiplayed using graphviz"""
        output.write("digraph \"DeBruijn Graph\" {\n")
        output.write("  bgcolor=\"white\";\n")
        for src, dsts in iter(self.archi_og.items()):
            # print(dsts)
            srclab = src.label
            weightmap = {}
            for dst in dsts:
                weightmap[dst] = weightmap.get(dst, 0) + 1
            for dst, v in iter(weightmap.items()):
                dstlab = dst.label
                output.write("  %s -> %s [label=\"%d\"] ;\n" % (srclab, dstlab, v))
        output.write("}\n")











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
        self.head, self.tail = None, None        

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
        self.balanceCount()
 
    def balanceCount(self):
        self.num_semi = 0
        self.num_bal = 0
        self.num_notBal = 0

        for vertice in self.archi.values():
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


    def eulerianVisit(self):
        """Return eulerian path of graph"""
        #assert self.isEulerian()                #TODO: idk if this check is too much 
        a = self.archi

        tour = []
        source = self.head
        print("SOURCE: " + source)

        def visit(x):
            

        
    def isEulerian(self):
        return self.isBalanced() or self.isSemiBalanced()

    def isSemiBalanced(self):
        return self.num_notBal == 0 and self.num_semi == 2

    def isBalanced(self):
        return self.num_notBal == 0 and self.num_semi == 0

    def toDot(self, dotFh, weights=False):
        """ Write dot representation to given filehandle.  If 'weights'
            is true, label edges corresponding to distinct k-1-mers
            with weights, instead of writing a separate edge for each
            copy of a k-1-mer. """
        dotFh.write("digraph \"Graph\" {\n")
        dotFh.write("  bgcolor=\"transparent\";\n")
        for node in iter(self.G.keys()):
            lab = node.km1mer
            dotFh.write("  %s [label=\"%s\"] ;\n" % (lab, lab))
        for src, dsts in iter(self.G.items()):
            # print(dsts)
            srclab = src.km1mer
            if weights:
                weightmap = {}
                if weights:
                    for dst in dsts:
                        weightmap[dst] = weightmap.get(dst, 0) + 1
                for dst, v in iter(weightmap.items()):
                    dstlab = dst.km1mer
                    dotFh.write("  %s -> %s [label=\"%d\"] ;\n" % (srclab, dstlab, v))
            else:
                for dst in dsts:
                    srclab = src.km1mer
                    dstlab = dst.km1mer
                    dotFh.write("  %s -> %s [label=\"\"] ;\n" % (srclab, dstlab))
        dotFh.write("}\n")











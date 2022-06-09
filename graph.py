import graph

class DeBruijnGraph:

    class Vertice:
    # Vertice del grafo
        def __init__(self, label):
            self.label = label         #kmer label
            self.in_degree = 0
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

    class Arco:

        def __init__(self, to_node):
            # self.from_node = from_node
            self.to_node = to_node
            self.weight = 0


    def __init__(self, kmers):    #TODO: is this even needed?
        self.archi = {}      
        self.vertici = {} 
        self.head, self.tail = None, None        

        for kmers in kmers:
            kmer_L, kmer_R = kmers[:-1], kmers[1:]                         #divido in k-1 mers
            vertice_L, vertice_R = None, None
            if kmer_L in self.vertici:                                        #per evitare vertici duplicati ne si controllo l'esistenza
                vertice_L = self.vertici[kmer_L]
            else:
                vertice_L = self.vertici[kmer_L] = self.Vertice(kmer_L)      #maybe dumb this one down into two commands

            if kmer_R in self.vertici:          
                vertice_R = self.vertici[kmer_R]
            else:
                vertice_R = self.vertici[kmer_R] = self.Vertice(kmer_R)

            vertice_L.out_degree += 1
            vertice_R.in_degree += 1
            # print("vertice_L: " + vertice_L.label + " in: " + str(vertice_L.in_degree) + " out: " + str(vertice_L.out_degree))
            # print("vertice_R: " + vertice_R.label + " in: " + str(vertice_R.in_degree) + " out: " + str(vertice_R.out_degree))
            # print(self.archi.setdefault(vertice_L, []))
            self.archi.setdefault(vertice_L, []).append(vertice_R)  

            
        self.balanceCount()
 
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
        """ Find and return Eulerian path or cycle (as appropriate) """
        assert self.isEulerian()
        g = self.archi
        if self.hasEulerianPath():
            g = g.copy()
            assert self.head is not None
            assert self.tail is not None
            g.setdefault(self.tail, []).append(self.head)
        # graph g has an Eulerian cycle
        tour = []
        src = iter(g.keys()).__next__()
        # print(g)
        def __visit(n):
            while len(g[n]) > 0:
                dst = g[n].pop()
                # print(dst)
                __visit(dst)
            tour.append(n)
        
        __visit(src)
        tour = tour[::-1][:-1]
            
        if self.hasEulerianPath():
            # Adjust node list so that it starts at head and ends at tail
            sti = tour.index(self.head)
            tour = tour[sti:] + tour[:sti]
            print(tour)
        
        # Return node list
        return map(str, tour)
            

        
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

    def toDot(self, dotFh, weights=False):
        """ Write dot representation to given filehandle.  If 'weights'
            is true, label edges corresponding to distinct k-1-mers
            with weights, instead of writing a separate edge for each
            copy of a k-1-mer. """
        dotFh.write("digraph \"Graph\" {\n")
        dotFh.write("  bgcolor=\"transparent\";\n")
        # for node in iter(self.archi.keys()):
        #     lab = node.label
        #     dotFh.write("  %s [label=\"%s\"] ;\n" % (lab, lab))
        for src, dsts in iter(self.archi.items()):
            # print(dsts)
            srclab = src.label
            if weights:
                weightmap = {}
                if weights:
                    for dst in dsts:
                        weightmap[dst] = weightmap.get(dst, 0) + 1
                for dst, v in iter(weightmap.items()):
                    dstlab = dst.label
                    dotFh.write("  %s -> %s [label=\"%d\"] ;\n" % (srclab, dstlab, v))
            else:
                for dst in dsts:
                    srclab = src.label
                    dstlab = dst.label
                    dotFh.write("  %s -> %s [label=\"\"] ;\n" % (srclab, dstlab))
        dotFh.write("}\n")











from Bio import SeqIO
import elem

def read_input(path):
    reads = []
    # path = Path(__file__) / "../fa-test.fa"        
    with path.open() as f:
        for record in SeqIO.parse(f, 'fasta'):
            reads.append(str(record.seq))

    return reads

def create_db_graph(reads, k):

    archi = dict()
    vertici = dict()

    for read in reads:
        i = 0
        while i+k < len(read):     # Caso in cui la read é < lunga di K?
            r1 = read[i: i+k]
            r2 = read[i+1 : i+k+1]
            if r1 in archi.keys():
                vertici[r1].out_archi += 1
                archi[r1] += [elem.Arco(r2)]
            else:
                vertici[r1] = elem.Vertice(r1)
                vertici[r1].out_archi += 1     #might wanna move this one out of the if 
                archi[r1] = [elem.Arco(r2)]
            
            if r2 in archi.keys():
                vertici[r2].in_archi += 1
            else:
                vertici[r2] = elem.Vertice(r2)
                vertici[r2].in_archi += 1
                archi[r2] = []
            i += 1  
    return (vertici, archi)

def output_contigs(g):
    """ Perform searching for Eulerian path in the graph to output genome assembly"""
    V = g[0]
    E = g[1]
    # Pick starting node (the vertex with zero in degree)
    start = list(V.keys())
    for k in V.keys():
        if V[k].in_archi < V[start].in_archi:
            start = k

    contig = start
    current = start
    while len(E[current]) > 0:
        # Pick the next node to be traversed (for now, at random)
        next = E[current][0]
        del E[current][0]
        contig += next.label[-1]
        current = next.label

    return contig  
    
def print_graph(g):
    """ Print the information in the graph to be (somewhat) presentable """
    V = g[0]
    E = g[1]
    for k in V.keys():
        print("name: ", V[k].label, ". in_archi: ", V[k].in_archi, ". out_archi: ", V[k].out_archi)
        print("Edges: ")
        for e in E[k]:
            print(e.label)
        print(" ")

    
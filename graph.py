from Bio import SeqIO
import elem
import sys

def read_input(path):
    """Relative read of fasta file within project"""
    reads = []
    # path = Path(__file__) / "../fa-test.fa"        
    with path.open() as f:
        for record in SeqIO.parse(f, 'fasta'):
            reads.append(str(record.seq))       #maybe add strip to avoid blank spaces
    return reads

def splice(read, k):
    """splice strings into k-mers"""
    kmer = []
    for elem in read:
        for i in range(0, len(elem) - (k - 1)):
            kmer.append(elem[i : i + k])
    return kmer

def create_db_graph(kmers, k):
    archi = {}      
    vertici = {}         

    for kmer in kmers:
        kmer_L, kmer_R = kmer[:-1], kmer[1:]                         #divido in k-1 mers
        vertice_L, vertice_R = None, None
        if kmer_L in vertici:                                        #per evitare vertici duplicati ne si controllo l'esistenza
            vertice_L = vertici[kmer_L]
        else:
            vertice_L = vertici[kmer_L] = elem.Vertice(kmer_L)      #maybe dumb this one down into two commands

        if kmer_R in vertici:          
            vertice_R = vertici[kmer_R]
        else:
            vertice_R = vertici[kmer_R] = elem.Vertice(kmer_R)
        archi.setdefault(kmer_L, []).append(kmer_R)                  #creazione arco tra i due k-1 mer
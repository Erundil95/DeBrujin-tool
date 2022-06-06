from Bio import SeqIO
import graph
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
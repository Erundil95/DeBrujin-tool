from asyncore import write
from sysconfig import get_path
from Bio import SeqIO
from Bio.Seq import Seq
from pathlib import Path
from graphviz import Digraph as dg

import utils
import graph

def assemble_reads(path, k): 
    kmer = utils.splice(utils.read_input(path), k)
    db = graph.DeBruijnGraph(kmer)

    handle = open('graph.gv', 'w')
    db.printGraph(handle)

    #Superstring assembly function
    kmer_list = db.eulerianPath()
    ss = kmer_list[0]
    i = 1
    while i < (len(kmer_list)):
        x = kmer_list[i]
        ss = ss + x[-1]
        i += 1

    #print superstringa finale
    output = open('output.txt', "w")
    output.write(ss)
    output.close()
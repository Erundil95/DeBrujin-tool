from Bio import SeqIO
from Bio.Seq import Seq
from pathlib import Path
import graph

path = Path(__file__) / "../fa-test.fa"   


kmer = graph.splice(graph.read_input(path), 4)
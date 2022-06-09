from Bio import SeqIO
from Bio.Seq import Seq
from pathlib import Path
import utils
import graphtest
import graph

path = Path(__file__) / "../fa-test.fa"   

read = utils.read_input(path)
# print(read)
kmer = utils.splice(utils.read_input(path), 3)
# print(kmer)
# print(kmer)
# print(list(dict.fromkeys(kmer)))


db = graph.DeBruijnGraph(kmer)
# db = graph.DeBruijnGraph(list(dict.fromkeys(kmer)))
# print(db.hasEulerianPath())
# print(db.eulerianPath())
# print(dir(iter(db.G)))

handle = open('graph.txt', 'w')
db.toDot(handle, weights=True)


#Superstring assembly function :TODO put in separate method (maybe fuse path method with this one directly)
kmer_list = list(db.eulerianPath())
ss = kmer_list[0]
i = 1
while i < (len(kmer_list)):
    x = kmer_list[i]
    ss = ss + x[-1]
    i += 1

print(ss)
 
#TODO: check duplicati maybe per le read multiple non funzionanti








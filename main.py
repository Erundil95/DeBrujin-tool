from Bio import SeqIO
from Bio.Seq import Seq
from pathlib import Path
import graph

path = Path(__file__) / "../fa-test.fa"        
read = graph.read_input(path)
g = graph.create_db_graph(read, 4)

# # print(graph.edges)
# # print(graph.vertices)

# for key, possible_values in graph.edges.items():
#     print(key, ' : ', possible_values)





# Main script
# g = construct_graph(test, 3)

# print_graph(g)
# for k in g.keys():
#   print k, g[k]
# g = construct_graph(reads)
contig = graph.output_contigs(g)
print(contig)
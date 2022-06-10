from pathlib import Path
import assembler

path = Path(__file__) / "../input.fa"   
assembler.assemble_reads(path, 5)








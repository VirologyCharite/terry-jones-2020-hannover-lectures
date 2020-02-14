from Bio import SeqIO
from Bio.SeqUtils import GC

for record in SeqIO.parse('wuhan.fasta', 'fasta'):
    if 'ACTAATTAC' in record.seq:
        print(record.id, GC(record.seq[:1000]))

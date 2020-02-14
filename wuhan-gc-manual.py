from Bio import SeqIO

for record in SeqIO.parse('wuhan.fasta', 'fasta'):
    if 'ACTAATTAC' in record.seq:
        subsequence = record.seq[0:100]
        gc = subsequence.count('G') + subsequence.count('C')
        print(record.id, 100.0 * gc / len(subsequence))

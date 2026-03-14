# biopython_intro.py
# Reading and analyzing FASTA files with Biopython

from Bio import SeqIO

print("=== Analyzing sequences.fasta ===")
print()

for record in SeqIO.parse("sequences.fasta", "fasta"):
    sequence = str(record.seq).upper()
    length = len(sequence)

    g = sequence.count("G")
    c = sequence.count("C")
    gc = round((g + c) / length * 100, 2)

    print(f"Gene: {record.id}")
    print(f"  Length: {length} bp")
    print(f"  GC Content: {gc}%")
    print(f"  First 30 bases: {sequence[:30]}")
    print()
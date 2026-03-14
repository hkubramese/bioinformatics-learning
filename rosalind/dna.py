# Rosalind: DNA Problem
# Open the dataset file and read it
with open("rosalind_dna.txt") as f:
    dna = f.read().strip()

# Count each nucleotide
a = dna.count("A")
c = dna.count("C")
g = dna.count("G")
t = dna.count("T")

# Print in required format: A C G T
print(a, c, g, t)
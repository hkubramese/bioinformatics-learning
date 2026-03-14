# Rosalind: RNA Problem
# Open the dataset file and read it
with open("rosalind_rna.txt") as f:
    dna = f.read().strip()

# Count each nucleotide
a = dna.count("A")
c = dna.count("C")
g = dna.count("G")
t = dna.count("T")

# Replace T with U
rna = dna.replace("T", "U")

# Print the result
print(rna)
# Rosalind Problem: REVC
# Find the reverse complement of a DNA string

with open("rosalind_revc.txt") as f:
    dna = f.read().strip()

# Step 1: complement each base
complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
comp_dna = ""
for base in dna:
    comp_dna += complement[base]

# Step 2: reverse the complement string
result = comp_dna[::-1]

print(result)
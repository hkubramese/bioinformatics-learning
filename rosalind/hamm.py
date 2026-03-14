# Rosalind: HAMM Problem
# Count the number of positions where two sequences differ

with open("rosalind_hamm.txt") as f:
    lines = f.readlines()

# Read the two sequences
dna1 = lines[0].strip()
dna2 = lines[1].strip()

# Count differences
count = 0
for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
        count += 1

print(count)
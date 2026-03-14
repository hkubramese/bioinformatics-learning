# Rosalind: GC Content Problem
# Find the sequence with highest GC content

with open("rosalind_gc.txt") as f:
    lines = f.readlines()

# Variables to track current sequence
best_name = ""
best_gc = 0.0
current_name = ""
current_seq = ""

for line in lines:
    line = line.strip()
    if line.startswith(">"):
        # New sequence starting - calculate previous one first
        if current_seq:
            g = current_seq.count("G")
            c = current_seq.count("C")
            gc = (g + c) / len(current_seq) * 100
            if gc > best_gc:
                best_gc = gc
                best_name = current_name
        # Start new sequence
        current_name = line[1:]
        current_seq = ""
    else:
        current_seq += line

# Don't forget the last sequence!
if current_seq:
    g = current_seq.count("G")
    c = current_seq.count("C")
    gc = (g + c) / len(current_seq) * 100
    if gc > best_gc:
        best_gc = gc
        best_name = current_name

print(best_name)
print(round(best_gc, 6))
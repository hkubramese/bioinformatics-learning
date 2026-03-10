# nucleotide_counter.py
# Analyzes a DNA sequence and returns nucleotide statistics

def analyze_dna(sequence):
    """
    Takes a DNA sequence string and prints nucleotide counts and GC content.
    """
    # Convert to uppercase so "a" and "A" are treated the same
    sequence = sequence.upper()
    total = len(sequence)

    count_A = sequence.count("A")
    count_T = sequence.count("T")
    count_G = sequence.count("G")
    count_C = sequence.count("C")
    gc_content = ((count_G + count_C) / total) * 100

    print(f"\nAnalyzing: {sequence[:20]}...")
    print(f"Length: {total} nucleotides")
    print(f"A: {count_A}  T: {count_T}  G: {count_G}  C: {count_C}")
    print(f"GC Content: {round(gc_content, 2)}%")

# Test with three different sequences
analyze_dna("ATGCTTGCAATGCGCTATGCGATCGATCGATCGATGCTA")
analyze_dna("GCGCGCGCGCGCGCGCGCGC")
analyze_dna("ATATATATATATATATAT")
def calculate_gc_content(dna):
    dna = dna.upper()

    if len(dna) == 0:
        return 0

    gc_count = dna.count("G") + dna.count("C")
    gc_percentage = (gc_count / len(dna)) * 100

    return gc_percentage


sequence = "ATGCGCATGC"

result = calculate_gc_content(sequence)

print("DNA sequence:", sequence)
print("GC content:", result, "%")
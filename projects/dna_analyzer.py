
# DNA Sequence Analyzer
# A beginner bioinformatics project

dna = input("Enter a DNA sequence: ").upper().strip()

valid_bases = {"A", "T", "G", "C"}

if not dna:
    print("Error: DNA sequence cannot be empty.")

elif not set(dna).issubset(valid_bases):
    print("Error: Invalid DNA sequence. Use only A, T, G, C.")

else:
    length = len(dna)

    a_count = dna.count("A")
    t_count = dna.count("T")
    g_count = dna.count("G")
    c_count = dna.count("C")

    gc_content = ((g_count + c_count) / length) * 100

    print("\n--- DNA Sequence Analysis ---")
    print("DNA Sequence:", dna)
    print("Sequence Length:", length)
    print("A count:", a_count)
    print("T count:", t_count)
    print("G count:", g_count)
    print("C count:", c_count)
    print("GC Content:", round(gc_content, 2), "%")

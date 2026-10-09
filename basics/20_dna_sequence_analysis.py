dna = "ATGCGATCGATCGGCTA"

print("DNA Sequence:", dna)
print("Sequence Length:", len(dna))

a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)

gc_content = ((g_count + c_count) / len(dna)) * 100

print("GC Content:", round(gc_content, 2), "%")
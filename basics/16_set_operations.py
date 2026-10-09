biology_topics = {"DNA", "RNA", "Protein", "Cell"}

print("Original set:", biology_topics)

biology_topics.add("Genetics")
print("After adding:", biology_topics)

biology_topics.discard("RNA")
print("After removing:", biology_topics)

print("Number of topics:", len(biology_topics))
print("Is DNA present?", "DNA" in biology_topics)
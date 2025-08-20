from Bio import SeqIO

# Files
original_file = "cp_scaffolded_linear.fasta"
insert_file = "repeat_region_101255_125535_reverse_complement"
output_file = "cp_scaffolded_linear_with_repeat.fasta"

# Insert after ndhF
insert_pos = 81927

# Load sequences
original = SeqIO.read(original_file, "fasta")
insert = SeqIO.read(insert_file, "fasta")

# Insert sequence at position
new_seq = original.seq[:insert_pos] + insert.seq + original.seq[insert_pos:]
original.seq = new_seq

# Save
SeqIO.write(original, output_file, "fasta")
print(f"Inserted at position {insert_pos}, saved to {output_file}")

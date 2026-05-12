import matplotlib.pyplot as plt
stop_input = input("Enter stop codon (TAA, TAG, or TGA): ")
# Initialize dictionary to count codons
codon_counts = {}
# Open fasta file
file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
file = open(file, 'r')
# Initialize variables for reading
current_seq = ''
keep_gene = False
# Read file line by line
for line in file:
    line = line.strip()
    if line.startswith('>'):
        # Process previous gene's sequence
        if keep_gene and current_seq != '':
            # Count codons in steps of 3
            for i in range(0, len(current_seq) - 2, 3):
                codon = current_seq[i:i+3]
                # Only count complete codons
                if len(codon) == 3:
                    if codon in codon_counts:
                        codon_counts[codon] += 1
                    else:
                        codon_counts[codon] = 1
        # Reset for new gene
        current_seq = ''
        keep_gene = False
    else:
        # Build sequence
        current_seq = current_seq + line
        # Check if stop codon is in the whole sequence so far
        if stop_input in current_seq:
            keep_gene = True
# Process the last gene
if keep_gene and current_seq != '':
    for i in range(0, len(current_seq) - 2, 3):
        codon = current_seq[i:i+3]
        if len(codon) == 3:
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1
file.close()
# Create pie chart
labels = list(codon_counts.keys())
sizes = list(codon_counts.values())
plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Codon Usage for Genes Containing ' + stop_input)
# Save chart to file
plt.savefig('codon_usage_pie.png')
print("Pie chart saved as codon_usage_pie.png")
# Ask user for stop codon
stop_input = input("Enter stop codon (TAA, TAG, or TGA): ")
# Open the original fasta file and create output file
infile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
outfile = open('stop_genes.fa', 'w')
# Initialize variables
current_name = ''
current_seq = ''
# Read file line by line
for line in infile:
    line = line.strip()
    # If line starts with >, it's a header line
    if line.startswith('>'):
        # Process previous gene if it exists
        if current_seq != '' and stop_input in current_seq:
            # Extract gene name from header 
            gene_name = current_name.split()[0]
            outfile.write('>' + gene_name + '\n')
            outfile.write(current_seq + '\n')
        # Start new gene: save the header
        current_name = line[1:]
        current_seq = ''
    else:
        # Append sequence line to current sequence
        current_seq = current_seq + line
# Don't forget the last gene
if current_seq != '' and stop_input in current_seq:
    gene_name = current_name.split()[0]
    outfile.write('>' + gene_name + '\n')
    outfile.write(current_seq + '\n')
# Close files
infile.close()
outfile.close()
print("Done! Check stop_genes.fa")
#Define variables
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start = 'AUG'
stops = ['UAA', 'UAG', 'UGA']
longest_orf = ''
max_len = 0
#Iterate the sequence and find the start codon(the last two positions can't be a start of a codon)
for i in range(len(seq) - 2):
 if seq[i:i+3] == start:
#Find stop codon in the rest of sequence
   for j in range(i + 3, len(seq) - 2, 3):
                 codon = seq[j:j+3]
                 if codon in stops:
                     current_orf = seq[i:j+3]
                     current_len = len(current_orf)
                     if current_len > max_len:
                         max_len = current_len
                         longest_orf = current_orf
                     break
print("Longest ORF:", longest_orf)
print("Length (nt):", max_len)
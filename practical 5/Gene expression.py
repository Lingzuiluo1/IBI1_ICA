import matplotlib.pyplot as plt
import numpy as np
#create a dictionary of gene expression and print it
gene_expression = {'TP53':12.4,'EGFR':15.1,'BRCA1':8.2,'PTEN':5.3,'ESR1':10.7}
print(gene_expression)
#Add MYC to the dictionary and print it
gene_expression['MYC'] = 11.6
print(gene_expression)
#Produce a bar chart of the dictionary
genes= list(gene_expression.keys())
expressions= list(gene_expression.values())
plt.figure()
plt.bar(genes, expressions, width=0.5)
plt.xlabel('Genes')
plt.ylabel('Expression Levels')
plt.title('Gene Expression Levels')
#create a variable to represent a gene of interest and check if it is in the dictionary
gene_interest='X' 
#X = TP53,EGFR ...... or any other genes
if gene_interest in gene_expression:
    print(f"{gene_interest} 's expression level: {gene_expression[gene_interest]}")
else:
    print(f"{gene_interest} is not in the dictionary.")
#calculate the average
total = sum(gene_expression.values())
gene_number = len(gene_expression)
average_expression = total / gene_number
print(f"Average gene expression level: {average_expression:.2f}")
plt.show()
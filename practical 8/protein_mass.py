# Amino acid mass table (dictionary)
mass_table = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
    'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
    'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
    'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
    'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
}

def protein_mass(sequence):
    """
    Input: sequence, a string of amino acid letters
    Returns: total mass in amu, or None if unknown amino acid found
    """
    total = 0
    for aa in sequence:
        if aa in mass_table:
            total = total + mass_table[aa]
        else:
            print("Error: unknown amino acid", aa)
            return None
    return total

# Example usage
seq = "MALWMR"
mass = protein_mass(seq)
print("Protein mass:", mass, "amu")
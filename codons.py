def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path) as file:
        rows = file.readlines()
    for row_str in rows:
        parts = row_str.strip().split('\t')
        if len(parts) >= 3:
            codon = parts[0]
            amino_acid_abbr = parts[2]
            codon_dict[codon] = amino_acid_abbr
    return codon_dict



# =====================================================================
# 1. CREATE EMPTY MEMORY BANKS (DICTIONARIES)
# =====================================================================
hmm_matches = {}
blast_matches = {}
tmhmm_matches = {}

# =====================================================================
# 2. READ THE HMM FILE LINE BY LINE (Tier 1 Evidence)
# =====================================================================
# Script is in scripts/, so ".." goes up to root, then down into data/
with open("../data/hmmscan.htab", "r") as file:
    for line in file:
        if line.startswith("#"):
            continue
        columns = line.split("\t")
        
        # Clean up the ID and grab the name
        gene_id = columns[0].replace("_polypeptide", "").strip()
        protein_name = columns[1].strip()
        
        hmm_matches[gene_id] = protein_name

# =====================================================================
# 3. READ THE BLAST FILE EXPORTED FROM MYSQL (Tier 2 Evidence)
# =====================================================================
with open("../data/blast_results.txt", "r") as file:
    next(file)  # Skip the header line
    for line in file:
        columns = line.split("\t")
        if len(columns) >= 2:
            gene_id = columns[0].replace("_polypeptide", "").strip()
            protein_name = columns[1].strip()
            
            blast_matches[gene_id] = protein_name

# =====================================================================
# 4. READ THE GENERATED TMHMM FILE (Tier 3 Evidence)
# =====================================================================
with open("../data/prodigal2fasta.nostars.faa", "r") as file:
    for line in file:
        columns = line.strip().split()
        if not columns or len(columns) < 3:
            continue
            
        gene_id = columns[0]
        feature = columns[2]
        
        # If already marked True on a previous line, pass over it
        if gene_id in tmhmm_matches and tmhmm_matches[gene_id] == True:
            continue
            
        if feature == "TMhelix":
            tmhmm_matches[gene_id] = True
        else:
            tmhmm_matches[gene_id] = False

# =====================================================================
# 5. PROCESS THE MAIN FASTA HEADERS AND APPLY HIERARCHY
# =====================================================================
# Saving the output report directly into the results/ folder
with open("../results/final_annotations.txt", "w") as output_file:
    output_file.write("Gene_ID\tFinal_Annotation\n") # Added file header

    with open("../data/prodigal2fasta.nostars.faa", "r") as file:
        for line in file:
            if line.startswith(">"):
                current_gene_id = line.replace(">", "").replace("_polypeptide", "").strip()
                
                # Reasoning Hierarchy execution
                if current_gene_id in hmm_matches:
                    final_name = hmm_matches[current_gene_id]
                elif current_gene_id in blast_matches:
                    final_name = blast_matches[current_gene_id]
                elif tmhmm_matches.get(current_gene_id) == True:
                    final_name = "predicted transmembrane protein"
                else:
                    final_name = "Hypothetical protein"
                    
                output_file.write(current_gene_id + "\t" + final_name + "\n")

print("Updated pipeline ran successfully! Check 'results/final_annotations.txt'.")

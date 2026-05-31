# DNA Sequence Matcher: A 3-Step Gene Naming Tool

When scientists sequence a new genome, they get a long string of DNA letters, but they don't know what those genes actually *do*. 

This Python program acts like a smart judge. It takes a list of unknown genes, looks at three different types of lab evidence, and automatically picks the best name for each gene based on a strict priority rule.

## How the Program Decides the Winner

For every single gene, the script runs through this simple checklist:

1. **Rule 1: Look for a "Family Match" (Highest Priority)**
   It checks the `hmmscan.htab` file first. This file looks for deep evolutionary shapes. If it finds a solid match here, the script names the gene right away and stops looking.
   
2. **Rule 2: Look for a "Twin Match" (Second Priority)**
   If Rule 1 finds nothing, the script checks the `blast_results.txt` file (which holds matches exported from a database). It looks for genes with highly similar sequences and grabs the best match.
   
3. **Rule 3: Check the "Location" (Third Priority)**
   If there is no family or twin match, we don't know the gene's function. But the script checks the `tmhmm.long` file to see if the protein sits inside a cell membrane. If it does, it names it a `predicted transmembrane protein`.
   
4. **The Catch-All: "The Mystery Gene"**
   If a gene fails all three rules, the script safely labels it a `Hypothetical protein`.

## The Files Used

* `annotate_pipeline.py` - The main Python program you run.
* `prodigal2fasta.nostars.faa` - The master checklist of all your unknown genes.
* `hmmscan.htab` - The file holding the "Family Matches."
* `blast_results.txt` - The file holding the "Twin Matches."
* `prodigal2fasta.nostars.tmhmm.long` - The file holding the cell membrane location info.
* `final_annotations.txt` - The final spreadsheet created by the program showing each gene and its new name.

## How to Run It

Make sure all your files are in the same folder, open your terminal, and type:

```bash
python3 annotate_pipeline.py

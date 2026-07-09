# DNA Sequence Matcher: Automated Gene Annotation Pipeline

A Python-based bioinformatics pipeline that automatically assigns functional gene names to unknown genomic sequences by integrating multiple sources of biological evidence. The pipeline combines HMMER, BLAST, and TMHMM using a rule-based decision system to generate high-confidence gene annotations.

---

## Why This Project?

Newly sequenced genomes often contain thousands of genes with unknown biological function. Manual annotation is time-consuming and requires evaluating multiple sources of evidence. This project demonstrates how computational workflows can automate functional gene annotation by integrating sequence similarity, protein family information, and protein topology predictions into a single reproducible pipeline.

---

## Features

- Performs protein family identification using **HMMER**
- Identifies homologous sequences using **BLAST**
- Predicts transmembrane proteins using **TMHMM**
- Applies a rule-based evidence hierarchy to assign functional gene names
- Generates a final annotation table for downstream biological analysis

---

## Technologies Used

- Python
- HMMER
- BLAST
- TMHMM
- Linux
- Bioinformatics

---

## Pipeline Workflow

The pipeline evaluates each unknown gene using a prioritized evidence-based approach:

1. **Protein Family Match (Highest Priority)**
   - Searches HMMER results for conserved protein domains.
   - Assigns the associated gene function when a confident match is identified.

2. **Sequence Similarity Search**
   - If no HMMER match exists, evaluates BLAST sequence similarity results.
   - Assigns the highest-confidence homologous annotation.

3. **Transmembrane Protein Prediction**
   - If no sequence match is identified, evaluates TMHMM predictions.
   - Labels proteins predicted to contain transmembrane domains.

4. **Fallback Annotation**
   - Genes lacking supporting evidence are labeled as **Hypothetical Protein**.

---

## Project Structure

```
genomic-annotation-pipeline/
│
├── scripts/
│   └── annotate_pipeline.py
│
├── data/
│   ├── input/
│   └── reference/
│
├── results/
│   ├── blast_results.txt
│   ├── hmmscan.htab
│   ├── tmhmm.long
│   └── final_annotations.txt
│
└── README.md
```

---

## Example Output

Input:
- Unknown genomic sequences
- HMMER protein family matches
- BLAST similarity results
- TMHMM topology predictions

Output:

```
Gene_ID         Annotation
gene_001        DNA helicase
gene_002        ATP synthase subunit
gene_003        Predicted transmembrane protein
gene_004        Hypothetical protein
```

The final output is a tab-delimited annotation table that assigns functional gene names based on the highest-confidence biological evidence available.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/riceroni18/genomic-annotation-pipeline.git
cd genomic-annotation-pipeline
```

Run the pipeline:

```bash
python3 annotate_pipeline.py
```

---

## Skills Demonstrated

- Bioinformatics pipeline development
- Python programming
- Functional gene annotation
- Comparative genomics
- Sequence analysis
- Scientific workflow design
- Data integration
- Linux command line

---

## Future Improvements

- Support additional annotation databases (Pfam, InterPro)
- Containerize the workflow using Docker
- Convert the pipeline into a Nextflow workflow
- Generate interactive summary reports
- Improve scalability for larger genomic datasets

---

## Author

**Marina Rice**

M.S. Bioinformatics Candidate | Clinical Genomics | Computational Biology

GitHub: https://github.com/riceroni18
LinkedIn: https://linkedin.com/in/marina-rice-3071a1a9

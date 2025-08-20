# Chloroplast Genome Assembly Pipeline (ONT Data)

This repository contains a workflow for assembling, scaffolding, and polishing a **chloroplast genome** using Oxford Nanopore Technologies (ONT) long-read data. The pipeline integrates basecalling, reference-guided read extraction, de novo assembly, contig scaffolding, inverted repeat duplication, and polishing.

---

## Workflow Overview

1. **Basecalling & Demultiplexing** (Dorado)  
2. **Reference Download** (efetch from NCBI)  
3. **Read Processing** (concatenate barcodes, map with minimap2)  
4. **De novo Assembly** (Flye)  
5. **Reference Comparison** (MUMmer4)  
6. **Contig Extraction & Orientation** (samtools faidx, seqtk reverse-complement)  
7. **Scaffolding** (concatenate contigs into linear genome)  
8. **Inverted Repeat Duplication** (Python script: `insert_repeat.py`)  
9. **Polishing** (Racon ×3 + Medaka)  
10. **Final Evaluation** (MUMmer4)  

---

## Repository Contents

- `workflow` — Main pipeline script  
- `insert_repeat.py` — Python script that inserts duplicated inverted repeat region into scaffold   

---

## Dependencies

Install the following tools:

```bash
conda create -n cp_assembly -c bioconda -c conda-forge \
  dorado flye minimap2 samtools seqtk racon medaka mummer biopython
conda activate cp_assembly

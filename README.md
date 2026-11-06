# FASTA Sequence Toolkit

Python command-line tools for exploring human gene annotation files: looking up genes on chromosome 21, counting chr21 genes by functional category, and finding the genes shared between the chr21 list and the full HUGO gene list.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white) ![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC?logo=pytest&logoColor=white)

## 🧰 Tools

### `gene_names_from_chr21.py`: interactive gene lookup
Loads `chr21_genes.txt` and asks for gene symbols one at a time (case-insensitive), printing each gene's description. Type `quit` or `exit` to stop.

```bash
python gene_names_from_chr21.py -i chr21_genes.txt
```

### `find_common_cats.py`: genes per category
Counts how many chr21 genes fall into each functional category and adds the category's definition. Writes the result to **`OUTPUT/categories.txt`** (`Category`, `Count`, `Description`).

```bash
python find_common_cats.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt
```

### `intersection_of_gene_names.py`: shared gene symbols
Finds the gene symbols present in both `chr21_genes.txt` and `HUGO_genes.txt`, writes them in sorted order to **`OUTPUT/intersection_output.txt`**, and prints summary counts.

```bash
python intersection_of_gene_names.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
# Number of unique gene names in chr21_genes.txt: 285
# Number of unique gene names in HUGO_genes.txt: 11815
# Number of common gene symbols found: 204
```

Every argument has a default, so each script also runs without any flags from the repository root.

## 📊 Data

| File | Contents |
| :--- | :--- |
| `chr21_genes.txt` | Chromosome 21 genes: symbol, description, category |
| `chr21_genes_categories.txt` | Definitions of the chr21 gene categories (1.1–5) |
| `HUGO_genes.txt` | HUGO gene symbols with descriptions |
| `hgnc_complete_set_reduced.txt`, `gene_age.txt` | Extra reference tables (HGNC set, gene age) |

## 🚀 Getting Started

```bash
git clone https://github.com/Adidaware/FASTA-Sequence-Toolkit.git
cd FASTA-Sequence-Toolkit
pip install -r requirements.txt   # only needed to run the tests
```

Run the scripts from the repository root so that the `scripts` package can be imported.

## ✅ Tests

```bash
python -m pytest
```

## 📁 Repository Layout

```
├── gene_names_from_chr21.py
├── find_common_cats.py
├── intersection_of_gene_names.py
├── scripts/
│   ├── utils.py        # gene-file readers, category counts, intersections
│   └── io_utils.py     # creates output directories
├── tests/unit/         # pytest suites for utils and io_utils
└── OUTPUT/             # example output
```

## 🙏 Credits

`scripts/io_utils.py` is based on provided starter code.

## 👤 Author

**Aditya Daware** · [LinkedIn](https://www.linkedin.com/in/aditya-daware) · [GitHub](https://github.com/Adidaware)

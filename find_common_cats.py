""" Count how many chr21 genes fall into each gene category and write OUTPUT/categories.txt """
import argparse
from scripts.io_utils import mkdir_from_infile


def get_cli_args():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(
        description='Combine on gene name and count the category occurrence')
    parser.add_argument('-i1', '--infile1', type=str, default='chr21_genes.txt',
                        help='Path to the gene description file to open')
    parser.add_argument('-i2', '--infile2', type=str, default='chr21_genes_categories.txt',
                        help='Path to the gene category file to open')
    return parser.parse_args()


def main():
    """ Count genes per category and write them with the category descriptions """
    args = get_cli_args()
    category_counts = {}
    with open(args.infile1, 'r', encoding='utf-8') as file:
        next(file)  # skip the header row
        for line in file:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 3 and parts[2].strip():
                category = parts[2].strip()
                category_counts[category] = category_counts.get(category, 0) + 1

    category_descriptions = {}
    with open(args.infile2, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 2:
                category_descriptions[parts[0].strip()] = parts[1].strip()

    outfile = "OUTPUT/categories.txt"
    mkdir_from_infile(file=outfile)
    with open(outfile, 'w', encoding='utf-8') as file:
        file.write("Category\tCount\tDescription\n")
        for category, count in sorted(category_counts.items()):
            description = category_descriptions.get(category, "")
            file.write(f"{category}\t{count}\t{description}\n")
    print(f"Output stored in {outfile}")


if __name__ == "__main__":
    main()

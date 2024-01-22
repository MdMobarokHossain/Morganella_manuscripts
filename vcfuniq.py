import vcf
import argparse
import csv

def get_unique_mutations(file1, file2, output_file):
    vcf_reader1 = vcf.Reader(open(file1, 'r'))
    vcf_reader2 = vcf.Reader(open(file2, 'r'))

    mutations1 = {str(record.CHROM) + str(record.POS) + str(record.REF) + str(record.ALT[0]): record for record in vcf_reader1}
    mutations2 = {str(record.CHROM) + str(record.POS) + str(record.REF) + str(record.ALT[0]): record for record in vcf_reader2}

    unique_mutations_in_file1 = set(mutations1.keys()) - set(mutations2.keys())
    unique_mutations_in_file2 = set(mutations2.keys()) - set(mutations1.keys())

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File', 'Chromosome', 'Position', 'Reference', 'Alternate'])
        for mutation_key in unique_mutations_in_file1:
            record = mutations1[mutation_key]
            writer.writerow([file1, record.CHROM, record.POS, record.REF, record.ALT[0]])
        for mutation_key in unique_mutations_in_file2:
            record = mutations2[mutation_key]
            writer.writerow([file2, record.CHROM, record.POS, record.REF, record.ALT[0]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare mutations in two VCF files and find unique mutations.')
    parser.add_argument('file1', help='Path to the first VCF file')
    parser.add_argument('file2', help='Path to the second VCF file')
    parser.add_argument('output_file', help='Path to the output CSV file')
    args = parser.parse_args()

    get_unique_mutations(args.file1, args.file2, args.output_file)


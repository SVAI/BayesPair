import vcf

def main(file_input, file_output):

    vcf_file = file_input
    results = ''
    for rec in vcf.Reader(open(vcf_file,'r')):
        results += '{},{},{},{}\n'.format(rec.CHROM, rec.POS, rec.REF, rec.ALT, rec.QUAL)

    with open("{}.csv".format(file_output), "w") as text_file:
        text_file.write(results)


if __name__ == '__main__':
    main()
import vcf

def write_filtered_csv(file_input, file_output, only_snps=True):

    results = ''
    for rec in vcf.Reader(open(file_input,'r')) :
        if only_snps:
            if rec.is_snp:
                results += '{},{},{},{}\n'.format(rec.CHROM, rec.POS, rec.REF, rec.ALT, rec.QUAL)
        elif not only_snps: 
            results += '{},{},{},{}\n'.format(rec.CHROM, rec.POS, rec.REF, rec.ALT, rec.QUAL)

    with open("{}.csv".format(file_output), "w") as text_file:
        text_file.write(results)


def filter_only_snps_vcf(file_input, file_output, only_snps=True):
    
    vcf_reader = vcf.Reader(filename=file_input)
    vcf_writer = vcf.Writer(open(file_output,'w'), vcf_reader)
    for record in vcf_reader:
        if record.is_snp:
            vcf_writer.write_record(record)




if __name__ == '__main__':
    filter_only_snps_vcf('','.vcf') # insert file_input and file_output names
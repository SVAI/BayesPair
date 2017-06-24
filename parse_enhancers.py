from collections import defaultdict
import vcf

enhancer_regions = defaultdict(list)

with open('vista_enhancers.txt', 'r') as f:
	lines = f.readlines()
	for line in lines:
		if line[0] == '>':
			entry = line.split('|')
			chrom_entry = entry[1].split(':')
			chrom = chrom_entry[0].replace('chr', '')
			base_range = chrom_entry[1]
			start, end = base_range.split('-')
			enhancer_regions[chrom].append((int(start), int(end)))

enhancer_vcfs = []

with open('/mnt/disks/data-vcf/GSN79Tumor_normal.vcf', 'r') as f:
	entries = vcf.Reader(f)
	for entry in entries:
		chrom = str(entry.CHROM)
		enhancers = enhancer_regions[chrom]
		for enhancer_region in enhancers:
			start, stop = enhancer_region
			if start < entry.POS < stop:
				enhancer_vcfs.append(entry)
				break
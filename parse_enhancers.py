from collections import defaultdict

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

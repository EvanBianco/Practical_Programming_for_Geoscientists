# Add up the numbers of lithologies in a file
import sys

# Get new lithologies from a line and add it to collectio 
def update_lithset(line, lithset):
	"""
	Checks a lithology and sees if it is already
	in the lithset. If not, it adds it
	Returns a list of lithologies
	"""
	temp = line.strip()
	fields = temp.split()
	if fields[1].upper() not in lithset:
		lithset.append(fields[1].upper())
	return lithset

# Should this line be skipped because it is in the header?
def should_skip_line(line):
	return line.startswith('#') or line.startswith('~')

# Make a list of all lithologies in a data file
def get_lithset(source):
	"""
	Gets all the unique lithologies in a data file
	"""
	lithset = [] 
	for line in source:
		if should_skip_line(line):
			pass  
		else:
			update_lithset(line, lithset)
	return lithset

# Show total number of lithologies for each file given on the command line
for filename in sys.argv[1:]:
	reader = open(filename, 'r')
	lithset = get_lithset(reader)
	reader.close()
	print(filename.strip(), ':', len(lithset))
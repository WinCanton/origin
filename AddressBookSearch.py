def search(keyword, filename):
	print('generator started')
	f = open(filename, 'r')
	for line in f:
		if keyword in line:
			yield line
	f.close()

the_generator = search('Admiral', 'AddressBook.csv')

print(the_generator.next())
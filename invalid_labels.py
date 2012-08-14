#!/usr/bin/python

import sys, re
import data_structures


class LabelCollection(object):
	def __init__(self):
		super(LabelCollection, self).__init__()
		self.__labels = data_structures.ArrayDict()
		self.__refs = data_structures.ArrayDict()
		self.__label_regex = re.compile('\\label\{([^}]+)\}')
		self.__refs_regex = re.compile('\\ref\{([^}]+)\}')

	def update(self, tex_file):
		fp = open(tex_file, 'r')

		for line in fp:
			l = line.strip()
			if len(l) == 0:
				continue

			self.__put_labels(tex_file, l)
			self.__put_refs(tex_file, l)

		fp.close()

	def __put_labels(self, tex_file, line):
		for m in self.__label_regex.findall(line):
			self.__labels.put(m, tex_file)

	def __put_refs(self, tex_file, line):
		for m in self.__refs_regex.findall(line):
			self.__refs.put(m, tex_file)

	def get_labels(self):
		return self.__labels

	def get_refs(self):
		return self.__refs

	def validate_labels(self):
		print 'Validating Labels'
		total = 0
		warnings = 0

		for k in self.__labels.keys():
			files = self.__labels.get(k)

			if len(files) > 1:
				print '%s : %s' % (k, files)
				warnings += 1

			total += 1

		print 'Labels Found: %d' % (total,)
		print 'Valid Found: %d' % (total - warnings,)
		print 'Warnings Found: %d' % (warnings,)

	def validate_refs(self):
		print 'Validating Refs'
		total = 0
		warnings = 0

		for k in self.__refs.keys():
			if not self.__labels.has_key(k):
				print '%s : %s' % (k, self.__refs.get(k))
				warnings += 1

			total += 1

		print 'References Found: %d' % (total,)
		print 'Valid References: %d' % (total - warnings,)
		print 'Warnings Found: %d' % (warnings,)


def main():
	if len(sys.argv) == 1:
		print "TexUtils: Find Invalid Labels"
		print "-----------------------------"
		print "Vassilios Karakoidas (c) 2012"
		print "email: vassilios.karakoidas@gmail.com"
		print "www: http://bkarak.wizhut.com/\n"
		print "usage:"
		print "invalid-labels.py <list-of-tex-files>"
		return

	lbl_col = LabelCollection()

	for tex_file in sys.argv[1:]:
		lbl_col.update(tex_file)
	
	lbl_col.validate_labels()
	lbl_col.validate_refs()

if __name__ == '__main__':
	main()

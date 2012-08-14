#!/usr/bin/python

import sys, re
import data_structures


class LabelCollection(object):
	def __init__(self):
		super(LabelCollection, self).__init__()
		self.__labels = data_structures.ArrayDict()
		self.__refs = data_structures.ArrayDict()

	def update(self, tex_file):
		fp = open(tex_file, 'r')

		for line in fp:
			if len(line.strip()) == 0:
				continue

			self.__put_labels(line.strip())

		fp.close()

	def __put_labels(self, line):
		label_re = re.compile('\\label\{([^}]+)\}')


	def __put_refs(self, line):
		ref_re = re.compile('\\ref\{([^}]+)\}')



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

if __name__ == '__main__':
	main()

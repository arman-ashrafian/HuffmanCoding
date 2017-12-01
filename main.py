# Arman Ashrafian
# 11-30-2017

# This file tests the huffman compression of the Gettysburg Address.
# Compresses the file from 1473 bytes to 773 bytes.
#
# Compression Ratio: 1.91

from huffmancoding import HuffmanCoding
import os

def main():
	OUTPUT_FREQ_TABLE = False

	path = "C:\\Users\\arman\\Desktop\\HuffmanCoding\\text\\gettysburg.txt"
	path2 = "C:\\Users\\arman\\Desktop\\HuffmanCoding\\text\\gettysburg.bin"

	h = HuffmanCoding(path)

	output_path = h.compress()

	h.decompress(output_path)

	# print out frquency table and huffman codes for each letter
	if OUTPUT_FREQ_TABLE:
		print('Frequency Table')
		for node in h.og_heap:
			print('%s - %s' % (node.char, node.freq))

	# print out the compression ratio
	og_size = os.stat(path).st_size
	de_size = os.stat(path2).st_size

	print('\nCompression Ratio: %.4f' % (og_size/de_size))



if __name__ == '__main__':
	main()
# Arman Ashrafian
# 11-30-2017

# This file implements everything needed for Lossless Huffman Coding.
# HuffmanCoding takes the full path of file to be compressed and builds
# the neccessary codes for encoding.

# compress() 		- Returns the path of the compressed file (.bin format)
#
# decompress(path) 	- Requires path of file to be decompressed. Must be called
#                     from same object that called compressed because the code
#                     mapping is a data member of the object.  

import os
import heapq

class HuffmanCoding:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.encodes = {}
		self.decodes = {}

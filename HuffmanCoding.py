	# Arman Ashrafian
	# 11-30-2017

	# This file implements everything needed for Lossless Huffman Coding.
	# HuffmanCoding takes the full path of file to be compressed and builds
	# the neccessary codes for encoding.

	# compress()        - Returns the path of the compressed file (.bin format)
	#
	# decompress(path)  - Requires path of file to be decompressed. Must be called
	#                     from same object that called compressed because the code
	#                     mapping is a data member of the object.  

import os
import heapq

# Huffman Tree Node
class Node:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq

		# children
		self.left = None
		self.right = None

	# compare nodes by frequency
	def __cmp__(self, other):
		if other == None or not isinstance(other, Node):
			return -1
		else:
			return self.freq > other.freq

class HuffmanCoding:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.encodes = {}
		self.decodes = {}

	def build_frequency_dict(self, text):
		freq = {}
		for ch in text:
			if not ch in freq:
				freq[ch] = 0
			freq[ch] += 1 
		return freq 

	def build_priority_queue(self, freq):
		for key in freq:
			heapq.heappush(self.heap, Node(key, freq[key]))

	def merge_nodes(self):
		while(len(self.heap) > 1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged_node = Node(None, node1.freq + node2.freq)
			merged.left = node1 
			merged.right = node2 

			heapq.heappush(self.heap, merged_node)

	def recur_make_codes(self, node, currentCode):
		if node == None: return 
		if node.char != None:
			self.encodes[node.char] = currentCode
			self.decodes[currentCode] = node.char
			return
		# going left (0)
		self.recur_make_codes(node.left, currentCode + "0")
		# going right (1)
		self.recur_make_codes(node.right, currentCode + "1")

	def make_codes(self):
		root = heapq.heappop(self.heap)
		currentCode = ""
		self.recur_make_codes(root, currentCode)

	def get_encoded_text(self, text):
		encoded_text = ""
		for ch in text:
			encoded_text += self.encodes[ch]
		return encoded_text

	def add_padding(self, encodedText):
		''' 
		Adds extra 0's to end of encoded text to ensure 8 bits per byte.
		Padding info put at beginning of encoded text for decompression.
		'''
		padding = 8 - (len(encodedText) % 8)
		for i in range(padding):
			encodedText += "0"
		# convets padding to 8 bit binary
		paddedInfo = "{0:08b}".format(padding)   
		encodedText = paddedInfo + encodedText

	def get_byte_array(self, paddedText):
		b = bytearray()
		for i in range(0, len(paddedText), 8):
			byte = paddedText[i:i+8]
			b.append(int(byte, 2))
		return b


from huffmancoding import HuffmanCoding

def main():
	path = "C:\\Users\\arman\\Desktop\\HuffmanCoding\\text\\sample1.txt"

	h = HuffmanCoding(path)

	output_path = h.compress()

if __name__ == '__main__':
	main()
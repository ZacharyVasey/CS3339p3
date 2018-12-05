from memoryUnit import MemoryUnit, Cache


def main():
	opCodeString = ["STUR", "STUR", "STUR", "LDUR", "LDUR", "STUR", "LDUR"]
	address = [0, 0, 0, 0, 4, 0, 0]
	offset = [0, 1, 2, 0, 0, 4, 4]
	premem = [66, 2, 85, '', '', 1, '']
	postmem = ['', '', '', '', '', '', '']
	
	cache = Cache()
	mem = MemoryUnit(cache)
	
	index = 0
	
	while(index < 6):
		mem.setContent(premem[index])
		mem.accessMemory(opCodeString[index], address[index], offset[index])
		postmem[index] = mem.getContent()
		index = index + 1
	print postmem
	
if __name__== "__main__":
	main()
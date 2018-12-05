from memoryUnit import MemoryUnit, Cache


def main():
	opCodeString = ["STUR", "STUR", "STUR", "LDUR", "LDUR", "STUR", "LDUR"]
	address = [0, 0, 0, 0, 4, 0, 0]
	offset = [0, 1, 2, 0, 0, 4, 4]
	premem = [66, 2, 85, '', '', 1, '']
	postmem = ['', '', '', '', '', '', '']
	
	cache = Cache(10)
	mem = MemoryUnit(cache)
	
	index = 0
	
	while(index < 6):
		print "\n\n"
		print("Load in from premem: " + str(premem[index]))
		mem.setContent(premem[index])
		print(opCodeString[index] + ", address: " + str(address[index]) + ", offset: " + str(offset[index]))
		mem.accessMemory(opCodeString[index], address[index], offset[index])
		print("result: " + str(mem.getContent()))
		postmem[index] = mem.getContent()
		print("Cache: " + str(cache.data))
		index = index + 1
	
if __name__== "__main__":
	main()
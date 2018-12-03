from reg import RegFile
from writeback import WriteBack

def main():
	regob = RegFile()
	wbob = WriteBack(regob)
	regob.printRegFile()

	# TEST WB to write post-ALU
	print 'PALU: write 5 to r5.'
	wbob.writeRegFile(5, 5)
	regob.printRegFile()
	wbob.contOn()
	wbob.writeRegFile(5, 5)
	regob.printRegFile()	
	print 'PALU: write 10 to r10 and 15 to r15.'
	wbob.contOff()
	wbob.writeRegFile(10, 10, 15, 15)
	regob.printRegFile()
	wbob.contOn()
	wbob.writeRegFile(10, 10, 15, 15)
	regob.printRegFile()

	# TESTPRINT - Direct print of register file.
	# print
	# for el in regob.regFile:
	# 	print el, 



if __name__== "__main__":
	main()

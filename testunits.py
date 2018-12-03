from reg import RegFile
from postmem import PostMem 
from postalu import PostAlu
from writeback import WriteBack

def main():
	regob = RegFile()
	pmo = PostMem()
	pao = PostAlu()
	wbob = WriteBack(regob, pmo, pao)
	regob.printRegFile()

	# TEST WB to write post-ALU
	print '//============================================================='
	print '//	WRITEBACK MODULE TEST'
	print '//============================================================='
	print '>>> PHASE 1: write directly to register file.\n'
	wbob.contOff()
	print 'Write 5 to r5.'
	wbob.writeReg(5, 5)
	regob.printRegFile()		# Values 5 should NOT be written to r5.
	wbob.contOn()
	wbob.writeReg(5, 5)
	regob.printRegFile()		# Values 5 should be written to r5.
	wbob.contOff()
	print 'Write 10 to r10 and 15 to r15.'	
	wbob.writeReg(10, 10, 15, 15)
	regob.printRegFile()		# Values 10 and 15 should NOT be written to r10 & r15.
	wbob.contOn()				
	wbob.writeReg(10, 10, 15, 15)
	regob.printRegFile()		# Values 10 and 15 should be written to r10 & r15.
	print '>>> PHASE 2: pull from buffers and write to register file.\n'
	wbob.contOff()				# With control off, attempt to write to registers
	pmo.setContent(6, 6)		# from post-mem and post-alu.
	pao.setContent(7, 7)
	pmo.printContent()
	pao.printContent()
	wbob.writeFromBuffs()
	regob.printRegFile()		# Values 6 and 7 should NOT be written to r6 & r7.
	wbob.contOn()
	pmo.setContent(6, 6)
	pao.setContent(7, 7)
	pmo.printContent()
	pao.printContent()
	wbob.writeFromBuffs()
	regob.printRegFile()		# Values 6 & 7 should be written to r6 & r7.
	wbob.contOff()
	pao.setContent(None, None)
	pmo.setContent(8, 8)
	pmo.printContent()
	pao.printContent()
	wbob.writeFromBuffs()
	regob.printRegFile()		# Value 8 should NOT print written to r8.
	wbob.contOn()
	wbob.writeFromBuffs()
	regob.printRegFile()		# Value 8 should print written to r8.
	wbob.contOff()
	pmo.setContent(None, None)
	pao.setContent(9, 9)
	pmo.printContent()
	pao.printContent()
	wbob.writeFromBuffs()
	regob.printRegFile()		# Value 9 should NOT print written to r9.
	wbob.contOn()
	wbob.writeFromBuffs()
	regob.printRegFile()		# Value 9 should print written to r9.



	# #TESTPRINT - Direct print of register file.
	# print
	# for el in regob.regFile:
	# 	print el, 

if __name__== "__main__":
	main()

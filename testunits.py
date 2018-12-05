from reg import RegFile
from postmem import PostMem 
from postalu import PostAlu
from prealu import PreAlu
from premem import PreMem
from preiss import PreIss
from writeback import WriteBack

def main():
	regob = RegFile()
	pmo = PostMem()
	pao = PostAlu()
	prao = PreAlu()
	prmo = PreMem()
	prio = PreIss()
	wbob = WriteBack(regob, pmo, pao)
	regob.printRegFile()

	# TEST WB to write post-ALU
	print '//=================================================================='
	print '//	MODULE TEST - WRITEBACK - POSTMEM - POSTALU'
	print '//=================================================================='
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

	# TEST WB to write post-ALU
	print '//=================================================================='
	print '//	MODULE TEST - PREALU - PREMEM'
	print '//=================================================================='
	print '>>> PHASE 1: Test passing PC values to Pre-ALU buffer, and simul-\n' \
			+ '-taneously update OLDEST truth value.'
	print 'The buffer is fed the address of an instruction in memory - '
	print 'aka the bindata index.'			
	print '\t Feed: [bindata index]'

	suc = False
	prao.printBuff()
	
	print '\nFeed 96'
	suc = prao.feedBuff(96)
	print "Success:", str(suc)
	prao.printBuff()
	
	print '\nFeed 100'
	suc = prao.feedBuff(100)
	print "Success:", str(suc)
	prao.printBuff()
	
	print '\nFeed 104'
	suc = prao.feedBuff(104)
	print "Success:", str(suc)
	prao.printBuff()
	
	print "\nEmpty"
	suc = prao.emptyBuff()
	print "Success:", str(suc)
	prao.printBuff()
	
	print "\nEmpty"
	suc = prao.emptyBuff()
	print "Success:", str(suc)
	prao.printBuff()
	
	print "\nEmpty"
	suc = prao.emptyBuff()
	print "Success:", str(suc)
	prao.printBuff()	
	
	print "\nEmpty"
	suc = prao.emptyBuff()
	print "Success:", str(suc)
	prao.printBuff()
	
	print '\nFeed 104'
	suc = prao.feedBuff(104)
	print "Success:", str(suc)
	prao.printBuff()
	
	print "\nEmpty"
	suc = prao.emptyBuff()
	print "Success:", str(suc)
	prao.printBuff()
	
	print '\nFeed 156'
	suc = prao.feedBuff(156)
	print "Success:", str(suc)
	prao.printBuff()
	
	print '\nFeed 96'
	suc = prao.feedBuff(96)
	print "Success:", str(suc)
	prao.printBuff()

	print '\n>>> PHASE 2: Test passing PC values to Pre-MEM buffer, and simultaneously\n'\
		'update OLDEST truth value.  The buffer is fed the address \nof '\
		'an instruction in memory - aka the bindata index.'

	suc = False
	prmo.printBuff()
	
	print '\nFeed 96'
	suc = prmo.feedBuff(96)
	print "Success:", str(suc)
	prmo.printBuff()
	
	print '\nFeed 100'
	suc = prmo.feedBuff(100)
	print "Success:", str(suc)
	prmo.printBuff()
	
	print '\nFeed 104'
	suc = prmo.feedBuff(104)
	print "Success:", str(suc)
	prmo.printBuff()
	
	print "\nEmpty"
	suc = prmo.emptyBuff()
	print "Success:", str(suc)
	prmo.printBuff()
	
	print "\nEmpty"
	suc = prmo.emptyBuff()
	print "Success:", str(suc)
	prmo.printBuff()
	
	print "\nEmpty"
	suc = prmo.emptyBuff()
	print "Success:", str(suc)
	prmo.printBuff()	
	
	print "\nEmpty"
	suc = prmo.emptyBuff()
	print "Success:", str(suc)
	prmo.printBuff()
	
	print '\nFeed 104'
	suc = prmo.feedBuff(104)
	print "Success:", str(suc)
	prmo.printBuff()
	
	print "\nEmpty"
	suc = prmo.emptyBuff()
	print "Success:", str(suc)
	prmo.printBuff()
	
	print '\nFeed 156'
	suc = prmo.feedBuff(156)
	print "Success:", str(suc)
	prmo.printBuff()
	
	print '\nFeed 96'
	suc = prmo.feedBuff(96)
	print "Success:", str(suc)
	prmo.printBuff()

	print '\n//=================================================================='
	print '//	MODULE TEST - PRE-ISSUE'
	print '//=================================================================='
	print '>>> PHASE 1: Test feeding, emptying, and sorting Pre-Issue Buffer.'
	print 'The buffer is fed the address of an instruction in memory - '
	print 'aka the bindata index.'
	print '\tFeed: [bindata index] or [bindata index, bindata index]'
	print '\tEmpty: [pre-issue buffer index, bindata index]'
	count = 0
	suc = False
	prio.printBuff()

	count = prio.countEmpties()
	print 'Feed: 96'
	print 'Empties:', count
	suc = prio.feedBuff(96)
	print 'Success:', suc
	prio.printBuff()

	count = prio.countEmpties()
	print 'Feed: 100, 104'
	print 'Empties:', count
	suc = prio.feedBuff(100, 104)
	print 'Success:', suc
	prio.printBuff()	

	count = prio.countEmpties()
	print 'Feed: 108, 112'
	print 'Empties:', count
	suc = prio.feedBuff(108, 112)
	print 'Success:', suc
	prio.printBuff()	

	count = prio.countEmpties()
	print 'Feed: 108'
	print 'Empties:', count
	suc = prio.feedBuff(96)
	print 'Success:', suc
	prio.printBuff()

	count = prio.countEmpties()
	print 'Feed: 96'
	print 'Empties:', count
	suc = prio.feedBuff(96)
	print 'Success:', suc
	prio.printBuff()

	print 'Sort buffer'
	prio.sortBuff()
	prio.printBuff()

	print 'Empty: 1, 96'
	suc = prio.emptyBuff(1, 96)
	print 'Success:', suc
	prio.printBuff()

	print 'Empty: 1, 96'
	suc = prio.emptyBuff(1, 96)
	print 'Success:', suc
	prio.printBuff()

	print 'Empty: 0, 104'
	suc = prio.emptyBuff(0, 104)
	print 'Success:', suc
	prio.printBuff()

	# print 'Empty buffer: 5, 100'
	# print 'Empties:', count
	# suc = prio.emptyBuff(5, 100)
	# print 'Success:', suc
	# prio.printBuff()

	print 'Empty: 2, 100'
	suc = prio.emptyBuff(2, 100)
	print 'Success:', suc
	prio.printBuff()

	count = prio.countEmpties()
	print 'Feed: 108, 112'
	print 'Empties:', count
	suc = prio.feedBuff(108, 112)
	print 'Success:', suc
	prio.printBuff()	

	print 'Sort'
	prio.sortBuff()
	prio.printBuff()

	print 'Empty: 1, 96'
	suc = prio.emptyBuff(1, 96)
	print 'Success:', suc
	prio.printBuff()

	print 'Empty: 0, 96'
	suc = prio.emptyBuff(0, 96)
	print 'Success:', suc
	prio.printBuff()

	count = prio.countEmpties()
	print 'Feed: 116, 120'
	print 'Empties:', count
	suc = prio.feedBuff(116, 120)
	print 'Success:', suc
	prio.printBuff()	

	print 'Empty: 1, 104'
	suc = prio.emptyBuff(1, 104)
	print 'Success:', suc
	prio.printBuff()

	print 'Empty: 3, 112'
	suc = prio.emptyBuff(3, 112)
	print 'Success:', suc
	prio.printBuff()

	print 'Empty: 2, 108'
	suc = prio.emptyBuff(2, 108)
	print 'Success:', suc
	prio.printBuff()
	
	print '//=================================================================='
	print '//	MODULE TEST - CACHE'
	print '//=================================================================='
	print '>>> PHASE 1: write directly to register file.\n'


if __name__== "__main__":
	main()
	print
	print

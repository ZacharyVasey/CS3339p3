from reg import RegFile
from postmem import PostMem 
from postalu import PostAlu
from prealu import PreAlu
from premem import PreMem
from preiss import PreIss
from cache import Cache
from writeback import WriteBack

class TestUnits(object):
	def __init__(self, binDataOb):
		self.regob = RegFile()
		self.pmo = PostMem()
		self.pao = PostAlu()
		self.prao = PreAlu()
		self.prmo = PreMem()
		self.prio = PreIss()
		self.cbo = Cache(binDataOb)
		self.wbob = WriteBack(self.regob, self.pmo, self.pao)
		self.regob.printRegFile()
		self.bdo = binDataOb
	def run(self):


		# TEST WB to write post-ALU
		print '//=================================================================='
		print '//	MODULE TEST - WRITEBACK - POSTMEM - POSTALU'
		print '//=================================================================='
		print '>>> PHASE 1: write directly to register file.\n'
		self.wbob.contOff()
		print 'Write 5 to r5.'
		self.wbob.writeReg(5, 5)
		self.regob.printRegFile()		# Values 5 should NOT be written to r5.
		self.wbob.contOn()
		self.wbob.writeReg(5, 5)
		self.regob.printRegFile()		# Values 5 should be written to r5.
		self.wbob.contOff()
		print 'Write 10 to r10 and 15 to r15.'	
		self.wbob.writeReg(10, 10, 15, 15)
		self.regob.printRegFile()		# Values 10 and 15 should NOT be written to r10 & r15.
		self.wbob.contOn()				
		self.wbob.writeReg(10, 10, 15, 15)
		self.regob.printRegFile()		# Values 10 and 15 should be written to r10 & r15.
		print '>>> PHASE 2: pull from buffers and write to register file.\n'
		self.wbob.contOff()				# With control off, attempt to write to registers
		self.pmo.setContent(6, 6)		# from post-mem and post-alu.
		self.pao.setContent(7, 7)
		self.pmo.printContent()
		self.pao.printContent()
		self.wbob.writeFromBuffs()
		self.regob.printRegFile()		# Values 6 and 7 should NOT be written to r6 & r7.
		self.wbob.contOn()
		self.pmo.setContent(6, 6)
		self.pao.setContent(7, 7)
		self.pmo.printContent()
		self.pao.printContent()
		self.wbob.writeFromBuffs()
		self.regob.printRegFile()		# Values 6 & 7 should be written to r6 & r7.
		self.wbob.contOff()
		self.pao.setContent(None, None)
		self.pmo.setContent(8, 8)
		self.pmo.printContent()
		self.pao.printContent()
		self.wbob.writeFromBuffs()
		self.regob.printRegFile()		# Value 8 should NOT print written to r8.
		self.wbob.contOn()
		self.wbob.writeFromBuffs()
		self.regob.printRegFile()		# Value 8 should print written to r8.
		self.wbob.contOff()
		self.pmo.setContent(None, None)
		self.pao.setContent(9, 9)
		self.pmo.printContent()
		self.pao.printContent()
		self.wbob.writeFromBuffs()
		self.regob.printRegFile()		# Value 9 should NOT print written to r9.
		self.wbob.contOn()
		self.wbob.writeFromBuffs()
		self.regob.printRegFile()		# Value 9 should print written to r9.

		# #TESTPRINT - Direct print of register file.
		# print
		# for el in self.regob.regFile:
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
		self.prao.printBuff()
		
		print '\nFeed 96'
		suc = self.prao.feedBuff(96)
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print '\nFeed 100'
		suc = self.prao.feedBuff(100)
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print '\nFeed 104'
		suc = self.prao.feedBuff(104)
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print "\nEmpty"
		suc = self.prao.emptyBuff()
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print "\nEmpty"
		suc = self.prao.emptyBuff()
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print "\nEmpty"
		suc = self.prao.emptyBuff()
		print "Success:", str(suc)
		self.prao.printBuff()	
		
		print "\nEmpty"
		suc = self.prao.emptyBuff()
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print '\nFeed 104'
		suc = self.prao.feedBuff(104)
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print "\nEmpty"
		suc = self.prao.emptyBuff()
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print '\nFeed 156'
		suc = self.prao.feedBuff(156)
		print "Success:", str(suc)
		self.prao.printBuff()
		
		print '\nFeed 96'
		suc = self.prao.feedBuff(96)
		print "Success:", str(suc)
		self.prao.printBuff()

		print '\n>>> PHASE 2: Test passing PC values to Pre-MEM buffer, and simultaneously\n'\
			'update OLDEST truth value.  The buffer is fed the address \nof '\
			'an instruction in memory - aka the bindata index.'

		suc = False
		self.prmo.printBuff()
		
		print '\nFeed 96'
		suc = self.prmo.feedBuff(96)
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print '\nFeed 100'
		suc = self.prmo.feedBuff(100)
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print '\nFeed 104'
		suc = self.prmo.feedBuff(104)
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print "\nEmpty"
		suc = self.prmo.emptyBuff()
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print "\nEmpty"
		suc = self.prmo.emptyBuff()
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print "\nEmpty"
		suc = self.prmo.emptyBuff()
		print "Success:", str(suc)
		self.prmo.printBuff()	
		
		print "\nEmpty"
		suc = self.prmo.emptyBuff()
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print '\nFeed 104'
		suc = self.prmo.feedBuff(104)
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print "\nEmpty"
		suc = self.prmo.emptyBuff()
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print '\nFeed 156'
		suc = self.prmo.feedBuff(156)
		print "Success:", str(suc)
		self.prmo.printBuff()
		
		print '\nFeed 96'
		suc = self.prmo.feedBuff(96)
		print "Success:", str(suc)
		self.prmo.printBuff()

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
		self.prio.printBuff()

		count = self.prio.countEmpties()
		print 'Feed: 96'
		print 'Empties:', count
		suc = self.prio.feedBuff(96)
		print 'Success:', suc
		self.prio.printBuff()

		count = self.prio.countEmpties()
		print 'Feed: 100, 104'
		print 'Empties:', count
		suc = self.prio.feedBuff(100, 104)
		print 'Success:', suc
		self.prio.printBuff()	

		count = self.prio.countEmpties()
		print 'Feed: 108, 112'
		print 'Empties:', count
		suc = self.prio.feedBuff(108, 112)
		print 'Success:', suc
		self.prio.printBuff()	

		count = self.prio.countEmpties()
		print 'Feed: 108'
		print 'Empties:', count
		suc = self.prio.feedBuff(96)
		print 'Success:', suc
		self.prio.printBuff()

		count = self.prio.countEmpties()
		print 'Feed: 96'
		print 'Empties:', count
		suc = self.prio.feedBuff(96)
		print 'Success:', suc
		self.prio.printBuff()

		print 'Sort buffer'
		self.prio.sortBuff()
		self.prio.printBuff()

		print 'Empty: 1, 96'
		suc = self.prio.emptyBuff(1, 96)
		print 'Success:', suc
		self.prio.printBuff()

		print 'Empty: 1, 96'
		suc = self.prio.emptyBuff(1, 96)
		print 'Success:', suc
		self.prio.printBuff()

		print 'Empty: 0, 104'
		suc = self.prio.emptyBuff(0, 104)
		print 'Success:', suc
		self.prio.printBuff()

		# print 'Empty buffer: 5, 100'
		# print 'Empties:', count
		# suc = self.prio.emptyBuff(5, 100)
		# print 'Success:', suc
		# self.prio.printBuff()

		print 'Empty: 2, 100'
		suc = self.prio.emptyBuff(2, 100)
		print 'Success:', suc
		self.prio.printBuff()

		count = self.prio.countEmpties()
		print 'Feed: 108, 112'
		print 'Empties:', count
		suc = self.prio.feedBuff(108, 112)
		print 'Success:', suc
		self.prio.printBuff()	

		print 'Sort'
		self.prio.sortBuff()
		self.prio.printBuff()

		print 'Empty: 1, 96'
		suc = self.prio.emptyBuff(1, 96)
		print 'Success:', suc
		self.prio.printBuff()

		print 'Empty: 0, 96'
		suc = self.prio.emptyBuff(0, 96)
		print 'Success:', suc
		self.prio.printBuff()

		count = self.prio.countEmpties()
		print 'Feed: 116, 120'
		print 'Empties:', count
		suc = self.prio.feedBuff(116, 120)
		print 'Success:', suc
		self.prio.printBuff()	

		print 'Empty: 1, 104'
		suc = self.prio.emptyBuff(1, 104)
		print 'Success:', suc
		self.prio.printBuff()

		print 'Empty: 3, 112'
		suc = self.prio.emptyBuff(3, 112)
		print 'Success:', suc
		self.prio.printBuff()

		print 'Empty: 2, 108'
		suc = self.prio.emptyBuff(2, 108)
		print 'Success:', suc
		self.prio.printBuff()
		
		print '//=================================================================='
		print '//	MODULE TEST - CACHE'
		print '//=================================================================='
		print '>>> PHASE 1: test correct pc mapping of block offset, set index,'\
			+ '\nand tag.'




		self.cbo.printCache()
		bloff = 0
		pc = 96

		print '\nBlock offset:', pc
		print 'Expect: 0' 
		bloff = self.cbo.getBlockOffset(pc)
		print 'Result:', bloff
		
		pc += 4
		print '\nBlock offset:', pc
		print 'Expect: 1' 
		bloff = self.cbo.getBlockOffset(pc)
		print 'Result:', bloff

		pc += 4
		print '\nBlock offset:', pc
		print 'Expect: 0' 
		bloff = self.cbo.getBlockOffset(pc)
		print 'Result:', bloff

		pc += 4
		print '\nBlock offset:', pc
		print 'Expect: 1' 
		bloff = self.cbo.getBlockOffset(pc)
		print 'Result:', bloff

		pc += 2
		print '\nBlock offset:', pc
		print 'Expect: -1' 
		bloff = self.cbo.getBlockOffset(pc)
		print 'Result:', bloff


		pc += 2
		print '\nBlock offset:', pc
		print 'Expect: 0' 
		bloff = self.cbo.getBlockOffset(pc)
		print 'Result:', bloff

		pc += 1
		print '\nBlock offset:', pc
		print 'Expect: -1' 
		bloff = self.cbo.getBlockOffset(pc)
		print 'Result:', bloff

		pc = 96
		setInd = 0
		self.cbo.printCache()

		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 0' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc += 4
		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 0' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc += 4
		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 1' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc += 4
		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 1' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc += 4
		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 2' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc += 4
		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 2' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc += 4
		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 3' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc += 4
		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 3' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc += 4
		print '\nSet index:', pc, ' ~ ', bin(pc)
		print 'Expect: 0' 
		setInd = self.cbo.getSetIndex(pc)
		print 'Result:', setInd

		pc = 96
		tag = 0
		self.cbo.printCache()

		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 3' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		pc += 4
		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 3' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		pc += 4
		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 3' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		pc += 4
		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 3' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		pc += 4
		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 3' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		pc += 4
		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 3' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		pc += 400
		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 16' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		pc += 4
		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 16' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		pc += 100
		print '\nTag:', pc, ' ~ ', bin(pc)
		print 'Expect: 19' 
		tag = self.cbo.getTag(pc)
		print 'Result:', tag

		print '\n>>> PHASE 2'

		self.cbo.fabTestCache()
		self.cbo.printCache()
		pc = 104
		cAddr = [0, 0, 0]

		# 104
		print '\nCache Address:', pc 
		print 'Expect: [1, 0, 0]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		pc += 4  #108
		print '\nCache Address:', pc
		print 'Expect: [1, 0, 1]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		pc += 4	#112
		print '\nCache Address:', pc
		print 'Expect: [2, 0, 0]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		pc += 4	#116
		print '\nCache Address:', pc
		print 'Expect: [2, 0, 1]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		pc += 4	#120
		print '\nCache Address:', pc
		print 'Expect: [3, 0, 0]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		pc += 4	#124
		print '\nCache Address:', pc
		print 'Expect: [3, 0, 1]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		self.cbo.printCache()

		pc += 4	#128
		print '\nCache Address:', pc
		print 'Expect: [0, 0, 0]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		pc += 4	#132
		print '\nCache Address:', pc
		print 'Expect: [0, 0, 1]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		pc += 4	#136
		print '\nCache Address:', pc
		print 'Expect: [1, 1, 0]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		pc += 4	#140
		print '\nCache Address:', pc
		print 'Expect: [1, 1, 1]'
		cAddr = self.cbo.getCacheAddr(pc)
		print 'Result:', cAddr

		self.cbo.printCache()

		# Testing for invalid bits.  Won't be useful later in programming, as it 
		# will eventually automatically replace misses with data from memory.

		# pc += 4	#144
		# print '\nCache Address:', pc
		# print 'Expect: [None, None, None]'
		# cAddr = self.cbo.getCacheAddr(pc)
		# print 'Result:', cAddr

		# pc += 4	#148
		# print '\nCache Address:', pc
		# print 'Expect: [None, None, None]'
		# cAddr = self.cbo.getCacheAddr(pc)
		# print 'Result:', cAddr

		# Testing for invalid addresses.  Won't be useful later in programming, as it 
		# will eventually automatically replace misses with data from memory.

		# pc += 100
		# print '\nCache Address:', pc
		# print 'Expect: [None, None, None]'
		# cAddr = self.cbo.getCacheAddr(pc)
		# print 'Result:', cAddr

		self.cbo.printCache()
		pc = 104
		data = None

		print '\nData at address', pc
		print 'Expect: 1'
		data = self.cbo.getData(pc)
		print 'Result:', data

		pc += 4	# 108
		print '\nData at address', pc
		print 'Expect: 2'
		data = self.cbo.getData(pc)
		print 'Result:', data

		pc += 4 #112
		print '\nData at address', pc
		print 'Expect: 3'
		data = self.cbo.getData(pc)
		print 'Result:', data

		pc += 4 #116
		print '\nData at address', pc
		print 'Expect: 4'
		data = self.cbo.getData(pc)
		print 'Result:', data

		self.cbo.printCache()

		pc += 4
		print '\nData at address', pc
		print 'Expect: 5'
		data = self.cbo.getData(pc)
		print 'Result:', data

		pc += 4
		print '\nData at address', pc
		print 'Expect: 6'
		data = self.cbo.getData(pc)
		print 'Result:', data

		pc = 136
		print '\nData at address', pc
		print 'Expect: 9'
		data = self.cbo.getData(pc)
		print 'Result:', data

		pc += 4
		print '\nData at address', pc
		print 'Expect: 10'
		data = self.cbo.getData(pc)
		print 'Result:', data

		# Testing for invalid addresses.  Won't be useful later in programming, as it 
		# will eventually automatically replace misses with data from memory.

		pc += 4
		print '\nData at address', pc
		print 'Expect: None'
		data = self.cbo.getData(pc)
		print 'Result:', data




		# print '\nFABRICATED CACHE:'
		# self.cbo.fabTestCache()
		# self.cbo.printCache()

		# hit = [None, None, None]
		# truth = False
		# # Hit returns address: [setIndex, block, tag, blockOff]

		# print "\nHIT - 96"
		# print "Expect: True"
		# hit = self.cbo.getCacheAddr(96)
		# if hit[0] == None:
		# 	truth = False
		# else:
		# 	truth = True
		# print "Result:", truth
		
		# print "\nHIT - 100"
		# print "Expect: True"
		# hit = self.cbo.getCacheAddr(100)
		# if hit[0] == None:
		# 	truth = False
		# else:
		# 	truth = True
		# print "Result:", truth

		# print "\nHIT - 104"
		# print "Expect: True"
		# hit = self.cbo.getCacheAddr(104)
		# if hit[0] == None:
		# 	truth = False
		# else:
		# 	truth = True
		# print "Result:", truth

		# print "\nHIT - 108"
		# print "Expect: True"
		# hit = self.cbo.getCacheAddr(108)
		# if hit[0] == None:
		# 	truth = False
		# else:
		# 	truth = True
		# print "Result:", truth

		# print "\nHIT - 192"
		# print "Expect: True"
		# hit = self.cbo.getCacheAddr(192)
		# if hit[0] == None:
		# 	truth = False
		# else:
		# 	truth = True
		# print "Result:", truth

		# self.cbo.printCache()

		# print "\nHIT - 184"
		# print "Expect: False"
		# print "Why: not in cache"
		# hit = self.cbo.getCacheAddr(184)
		# if hit[0] == None:
		# 	truth = False
		# else:
		# 	truth = True
		# print "Result:", truth

		# self.cbo.printCache()

		# print "\nHIT - 200"
		# print "Expect: False"
		# print "Why: valid bit 0"
		# hit = self.cbo.getCacheAddr(200)
		# if hit[0] == None:
		# 	truth = False
		# else:
		# 	truth = True
		# print "Result:", truth

		# self.cbo.printCache()

		# print "\nHIT - 120"
		# print "Expect: False"
		# print "Why: valid bit 0"
		# hit = self.cbo.getCacheAddr(120)
		# if hit[0] == None:
		# 	truth = False
		# else:
		# 	truth = True
		# print "Result:", truth

		# print '\n>>> PHASE 3: Test fetching data from cache and updating LRU bit.'
		# print 'Unlike phase 2, this test will update the memory based on a test file,'\
		# 	'\ntestCache.txt, which is simply numbers 1 - 16, starting at memory'\
		# 	'\naddress 100.'

		# self.cbo.printCache()

		# self.cbo.testDataFetch(96, 501)
		# self.cbo.testDataFetch(100, 502)
		# self.cbo.testDataFetch(96, 501, 100, 502)
		# self.cbo.testDataFetch(192, 509)
		# self.cbo.testDataFetch(216, 515)

		# self.cbo.testDataFetch(200, 10)		# Previously 511 (word 0)
		# self.cbo.testDataFetch(212, 13)		# Previously 514 (word 1)
		# self.cbo.testDataFetch(120, 6, 124, 7)

		# print
		# self.cbo.clearCache()
		# self.cbo.printCache()

		# pc = 100
		# while pc < 224:
		# 	data = self.cbo.fetchData(pc)
		# 	print "\n>>> Data @ " + str(pc) + ": " + str(data)
		# 	pc += 4
		# 	self.cbo.printCache()


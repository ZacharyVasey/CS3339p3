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
		self.cbo = Cache()
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
		print '>>> PHASE 1: test correct index paced on provided PC.'

		self.cbo.printCache()
		setIndex = 0

		print '\nGet set index for 96  ~  ' + str(bin(96))
		print "Expect: 0"
		setIndex = self.cbo.getSetIndex(96)
		print "Result:", str(setIndex)

		print '\nGet set index for 100  ~  ' + str(bin(100))
		print "Expect: 0"
		setIndex = self.cbo.getSetIndex(100)
		print "Result:", str(setIndex)

		print '\nGet set index for 104  ~  ' + str(bin(104))
		print "Expect: 1"
		setIndex = self.cbo.getSetIndex(104)
		print "Result:", str(setIndex)

		print '\nGet set index for 108  ~  ' + str(bin(108))
		print "Expect: 1"
		setIndex = self.cbo.getSetIndex(108)
		print "Result:", str(setIndex)

		print '\nGet set index for 112  ~  ' + str(bin(112))
		print "Expect: 2"
		setIndex = self.cbo.getSetIndex(112)
		print "Result:", str(setIndex)

		print '\nGet set index for 116  ~  ' + str(bin(116))
		print "Expect: 2"
		setIndex = self.cbo.getSetIndex(116)
		print "Result:", str(setIndex)

		print '\nGet set index for 120  ~  ' + str(bin(120))
		print "Expect: 3"
		setIndex = self.cbo.getSetIndex(120)
		print "Result:", str(setIndex)

		print '\nGet set index for 124  ~  ' + str(bin(124))
		print "Expect: 3"
		setIndex = self.cbo.getSetIndex(124)
		print "Result:", str(setIndex)

		print '\nGet set index for 128  ~  ' + str(bin(128))
		print "Expect: 0"
		setIndex = self.cbo.getSetIndex(128)
		print "Result:", str(setIndex)

		print '\nGet set index for 132  ~  ' + str(bin(132))
		print "Expect: 0"
		setIndex = self.cbo.getSetIndex(132)
		print "Result:", str(setIndex)

		print '\nGet set index for 136  ~  ' + str(bin(136))
		print "Expect: 1"
		setIndex = self.cbo.getSetIndex(136)
		print "Result:", str(setIndex)

		print '\nGet set index for 140  ~  ' + str(bin(140))
		print "Expect: 1"
		setIndex = self.cbo.getSetIndex(140)
		print "Result:", str(setIndex)

		print '\n>>> PHASE 2: Test hitting (or missing) memory addresses in fabricated cache.'\
			'\nThis does NOT test data at the provided address, nor updating via memory at the'\
			'\nprovided address.  This simply tests if the provided address EXISTS in cache or not.'

		print '\nFABRICATED CACHE:'
		self.cbo.fabTestCache()
		self.cbo.printCache()

		hit = [None, None, None]
		truth = False
		# Hit returns address: [setIndex, block, tag, blockOff]

		print "\nHIT - 96"
		print "Expect: True"
		hit = self.cbo.isHit(96)
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Result:", truth
		
		print "\nHIT - 100"
		print "Expect: True"
		hit = self.cbo.isHit(100)
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Result:", truth

		print "\nHIT - 104"
		print "Expect: True"
		hit = self.cbo.isHit(104)
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Result:", truth

		print "\nHIT - 108"
		print "Expect: True"
		hit = self.cbo.isHit(108)
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Result:", truth

		print "\nHIT - 192"
		print "Expect: True"
		hit = self.cbo.isHit(192)
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Result:", truth

		self.cbo.printCache()

		print "\nHIT - 184"
		print "Expect: False"
		print "Why: not in cache"
		hit = self.cbo.isHit(184)
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Result:", truth

		print "\nHIT - 200"
		print "Expect: False"
		print "Why: valid bit 0"
		hit = self.cbo.isHit(200)
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Result:", truth

		print "\nHIT - 120"
		print "Expect: False"
		print "Why: valid bit 0"
		hit = self.cbo.isHit(120)
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Result:", truth

		print '\n>>> PHASE 3: Test fetching data from cache.'
		print 'Unlike phase 2, this test will update the memory based on a test file,'\
			'\ntestCache.txt, which is simply numbers 1 - 16, starting at memory'\
			'\naddress 96.'

		self.cbo.printCache()

		data = None
		print "\nDATA @ 96"
		print "Expect: 1"
		data = self.cbo.getData(96)
		print "Result:", data

		print "\nDATA @ 100"
		print "Expect: 2"
		data = self.cbo.getData(100)
		print "Result:", data

		print "\nDATA @ 104"
		print "Expect: 3"
		data = self.cbo.getData(104)
		print "Result:", data

		print "\nDATA @ 108"
		print "Expect: 4"
		data = self.cbo.getData(108)
		print "Result:", data

		print "\nDATA @ 192"
		print "Expect: 9"
		data = self.cbo.getData(192)
		print "Result:", data

		print "\nDATA @ 196"
		print "Expect: 10"
		data = self.cbo.getData(196)
		print "Result:", data

		self.cbo.printCache()

		print "\nDATA @ 200"
		print "Expect: None"
		data = self.cbo.getData(200)
		print "Result:", data

		print "\nDATA @ 204"
		print "Expect: None"
		data = self.cbo.getData(204)
		print "Result:", data

		print "\nDATA @ 1024"
		print "Expect: None"
		data = self.cbo.getData(1024)
		print "Result:", data

		print '\n>>> PHASE 4: Test updating cache.'

	if __name__== "__main__":
		main()
		print
		print

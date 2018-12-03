##################################################################################
#    Class Simulator
##################################################################################
import copy
from reg import RegFile
class Simulator(object):
	
	def __init__(self, opCodeStr, isInstr, insType, data, rmRegNum, shamNum, rnRegNum, rdRtRegNum, immNum,
	             addrNum, shiftNum, litInstr, memLines, numLinesText, regFile):
		# Set up cycle sequence list.
		self.cycles = []  # Holds list of cycles, each with state data.  Each CC results in new cycle.
		# Set up BinData column copies.
		self.opCodeStr = opCodeStr
		self.isInstr = isInstr
		self.insType = insType
		self.data = data
		self.rmRegNum = rmRegNum
		self.shamNum = shamNum
		self.rnRegNum = rnRegNum
		self.rdRtRegNum = rdRtRegNum
		self.immNum = immNum
		self.addrNum = addrNum
		self.shiftNum = shiftNum
		self.litInstr = litInstr
		self.memLines = memLines
		self.numLinesText = numLinesText
		self.regFile = regFile
	###############################################################################
	#   Class Cycle:  a single cycle, and the register/data states at that time.
	###############################################################################
	# NESTED CLASS
	class Cycle(object):
		def __init__(self):
			self.PC = 0
			self.litIns = ''
			self.regState = [0] * 32
			self.datState = []
			self.datStart = 0
	
	###############################################################################
	###############################################################################
	def doADD(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		# print '\tInside doADD - memLines[x]:', self.memLines[x]     # TESTPRINT
		# print 'Testing ADD'             #TESTPRINT
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		# print '\trd:', self.rd          #TESTPRINT
		self.rn = self.rnRegNum[x]  # Get op1 register number.
		# print '\trn:', self.rn          #TESTPRINT
		self.rnVal = self.nextCyc.regState[self.rn]  # Get op1 value.
		# print '\trnVal:', self.rnVal    #TESTPRINT
		self.rm = self.rmRegNum[x]  # Get op2 register number.
		# print '\trm:', self.rm          #TESTPRINT
		self.rmVal = self.nextCyc.regState[self.rm]  # Get op2 value.
		# print '\trmVal:', self.rmVal    #TESTPRINT
		self.rdVal = self.rnVal + self.rmVal  # Get value to save to register.
		# print '\trdVal:', self.rdVal    #TESTPRINT
		nc.regState[self.rd] = self.rdVal
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.rdVal
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	
	###############################################################################
	###############################################################################
	def doSUB(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		self.rn = self.rnRegNum[x]  # Get op1 register number.
		self.rnVal = self.nextCyc.regState[self.rn]  # Get op1 value.
		self.rm = self.rmRegNum[x]  # Get op2 register number.
		self.rmVal = self.nextCyc.regState[self.rm]  # Get op2 value.
		self.rdVal = self.rnVal - self.rmVal  # Get value to save to register.
		nc.regState[self.rd] = self.rdVal
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.rdVal
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doLSL(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		# print 'Testing LSL...'          #TESTPRINT
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		# print '\trd:', self.rd          #TESTPRINT
		self.rn = self.rnRegNum[x]  # Get src register number.
		# print '\trn:', self.rn          #TESTPRINT
		self.rnVal = self.nextCyc.regState[self.rn]  # Get src value.
		# print '\trnVal:', self.rnVal    #TESTPRINT
		self.shiftVal = self.shamNum[x]  # Get shift amount.
		# print '\tshiftVal:', self.shiftVal  #TESTPRINT
		# regState[arg1] = (regState[arg2] % (1 << 64)) << shift Code from power point
		self.rdVal = (self.rnVal % (1 << 64)) << self.shiftVal
		# print '\trdVal:', self.rdVal        #TESTPRINT
		nc.regState[self.rd] = self.rdVal
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.rdVal
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doLSR(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		self.rn = self.rnRegNum[x]  # Get src register number.
		self.rnVal = self.nextCyc.regState[self.rn]  # Get src value.
		self.shiftVal = self.shamNum[x]  # Get shift amount.
		# regState[arg1] = (regState[arg2] % (1 << 64)) << shift
		self.rdVal = (self.rnVal % (1 << 64)) >> self.shiftVal
		nc.regState[self.rd] = self.rdVal
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.rdVal
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doAND(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		# print 'Testing AND...'              # TESTPRINT
		self.rd = self.rdRtRegNum[x]
		self.rdVal = self.nextCyc.regState[self.rd]
		# print '\trd:', self.rd              # TESTPRINT
		# print '\trdVal:', self.rdVal        # TESTPRINT
		self.rn = self.rnRegNum[x]
		# print '\trn:', self.rn              # TESTPRINT
		self.rnVal = self.nextCyc.regState[self.rn]
		# print '\trnVal:', bin(self.rnVal)   # TESTPRINT
		self.rm = self.rmRegNum[x]
		# print '\trm:', self.rm              # TESTPRINT
		self.rmVal = self.nextCyc.regState[self.rm]
		# print '\trmVal:', bin(self.rmVal)        # TESTPRINT
		self.thisNum = self.rmVal & self.rnVal
		# print '\trdVal:', self.thisNum      # TESTPRINT
		nc.regState[self.rd] = self.thisNum
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.thisNum
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doORR(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]
		self.rdVal = self.nextCyc.regState[self.rd]
		self.rn = self.rnRegNum[x]
		self.rnVal = self.nextCyc.regState[self.rn]
		self.rm = self.rmRegNum[x]
		self.rmVal = self.nextCyc.regState[self.rm]
		self.thisNum = self.rmVal | self.rnVal
		nc.regState[self.rd] = self.thisNum
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.thisNum
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doEOR(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]
		self.rdVal = self.nextCyc.regState[self.rd]
		self.rn = self.rnRegNum[x]
		self.rnVal = self.nextCyc.regState[self.rn]
		self.rm = self.rmRegNum[x]
		self.rmVal = self.nextCyc.regState[self.rm]
		self.thisNum = self.rmVal ^ self.rnVal
		nc.regState[self.rd] = self.thisNum
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.thisNum
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doASR(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.rd = self.rdRtRegNum[x]  # Get dest register number.
		self.rn = self.rnRegNum[x]  # Get src register number.
		self.rnVal = self.nextCyc.regState[self.rn]  # Get src value.
		self.shiftVal = self.shamNum[x]  # Get shift amount.
		self.rdVal = self.rnVal >> self.shiftVal
		nc.regState[self.rd] = self.rdVal
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.rdVal
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doADDI(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		# print 'Cycle ' + str(x + 1) + ':   ' + self.litInstr[x]  # TESTPRINT
		# print '\tInside doADD...'       # TESTPRINT
		# print '\t\tmemLines[x]:', self.memLines[x]  # TESTPRINT
		# Get immediate value.
		self.immVal = self.immNum[x]
		# print 'imm: ' + str(self.immVal)  # TESTPRINT
		# Get dest register number and value.
		self.rd = self.rdRtRegNum[x]
		# print 'rd: ' + str(self.rd)  # TESTPRINT
		# print 'rdVal: ' + str(self.nextCyc.regState[self.rd])  # TESTPRINT
		# Get src register value.
		self.rn = self.rnRegNum[x]
		# print 'rn: ' + str(self.rn)  # TESTPRINT
		self.rnVal = nc.regState[self.rn]
		# print 'rnVal: ' + str(self.nextCyc.regState[self.rn])    # TESTPRINT
		# Do the math:  rd = rn + imm
		# There's a lot going on here:  The current cycle (nextCyc) has 32 register files: regState[].
		# We want a specific dest register, IDed by rdRtRegNum[x]:  self.nextCyc.regState[self.rdRtRegNum[x]]
		# One of the operands is currently stored in the register file.  We get that specific src register the
		# same way.  In nextCyc, we need a specific register of the 32, IDed by rnRegNum[].
		# Finally, we have the easy immediate: NOT in a register file, but in immNum[].
		nc.regState[self.rd] = self.rnVal + self.immVal
		# print '\t\tnc.PC:', nc.PC   # TESTPRINT
		# print '\t\tself.nextCyc.PC:', self.nextCyc.PC       # TESTPRINT
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.rnVal + self.immVal
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doSUBI(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		self.immVal = self.immNum[x]
		# print 'imm: ' + str(self.immVal)  # TESTPRINT
		self.rd = self.rdRtRegNum[x]
		# print 'rd: ' + str(self.rd)  # TESTPRINT
		# print 'rdVal: ' + str(self.nextCyc.regState[self.rd])  # TESTPRINT
		self.rn = self.rnRegNum[x]
		# print 'rn: ' + str(self.rn)  # TESTPRINT
		self.rnVal = self.nextCyc.regState[self.rn]
		nc.regState[self.rd] = self.rnVal - self.immVal
		nc.litIns = self.litInstr[x]
		
		self.regFile.regFileList[self.rd] = self.rnVal - self.immVal
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doLDUR(self, nc, x):
		# print 'INSIDE LDUR...'
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		rn = self.rnRegNum[x]  # Base Address in Register #
		# print '\trn:', rn
		rnVal = nc.regState[rn]  # Base Address is...
		# print '\trnVal:', rnVal
		addr = self.addrNum[x]  # Offset
		# print '\taddr:', addr
		memAdr = (addr * 4) + rnVal
		datAdr = memAdr - nc.datStart
		datAdr /= 4
		# print '\tdatAdr:  ', datAdr
		
		# dataIndex = ((nc.datStart   - rnVal + addr) / 4)  # Fancy doings.
		# print '\t(datStart - rnVal):', (nc.datStart - rnVal)
		# print '\tdatStart:', nc.datStart
		# print '\tdataIndex:', dataIndex
		# print '\tcontents datState[datIndex]:  ', nc.datState[dataIndex]
		# print '\tcontents datState[37]:  ', nc.datState[37]
		
		testBound = datAdr > len(nc.datState) - 1
		if not testBound:
			load = nc.datState[datAdr]
			# print '\tload: ', load      # TESTPRINT
			# print '\tload:', load
			rd = self.rdRtRegNum[x]
			nc.regState[rd] = load
			nc.litIns = self.litInstr[x]
			
			self.regFile.regFileList[rd] = load
		else:
			popNum = datAdr - len(nc.datState)
			for x in range(0, popNum):
				nc.datState.append(0)
			load = nc.datState[datAdr]
			# print '\tload: ', load  # TESTPRINT
			rd = self.rdRtRegNum[x]
			nc.regState[rd] = load
			nc.litIns = self.litInstr[x]
			
			self.regFile.regFileList[rd] = load
			# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
			# for el in self.regFile.regFileList:
			# 	print el, '  ',
	
	###############################################################################
	###############################################################################
	def doSTUR(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		rd = self.rdRtRegNum[x]  # src register
		rdVal = nc.regState[rd]  # store
		rn = self.rnRegNum[x]  # base reg
		rnVal = nc.regState[rn]  # base addr
		addr = self.addrNum[x]  # offset
		dataIndex = ((nc.datStart - rnVal + addr) / 4)  # Fancy doings.
		# FANCIER DOINGS
		memIndex = rnVal + (addr * 4)
		# print 'memIndex:', memIndex
		datIndexEnd = (memIndex - nc.datStart) / 4
		# print 'datIndexEnd:', datIndexEnd
		
		#TESPRINT
		# print 'self.litInstr:  ', self.litInstr[x]
		# print 'DOSTUR', '  ', nc.PC
		# print 'pc:', nc.PC
		# print 'datStart:', nc.datStart
		# print 'baseAddress:', rnVal
		# print "dataIndex: ", dataIndex
		# print 'offset:', addr
		# print "Size of nc.datState[]", len(nc.datState)
		
		testBound = datIndexEnd > len(nc.datState) - 1
		if not testBound:
			nc.datState[dataIndex] = rdVal
			nc.litIns = self.litInstr[x]
		else:
			popNum = datIndexEnd - len(nc.datState) + 1
			# print '\tpopNum:', popNum                       #TESPRINT
			# print '\trdVal:', rdVal                         #TESPRINT
			nc.litIns = self.litInstr[x]
			for x in range(0, popNum):
				nc.datState.append(0)
			nc.datState[datIndexEnd] = rdVal
			

	###############################################################################
	###############################################################################
	def doCBZ(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		rd = self.rdRtRegNum[x]
		rdVal = nc.regState[rd]
		addr = self.addrNum[x]
		nc.litIns = self.litInstr[x]
		# print 'Testing CBZ...'
		# print '\tpc:', nc.PC
		# print '\trd:', rd
		# print '\trdVal:', rdVal
		# print '\taddr:', addr
		# addr *= 4
		# print '\taddr *= 4:', addr
		if rdVal == 0:  # If test value == 0, return the offset to adjust the instruction index.
			return addr
		else:
			return 0
	
	###############################################################################
	###############################################################################
	def doMOVZ(self, nc, x):
		rd = self.rdRtRegNum[x]
		nc.PC += 4
		nc.litIns = self.litInstr[x]
		nc.regState[rd] = 0
		nc.regState[rd] = self.immNum[x] * (2 ** self.shiftNum[x])
		
		self.regFile.regFileList[rd] = self.immNum[x] * (2 ** self.shiftNum[x])
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	###############################################################################
	###############################################################################
	def doMOVK(self, nc, x):
		nc.PC += 4
		BIT_MASK_0 = 0xFFFFFFFFFFFF0000
		BIT_MASK_1 = 0xFFFFFFFF0000FFFF
		BIT_MASK_2 = 0xFFFF0000FFFFFFFF
		BIT_MASK_3 = 0x0000FFFFFFFFFFFF
		rd = self.rdRtRegNum[x]
		nc.litIns = self.litInstr[x]
		if (self.shiftNum[x] == 0):
			nc.regState[rd] = nc.regState[rd] & BIT_MASK_0
			self.regFile.regFileList[rd] = regFile.regFileList[rd] & BIT_MASK_0
			print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
			for el in self.regFile.regFileList:
				print el, '  ',
		elif (self.shiftNum[x] == 1):
			nc.regState[rd] = nc.regState[rd] & BIT_MASK_1
			self.regFile.regFileList[rd] = regFile.regFileList[rd] & BIT_MASK_1
			print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
			for el in self.regFile.regFileList:
				print el, '  ',
		elif (self.shiftNum[x] == 2):
			nc.regState[rd] = nc.regState[rd] & BIT_MASK_2
			self.regFile.regFileList[rd] = regFile.regFileList[rd] & BIT_MASK_2
			print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
			for el in self.regFile.regFileList:
				print el, '  ',
		else:
			nc.regState[rd] = nc.regState[rd] & BIT_MASK_3
			self.regFile.regFileList[rd] = regFile.regFileList[rd] & BIT_MASK_3
			print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
			for el in self.regFile.regFileList:
				print el, '  ',
		# TESPRINT
		# print "shift num: ", self.shiftNum[x]
		nc.regState[rd] = nc.regState[rd] + (self.immNum[x] * (2 ** self.shiftNum[x]))
		
		self.regFile.regFileList[rd] = regFile.regFileList[rd] + (self.immNum[x] * (2 ** self.shiftNum[x]))
		# # TESPRINT
		# print '\nCYCLE: ' + str(nc.PC) + '     ' + 'INS: ' + self.litInstr[x]
		# for el in self.regFile.regFileList:
		# 	print el, '  ',
	
	###############################################################################
	###############################################################################
	def doCBNZ(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		rd = self.rdRtRegNum[x]
		rdVal = nc.regState[rd]
		addr = self.addrNum[x]
		nc.litIns = self.litInstr[x]
		# print 'Testing CBNZ...'
		# print '\tpc:', nc.PC
		# print '\trd:', rd
		# print '\trdVal:', self.rdVal
		# print '\taddr:', addr
		# addr *= 4
		# print '\taddr *= 4:', addr
		if rdVal != 0:  # If test value != 0, return the offset to adjust the instruction index.
			return addr
		else:
			return 0
	
	###############################################################################
	###############################################################################
	def doNOP(self, nc, x):
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		nc.litIns = self.litInstr[x]
	
	# TESTPRINT
	# print 'nextCyc.regState[self.rd]: ' + str(self.nextCyc.regState[self.rd])
	###############################################################################
	###############################################################################
	def doB(self, nc, x):
		nc.PC = self.memLines[x]
		nc.litIns = self.litInstr[x]
		addr = self.addrNum[x]
		return addr
	
	###############################################################################
	###############################################################################
	def doBREAK(self, nc, x):
		nc.PC = self.memLines[x]
		nc.litIns = self.litInstr[x]
	
	def writeOut(self, binData):
		outFile = open(binData.outFile, 'w')
		outFile.write(binData.finalText)
		outFile.close()
	###############################################################################
	#   run:  operates the simulator, which processes each instruction, one cycle
	#   at a time.  Makes copy of old cycle[i - 1], modifies that copy, and then
	#   saves it to the list of cycles.
	###############################################################################
	# FUNCTIONS
	def run(self, binData):
		# print "\n>>>>>>>>>>> INSIDE SIMULATOR.run(): YOU WILL BE SIMULATED >>>>>>>>>>>>>>>>> "  # TESTPRINT
		self.nextCyc = self.Cycle()  # Create first EMPTY cycle (empty regState[]).  Not appended to cycles[].
		
		# Grab memory start address.
		for y, ins in enumerate(self.opCodeStr):
			if self.insType[y] == 'DATA':
				self.nextCyc.datStart = self.memLines[y]
				break
		# print 'datStart:', self.nextCyc.datStart        # TESTPRINT
		# Load memory data in first iteration of cycles.  (Only data load, until later instructions.)
		for y, ins in enumerate(self.opCodeStr):
			if self.insType[y] == 'DATA':
				self.nextCyc.datState.append(self.data[y])
		# print 'nextCyc.datState[]...' #TESTPRINT
		# for x in self.nextCyc.datState:
		# 	print x,
		print
		
		# Load cycles[]
		self.x = 0
		while (self.x < self.numLinesText):
			# print 'In while loop...', self.x, ' ... ', self.litInstr[self.x], ' ... ', self.memLines[self.x]
			self.nextCyc = copy.deepcopy(self.nextCyc)
			######################################## R
			if self.opCodeStr[self.x] == 'ADD':
				self.doADD(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'SUB':
				self.doSUB(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'LSL':
				self.doLSL(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'LSR':
				self.doLSR(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'AND':
				self.doAND(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'ORR':
				self.doORR(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'EOR':
				self.doEOR(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'ASR':
				self.doASR(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			######################################## D
			elif self.opCodeStr[self.x] == 'LDUR':
				self.doLDUR(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'STUR':
				self.doSTUR(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			######################################## I
			elif self.opCodeStr[self.x] == 'ADDI':
				self.doADDI(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'SUBI':
				self.doSUBI(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			######################################## IM
			elif self.opCodeStr[self.x] == 'MOVK':
				self.doMOVK(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'MOVZ':
				self.doMOVZ(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			######################################## CB
			elif self.opCodeStr[self.x] == 'CBNZ':
				y = self.doCBNZ(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
				# print 'Inside CBNZ...'
				# print '\ty:', y
				# print '\ty += x:', y + self.x
				if y != 0:
					self.x += y
					continue
			# else:
			# 	print 'y == 0'
			elif self.opCodeStr[self.x] == 'CBZ':
				y = self.doCBZ(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
				# print 'Inside CBZ...'
				# print '\ty:', y
				# print '\ty += x:', y + self.x
				if y != 0:
					self.x += y
					continue
			# else:
			# print 'y == 0'
			######################################## B
			elif self.opCodeStr[self.x] == 'B':
				y = self.doB(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
				self.x += y
				continue
			######################################## MISC
			elif self.opCodeStr[self.x] == 'NOP':
				self.doNOP(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
			elif self.opCodeStr[self.x] == 'BREAK':
				self.doBREAK(self.nextCyc, self.x)
				self.cycles.append(self.nextCyc)
				break
			self.x += 1
		
		# TEST RUN() DOWN HERE
		self.printCycles(binData)
		#print "\n>>>>>>>>>>> EXITING SIMULATOR.run(): YOU HAVE BEEN SIMULATED >>>>>>>>>>>>>>>>> \n"  # TESPRINT
	
	def printCycle(self, clockCycle, binData):
		'Takes an element in the cycle Register and prints it.'
		# print
		# print '======================================================================='
		binData.finalText += '=======================================================================' + "\n"
		# print 'Cycle ' + str(clockCycle + 1) + ':  ' + str(self.cycles[clockCycle].PC) + \
		#       '\t\t' + self.cycles[clockCycle].litIns
		binData.finalText += 'Cycle ' + str(clockCycle + 1) + ':  ' + str(self.cycles[clockCycle].PC) + '\t\t' + self.cycles[clockCycle].litIns + "\n"
		# print '\nRegisters:'
		binData.finalText += '\nRegisters:' + "\n"
		z = 0
		for x in range(0, 4):  # Prints all registers 4 rows x 8 columns
			line = 'r' + str(z).zfill(2) + ':\t'
			for y in range(0, 8):
				line += str(self.cycles[clockCycle].regState[y + z]) + '\t'
			# print line
			binData.finalText += line + "\n"
			z += 8

		# print '\nData:'
		binData.finalText += '\nData:' + "\n"
		datStart = self.cycles[0].datStart
		header = str(datStart) + ':\t'
		y = 0
		for x, d in enumerate(self.cycles[clockCycle].datState):
			if ((x != 0) & (x % 8 == 0)):
				y += 1
				header += '\n' + str(datStart + (y * 32)) + ':\t'
			header += str(d) + '\t'
		# print header
		binData.finalText += header + "\n"
	
	def printCycles(self, binData):
		binData.finalText = ''
		for x, cycle in enumerate(self.cycles):
			self.printCycle(x, binData)
		self.writeOut(binData)

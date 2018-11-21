##################################################################################
#    Class BinData
##################################################################################
class BinData(object):
	def __init__(self):
		# FILE DATA
		self.inFile = ''     # Holds name of input file (via command line).
		self.outFile = ''     # Holds name of output file (via command line).
		self.finalText = ''     # Holds final text to write out to file.
		self.machineCodeFile = ''     # Holds name of string of all binary data from input file.
		self.numLinesText = 0   # Holds the number of lines in binary text file.
		self.PC = 96      # Holds beginning of memory address.
		# MASK DATA
		self.rmMask = 0x1F0000  # Mask to extract Rn register (R1)
		self.rnMask = 0x3E0     # Mask to extract Rd register (R2)
		self.rdMask = 0x1F      # Mask to extract Rm register (R3)
		self.shamMask = 0xFC00  # Mask to extract shamt register.
		self.imm_IM = 0x1FFFE0   # Mask to extract immediate from IM-format instruction.
		self.immI = 0x3FFC00    # Mask to extract immediate from I-format instruction.
		self.addrD = 0x1FF000   # Mask to extract address from D-format instruction.
		self.addrCB = 0xFFFFE0  # Mask to extract address from CB-format instruction.
		self.addrB = 0x3FFFFFF  # Mask to extract address from B-format instruction.
		self.shiftMask = 0x600000   # Mask to extract shift.
		# LIST DATA
		self.machineLines = []  # Holds RAW lines of binary text file, WITHOUT '\n' and '\t'
		self.instrSpaced = []   # Holds formatted lines of binary lines.
		self.opCodeStr = []     # Holds strings of opcodes, empty if data.
		self.isInstr = []       # Holds whether each column is instruction or data.
		self.insType = []       # Holds either: type of instruction (R, I, D, CB, IM, B, BREAK, NOP
		self.data = []          # Holds decimal value for data, empty if instruction.
		self.rmRegNum = []      # Holds register nums for Rm portion, empty if doesn't exist in instruction.
		self.shamNum = []       # Holds register nums for shamt portion, empty if doesn't exist in instruction.
		self.rnRegNum = []      # Holds register nums for Rn portion, empty if doesn't exist in instruction.
		self.rdRtRegNum = []      # Holds register nums for Rd/Rt portion, empty if doesn't exist in instruction.
		self.immNum = []        # Holds immediate value in instruction.
		self.addrNum = []       # Holds numeric address in instruction.
		self.shiftNum = []      # Holds shift in instruction.
		self.memLines = []      # Holds memory address of each line.
		self.litInstr = []      # Holds literal instructions or literal data (human readable).


##################################################################################
#    Class Dissemble
##################################################################################
class Dissemble(object):
	def __init__(self):
		'TESTPRINT:  this is my dissemble documentation.'
	
	##################################################################################
	#   openRead:  Opens binary text file and raw loads lines of binary code
	#   into machineCode list.
	##################################################################################
	def openRead(self, binData):  # Opens file and reads binary lines into list.
		with open(binData.inFile) as binData.machineCodeFile:  # 18-20 read in lines WITHOUT tabs.
			binData.machineLines = binData.machineCodeFile.readlines()
		binData.machineLines = [x.strip() for x in binData.machineLines]
		# TESTPRINT
		# print
		# print 'Testing openRead()...' + '\ninFile: ' + binData.inFile
		# print 'machineCode[]: '
		# for item in binData.machineLines:  # Print all raw binary lines in machineLines[].
		# 	print item
		binData.machineCodeFile.close()  # Clean up.
	
	##################################################################################
	#   processElvBits:  Takes 1st 11 bits of each line.  Tests for
	#   opcode via range.  Populates opcode string list, instruction type list,
	#   and data type list.  If line has no instruction type, then instruction type
	#   list left empty to maintain column integrity - and vice versa.
	##################################################################################
	def processElvBits(self, binData):
		# TESTPRINT
		# print
		# print 'Testing processLinesBin()...'
		# print 'First eleven bits, binary & decimal:'
		k = binData.PC
		for line in binData.machineLines:
			# Count lines
			binData.numLinesText += 1
			# Populate memory.
			binData.memLines.append(k)
			# Get the first bits in bin & dec.
			elvBin = line[0:11]
			elvDec = int(elvBin, 2)
			# TESTPRINT
			# print elvBin + '  -  '  + str(elvDec)
			if (elvDec >= 160 and elvDec <= 191):
				binData.isInstr.append(True)
				binData.opCodeStr.append("B")
				binData.insType.append("B")
				binData.data.append('')
			elif (elvDec == 1104):
				binData.isInstr.append(True)
				binData.opCodeStr.append("AND")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1112):
				binData.isInstr.append(True)
				binData.opCodeStr.append("ADD")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1160 or elvDec == 1161):
				binData.isInstr.append(True)
				binData.opCodeStr.append("ADDI")
				binData.insType.append("I")
				binData.data.append('')
			elif (elvDec == 1360):
				binData.isInstr.append(True)
				binData.opCodeStr.append("ORR")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == elvDec >= 1440 and elvDec <= 1447):
				binData.isInstr.append(True)
				binData.opCodeStr.append("CBZ")
				binData.insType.append("CB")
				binData.data.append('')
			elif (elvDec >= 1448 and elvDec <= 1455):
				binData.isInstr.append(True)
				binData.opCodeStr.append("CBNZ")
				binData.insType.append("CB")
				binData.data.append('')
			elif (elvDec == 1624):
				binData.isInstr.append(True)
				binData.opCodeStr.append("SUB")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1872):
				binData.isInstr.append(True)
				binData.opCodeStr.append("EOR")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1672 or elvDec == 1673):
				binData.isInstr.append(True)
				binData.opCodeStr.append("SUBI")
				binData.insType.append("I")
				binData.data.append('')
			elif (elvDec >= 1684 and elvDec <= 1687):
				binData.isInstr.append(True)
				binData.opCodeStr.append("MOVZ")
				binData.insType.append("IM")
				binData.data.append('')
			elif (elvDec >= 1940 and elvDec <= 1943):
				binData.isInstr.append(True)
				binData.opCodeStr.append("MOVK")
				binData.insType.append("IM")
				binData.data.append('')
			elif (elvDec == 1690):
				binData.isInstr.append(True)
				binData.opCodeStr.append("LSR")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1691):
				binData.isInstr.append(True)
				binData.opCodeStr.append("LSL")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1692):
				binData.isInstr.append(True)
				binData.opCodeStr.append("ASR")
				binData.insType.append("R")
				binData.data.append('')
			elif (elvDec == 1984):
				binData.isInstr.append(True)
				binData.opCodeStr.append("STUR")
				binData.insType.append("D")
				binData.data.append('')
			elif (elvDec == 1986):
				binData.isInstr.append(True)
				binData.opCodeStr.append("LDUR")
				binData.insType.append("D")
				binData.data.append('')
			elif (elvDec == 2038):
				binData.isInstr.append(True)
				binData.opCodeStr.append("BREAK")
				binData.insType.append("BREAK")
				binData.data.append('')
			# At this point no ops have been found to match ranges.
			elif (True):
				# Checking if entire line == 0 (NOP)
				if (int(line, 2) == 0):
					# print "NOP @ line #" + str(k)
					binData.isInstr.append(True)
					binData.opCodeStr.append("NOP")
					binData.insType.append("NOP")
					binData.data.append('')
				# If line has no matching op, but != 0, then its data.
				else:
					# print "Data @ line #" + str(k)
					binData.isInstr.append(False)
					binData.opCodeStr.append('')
					binData.insType.append("DATA")
					binData.data.append('')
			else:
				print "You shouldn't have come this far."
			k += 4
	
	# TESTPRINT
	# print 'isInstr[]:  '
	# print binData.isInstr
	# print 'opCodeStr[]:  '
	# print binData.opCodeStr
	# print 'data[]:'
	# print binData.data
	# print 'insType[]: '
	# print binData.insType
	# print 'number of lines in machineLines: ' + str(binData.numLinesText)
	# print 'memory in memLines[]: ' + str(binData.memLines)
	##################################################################################
	#   processRegs:  Uses masks and instruction types to populate the register lists.
	#   Nonexistent registers left empty in their respective list elements.
	##################################################################################
	def processRegs(self, binData):
		# TESTPRINT
		# print
		# print 'Testing processRegs()...'
		k = 0
		for line in binData.machineLines:
			# Grab binary line.
			tempBin = int(line, base=2)
			# Get Rm
			rmNum = ((tempBin & binData.rmMask) >> 16)
			# Get sham
			# Get sham
			shamNum = ((tempBin & binData.shamMask) >> 10)
			# Get Rn
			rnNum = ((tempBin & binData.rnMask) >> 5)
			# Get Rd/Rt
			rdRtNum = ((tempBin & binData.rdMask) >> 0)
			# Get Immediate (I-format)
			immI = ((tempBin & binData.immI) >> 10)
			# Get Immediate (IM-format)
			immIM = ((tempBin & binData.imm_IM) >> 5)
			# Get Addr (D-Format)
			adD = ((tempBin & binData.addrD) >> 12)
			# Get Addr (CB-Format)
			adCB = ((tempBin & binData.addrCB) >> 5)
			# Get Addr (B-Format)
			adB = ((tempBin & binData.addrB) >> 0)
			# Get op2
			# Get Shift
			shiftNum = ((tempBin & binData.shiftMask) >> 21)
			# Test for R-Format
			if (binData.insType[k] == 'R'):
				binData.rmRegNum.append(rmNum)
				binData.rnRegNum.append(rnNum)
				binData.rdRtRegNum.append(rdRtNum)
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				if (shamNum != 0):
					binData.shamNum.append(shamNum)
				else:
					binData.shamNum.append('')
			# Test for I-Format
			elif (binData.insType[k] == "I"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append(rnNum)
				binData.rdRtRegNum.append(rdRtNum)
				# Determine if imm is +/-
				testBit = immI >> 11  # Grab leftmost bit of imm.
				if (testBit == 0):
					binData.immNum.append(int(immI))
				else:
					immI = immI - 1
					immI = immI ^ 0xFFF
					immI = int(immI) * -1
					binData.immNum.append(int(immI))
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for D-Format
			elif (binData.insType[k] == "D"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append(rnNum)
				binData.rdRtRegNum.append(rdRtNum)
				binData.immNum.append('')
				binData.addrNum.append(adD)
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for CB-Format
			elif (binData.insType[k] == "CB"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append(rdRtNum)
				binData.immNum.append('')
				testBit = adCB >> 18
				if (testBit == 0):
					binData.addrNum.append(adCB)
				else:
					adCB = adCB - 1
					adCB = adCB ^ 0b1111111111111111111
					adCB = int(adCB) * -1
					binData.addrNum.append(adCB)
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for IM-Format
			elif (binData.insType[k] == "IM"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append(rdRtNum)
				binData.immNum.append(immIM)
				binData.addrNum.append('')
				# Test for proper quadrant of movk, movz:
				if (shiftNum == 0):
					binData.shiftNum.append(0)
				elif (shiftNum == 1):
					binData.shiftNum.append(16)
				elif (shiftNum == 2):
					binData.shiftNum.append(32)
				else:
					binData.shiftNum.append(48)
				binData.shamNum.append('')
			# Test for B-Format
			elif (binData.insType[k] == "B"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				# TESTPRINT
				# print "   adB: "
				# print bin(adB)
				testBit = adB >> 24
				if (testBit == 0):
					binData.addrNum.append(adB)
				else:
					# TESTPRINT
					# print "   neg adB: " + str(bin(adB))
					adB = adB - 1
					# print "   neg adB - 1: " + str(bin(adB))
					adB = adB ^ 0b11111111111111111111111111
					# print "   neg adB ^ F: " + str(bin(adB))
					adB = int(adB) * -1
					binData.addrNum.append(adB)
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for BREAK
			elif (binData.insType[k] == "BREAK"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for NOP
			elif (binData.insType[k] == "NOP"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
			# Test for Data
			elif (binData.insType[k] == "DATA"):
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
				testBin = tempBin >> 31
				# If data is negative.
				if (testBin == 1):
					twoC = (0xFFFFFFFF ^ tempBin) + 1
					dataVal = int(twoC) * -1
					binData.data[k] = dataVal
				# If data is positive...
				else:
					# TESTPRINT
					# print "Positive data at line #" + str(binData.memLines[k])
					binData.data[k] = int(line, 2)
			else:
				print "Error: unknown data type."
				binData.rmRegNum.append('')
				binData.rnRegNum.append('')
				binData.rdRtRegNum.append('')
				binData.immNum.append('')
				binData.addrNum.append('')
				binData.shiftNum.append('')
				binData.shamNum.append('')
			k += 1
	
	##################################################################################
	#   getSpacedStr:  Takes 1st 11 bits, formats them, and populates
	#   spaced string list.
	##################################################################################
	def getSpacedStr(self, binData):
		# TESTPRINT
		# print
		# print 'Testing getSpacedStr()...'
		k = 0
		for instr in binData.machineLines:
			# TESTPRINT
			# print instr
			if (binData.isInstr[k] == True):
				temp = "" + instr[0:8]
				temp = temp + " "
				temp = temp + instr[8:11]
				temp = temp + " "
				temp = temp + instr[11:16]
				temp = temp + " "
				temp = temp + instr[16:21]
				temp = temp + " "
				temp = temp + instr[21:26]
				temp = temp + " "
				temp = temp + instr[26:32]
				binData.instrSpaced.append(temp)
			else:
				binData.instrSpaced.append('')
			k += 1
	
	# TESTPRINT
	# print 'test instrSpaced: ' + str(binData.instrSpaced)
	##################################################################################
	#   printAssem: iterates through the lists and prints assembley code.
	##################################################################################
	def printAssem(self, binData):
		# TESTPRINT
		# print
		# print 'Testing printAssem()...'
		k = 0
		for k in range(k, binData.numLinesText):
			# Pull single line of binary data, spaced.
			startLine = ''
			line = ''
			if (binData.isInstr[k] == True):
				# Memory address.
				startLine += binData.instrSpaced[k]
			else:
				startLine += binData.machineLines[k]
			startLine += '\t' + str(binData.memLines[k]) + '\t'
			
			if (binData.insType[k] == 'R'):
				line = line + binData.opCodeStr[k]
				# if(binData.shamNum[k] == ''):       # If this is NOT an LSR or LSL...
				# 	line = line + '\t' + 'R' + str(binData.rdRtRegNum[k]) + ', '
				# else:
				# 	line = line + '\t' + 'R' + str(binData.rmRegNum[k]) + ', '
				line = line + '\t' + 'R' + str(binData.rdRtRegNum[k]) + ', '  # Print dest register.
				line = line + ' ' + 'R' + str(binData.rnRegNum[k]) + ','  # print src register.
				# Does this R-format use shift?
				if (binData.shamNum[k] == ''):
					line = line + ' ' + 'R' + str(binData.rmRegNum[k])
				else:
					line = line + ' ' + '#' + str(binData.shamNum[k])
			elif (binData.insType[k] == 'I'):
				line += binData.opCodeStr[k]
				line = line + '\t' + 'R' + str(binData.rdRtRegNum[k]) + ','
				line += ' R' + str(binData.rnRegNum[k]) + ','
				line += ' #' + str(binData.immNum[k])
			elif (binData.insType[k] == 'D'):
				line += binData.opCodeStr[k]
				line += '\t' + 'R' + str(binData.rdRtRegNum[k]) + ','
				line += ' ' + '[R' + str(binData.rnRegNum[k]) + ', #'
				line += str(binData.addrNum[k]) + ']'
			elif (binData.insType[k] == "CB"):
				line += binData.opCodeStr[k]
				line += '\t' + 'R' + str(binData.rdRtRegNum[k]) + ','
				line += ' ' + '#' + str(binData.addrNum[k])
			elif (binData.insType[k] == "B"):
				line += binData.opCodeStr[k]
				line += '\t' + "#" + str(binData.addrNum[k])
			elif (binData.insType[k] == "IM"):
				line += binData.opCodeStr[k]
				line += '\t' + "R" + str(binData.rdRtRegNum[k]) + ','
				line += ' ' + str(binData.immNum[k]) + ','
				line += ' ' + "LSL " + str(binData.shiftNum[k])
			elif (binData.insType[k] == 'BREAK'):
				line += binData.opCodeStr[k]
			elif (binData.insType[k] == 'DATA'):
				line += str(binData.data[k])
			elif (binData.insType[k] == "NOP"):
				line += str(binData.opCodeStr[k])
			binData.litInstr.append(line)
			startLine += line
			binData.finalText += startLine + '\n'
		# print lines
		print binData.finalText
	
	##################################################################################
	#   writeOut:  writes final product to text file.
	##################################################################################
	def writeOut(self, binData):
		outFile = open(binData.outFile, 'w')
		outFile.write(binData.finalText)
		outFile.close()
	
	##################################################################################
	#   run:  processes provided text file.
	##################################################################################
	def run(self, binData):
		# Open inFile & store data to list.
		self.openRead(binData)
		self.processElvBits(binData)
		self.processRegs(binData)
		self.getSpacedStr(binData)
		self.printAssem(binData)
		self.writeOut(binData)
	

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
		
		self.regFile.regFileList[self.rd] = self.rdVal
	
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
		
		self.regFile.regFileList[self.rd] = self.rdVal
	
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
		
		self.regFile.regFileList[self.rd] = self.rdVal
	
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
	
	###############################################################################
	###############################################################################
	def doLDUR(self, nc, x):
		# print 'INSIDE LDUR...'
		nc.PC = self.memLines[x]  # Increment PC to CURRENT instruction.
		rn = self.rnRegNum[x]  # Base Address in Register #
		print '\trn:', rn
		rnVal = nc.regState[rn]  # Base Address is...
		print '\trnVal:', rnVal
		addr = self.addrNum[x]  # Offset
		print '\taddr:', addr
		memAdr = (addr * 4) + rnVal
		datAdr = memAdr - nc.datStart
		datAdr /= 4
		print '\tdatAdr:  ', datAdr
		
		# dataIndex = ((nc.datStart   - rnVal + addr) / 4)  # Fancy doings.
		# print '\t(datStart - rnVal):', (nc.datStart - rnVal)
		# print '\tdatStart:', nc.datStart
		# print '\tdataIndex:', dataIndex
		# print '\tcontents datState[datIndex]:  ', nc.datState[dataIndex]
		# print '\tcontents datState[37]:  ', nc.datState[37]
		
		testBound = datAdr > len(nc.datState) - 1
		if not testBound:
			load = nc.datState[datAdr]
			print '\tload: ', load      # TESTPRINT
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
			print '\tload: ', load  # TESTPRINT
			# print '\tload:', load
			rd = self.rdRtRegNum[x]
			nc.regState[rd] = load
			nc.litIns = self.litInstr[x]
			
			self.regFile.regFileList[rd] = load
			
	
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
		elif (self.shiftNum[x] == 1):
			nc.regState[rd] = nc.regState[rd] & BIT_MASK_1
			self.regFile.regFileList[rd] = regFile.regFileList[rd] & BIT_MASK_1
		elif (self.shiftNum[x] == 2):
			nc.regState[rd] = nc.regState[rd] & BIT_MASK_2
			self.regFile.regFileList[rd] = regFile.regFileList[rd] & BIT_MASK_2
		else:
			nc.regState[rd] = nc.regState[rd] & BIT_MASK_3
			self.regFile.regFileList[rd] = regFile.regFileList[rd] & BIT_MASK_3
		# TESPRINT
		# print "shift num: ", self.shiftNum[x]
		nc.regState[rd] = nc.regState[rd] + (self.immNum[x] * (2 ** self.shiftNum[x]))
		
		self.regFile.regFileList[rd] = regFile.regFileList[rd] + (self.immNum[x] * (2 ** self.shiftNum[x]))
	
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
		print
		print '======================================================================='
		binData.finalText += '=======================================================================' + "\n"
		print 'Cycle ' + str(clockCycle + 1) + ':  ' + str(self.cycles[clockCycle].PC) + \
		      '\t\t' + self.cycles[clockCycle].litIns
		binData.finalText += 'Cycle ' + str(clockCycle + 1) + ':  ' + str(self.cycles[clockCycle].PC) + '\t\t' + self.cycles[clockCycle].litIns + "\n"
		print '\nRegisters:'
		binData.finalText += '\nRegisters:' + "\n"
		z = 0
		for x in range(0, 4):  # Prints all registers 4 rows x 8 columns
			line = 'r' + str(z).zfill(2) + ':\t'
			for y in range(0, 8):
				line += str(self.cycles[clockCycle].regState[y + z]) + '\t'
			print line
			binData.finalText += line + "\n"
			z += 8

		print '\nData:' 
		binData.finalText += '\nData:' + "\n"
		datStart = self.cycles[0].datStart
		header = str(datStart) + ':\t'
		y = 0
		for x, d in enumerate(self.cycles[clockCycle].datState):
			if ((x != 0) & (x % 8 == 0)):
				y += 1
				header += '\n' + str(datStart + (y * 32)) + ':\t'
			header += str(d) + '\t'
		print header
		binData.finalText += header + "\n"
	
	def printCycles(self, binData):
		binData.finalText = ''
		for x, cycle in enumerate(self.cycles):
			self.printCycle(x, binData)
		self.writeOut(binData)

import sys, getopt
from reg import RegFile
def main():
	binData = BinData()         # inData holds all the binary and assembled data.
	regFile = RegFile()         # regFile holds the latest register state.
	
	# Get command line data
	for i in range(len(sys.argv)):
		if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
			binData.inFile = sys.argv[i+1]
		elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
			binData.outFile = sys.argv[i+1] + '_dis.txt'
	# Initialize objects
	diss = Dissemble()
	diss.run(binData)
	#TESPRINT
	#print binData.outFile
	for i in range(len(sys.argv)):
		if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
			binData.inFile = sys.argv[i+1]
		elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
			binData.outFile = sys.argv[i+1] + '_sim.txt'
	#TESPRINT
	#print binData.outFile
	sim = Simulator(binData.opCodeStr, binData.isInstr, binData.insType, binData.data, binData.rmRegNum,
	                binData.shamNum, binData.rnRegNum, binData.rdRtRegNum, binData.immNum, binData.addrNum,
	                binData.shiftNum, binData.litInstr, binData.memLines, binData.numLinesText, regFile)
	sim.run(binData)
	
	# # TESTPRINT
	# print 'LIT INSTRUCTIONS'
	# for x, ins in enumerate(sim.litInstr):
	# 	print x, '   ', ins
	
	# TESTPRINT - Register file in RegFile object.
	print 'REGISTER FILE'
	for el in regFile.regFileList:
		print el, ',  ',
		
if __name__== "__main__":
	main()


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
		# print binData.finalText
	
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
	

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

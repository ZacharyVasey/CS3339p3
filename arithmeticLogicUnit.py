################################
# ALU
# The ALU handles all non-memory instructions (everything except LDUR and STUR and branch instructions that are handled in the IF stage).
# All ALU operations take one clock cycle.
# When the ALU finishes, the instruction is moved from the pre-ALU buffer to the post-ALU buffer.
# The ALU can only fetch one instruction from the pre-ALU buffer per clock cycle.
################################
class ArithmeticLogicUnit(object):
    def __init__(self):
        self.output = 0
    def compute(self, opCodeStr, firstReg, secondReg):
		if opCodeStr == 'ADD':
			object.doADD(firstReg, secondReg)
		elif opCodeStr == 'SUB':
			self.doSUB(firstReg, secondReg)
		elif opCodeStr == 'LSL':
			self.doLSL(firstReg, secondReg)
		elif opCodeStr == 'LSR':
			self.doLSR(firstReg, secondReg)
		elif opCodeStr == 'AND':
			self.doAND(firstReg, secondReg)
		elif opCodeStr == 'ORR':
			self.doORR(firstReg, secondReg)
		elif opCodeStr == 'EOR':
			self.doEOR(firstReg, secondReg)
		elif opCodeStr == 'ASR':
			self.doASR(firstReg, secondReg)
		elif opCodeStr == 'ADDI':
			self.doADDI(firstReg, secondReg)
		elif opCodeStr == 'SUBI':
			self.doSUBI(firstReg, secondReg)
		elif opCodeStr == 'MOVK':
			self.doMOVK(firstReg, secondReg)
		elif opCodeStr == 'MOVZ':
			self.doMOVZ(firstReg, secondReg)
		elif opCodeStr == 'NOP':
			self.doNOP(firstReg, secondReg)
		elif opCodeStr == 'BREAK':
			self.doBREAK(firstReg, secondReg)
        else:
            print "error in ArithmeticLogicUnit"
    def getOutput(self):
        return self.output
    ###############################################################################
    ###############################################################################
    def doADD(self, data1, data2):
        self.output = data1 + data2
    ###############################################################################
    ###############################################################################
    def doSUB(self, data1, data2):
        self.output = data1 - data2
    ###############################################################################
    ###############################################################################
    def doLSL(self, data, shift):
        self.output = (data % (1 << 64)) << shift
    ###############################################################################
    ###############################################################################
    def doLSR(self, data, shift):
        self.output = (data % (1 << 64)) >> shift
    ###############################################################################
    ###############################################################################
    def doAND(self, data1, data2):
        self.output = data1 & data2
    ###############################################################################
    ###############################################################################
    def doORR(self, data1, data2):
        self.output = data1 | data2
    ###############################################################################
    ###############################################################################
    def doEOR(self, data1, data2):
        self.output = data1 ^ data2
    ###############################################################################
    ###############################################################################
    def doASR(self, data, shift):
        self.output = data >> shift
    ###############################################################################
    ###############################################################################
    def doADDI(self, data, imm):
        self.output = data + imm
    ###############################################################################
    ###############################################################################
    def doSUBI(self, data, imm):
        self.output = data - imm
    ###############################################################################
    ###############################################################################
    #def doLDUR(self, nc, x):

    ###############################################################################
    ###############################################################################
    #def doSTUR(self, nc, x):

    ###############################################################################
    ###############################################################################
    #def doCBZ(self, nc, x):

    ###############################################################################
    ###############################################################################
    def doMOVZ(self, imm, shift):
        self.output = (imm * (2 ** shift))
    ###############################################################################
    ###############################################################################
    def doMOVK(self, data, imm, shift):
        BIT_MASK_0 = 0xFFFFFFFFFFFF0000
        BIT_MASK_1 = 0xFFFFFFFF0000FFFF
        BIT_MASK_2 = 0xFFFF0000FFFFFFFF
        BIT_MASK_3 = 0x0000FFFFFFFFFFFF
        if (shift == 0):
            data = data & BIT_MASK_0
        elif (shift == 1):
            data = data & BIT_MASK_1
        elif (shift == 2):
            data = data & BIT_MASK_2
        else:
            data = data & BIT_MASK_3
        data = data + (imm * (2 ** shift))

    ###############################################################################
    ###############################################################################
    #def doCBNZ(self, nc, x):

    ###############################################################################
    ###############################################################################
    #def doNOP(self, nc, x):

    ###############################################################################
    ###############################################################################
    #def doB(self, nc, x):

    ###############################################################################
    ###############################################################################
    #def doBREAK(self, nc, x):
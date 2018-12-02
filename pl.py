#========================================================================
# Class Pipeline
# The front face of the program, which will manage other operating
# classes.
#========================================================================
from cache import Cache
from insf import IF
from prealu import PreALU
from postalu import PostALU
from premem import PreMEM
from postmem import PostMEM
from preIssueBuffer import PreIssueBuffer
from arithmeticLogicUnit import ArithmeticLogicUnit

class PL(object):
	def __init__(self, bd):
		self.binData = bd
		
	def run(self):
		print("\n\n======================================================================")
		print('\nWELCOME TO THE PIPELINE')
		
		# TESTPRINT cache
		ch = Cache()
		ch.testPrint()
		
		# Initialized single, shared PC.
		pc = 96
		
		# Create IF object and pass starting address.  Run IF/ID phase.
		ifo = IF(self.binData)
		ifo.run()

		# Create Pre Issue Buffer
		pib = PreIssueBuffer()

		# Create Pre MEM unit
		preMEM = PreMEM()
		
		# Create Pre MEM unit
		preALU = PreALU()
		
		#Create ALU
		ALU = ArithmeticLogicUnit()
		
		# Create post MEM unit
		postMEM = PostMEM()

		# Create post ALU unit
		postALU = PostALU()
		
		#ALU Compute
		ALU.compute(opCodeStr, Reg1, Reg2)
		
		#assign output to post ALU
		postALU.setContent(ALU.getOutput())
		
		print('\n======================================================================\n\n')
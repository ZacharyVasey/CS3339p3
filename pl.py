#========================================================================
# Class Pipeline
# The front face of the program, which will manage other operating
# classes.
#========================================================================
from cache import Cache
from insf import IF

class PL(object):
	def __init__(self, bd):
		self.binData = bd
		
	def run(self):
		print '\n\n======================================================================'
		print '\nWELCOME TO THE PIPELINE'
		
		# TESTPRINT cache
		ch = Cache()
		ch.testPrint()
		
		# Initialized single, shared PC.
		pc = 96
		
		# Create IF object and pass starting address.  Run IF/ID phase.
		ifo = IF(self.binData)
		ifo.run()
		
		
		
		
		print '\n======================================================================\n\n'
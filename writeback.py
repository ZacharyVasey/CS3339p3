#####################################################################################
# WriteBack Class:	Manages the writeback unit.  Pulls from Post-MEM and Post-ALU
#					units.  Only writes to Reg unit when control signal switched on.
#####################################################################################
from reg import RegFile
from postmem import PostMem
from postalu import PostAlu

class WriteBack(object):
	def __init__(self, regob, pmemob, paluob):
		# print "Testing WriteBack().init..."		# TESTPRINT
		self.regob = regob
		self.pmo = pmemob
		self.pao = paluob
		self.cont = False;

	#################################################################################
	# contOff:	Switches control off - blocking writes to register.
	#################################################################################
	def contOff(self):
		print 'WB control OFF.'		# TESTPRINT
		self.cont = False;
	#################################################################################
	# contOff:	Switches control one - allowing writes to register.
	#################################################################################
	def contOn(self):
		print 'WB control ON.'		# TESTPRINT
		self.cont = True;


	#################################################################################
	# writeFromBuffs:	front facing function to write to register file.
	#################################################################################
	def writeFromBuffs(self):		
		if (self.cont):
			self.writeReg(self.pmo.regInd, self.pmo.regVal, 
				self.pao.regInd, self.pao.regVal)

	#################################################################################
	# writeReg:		performs actual working of writing to register file.  Was written
	#				before writeFromBuffs for testing purposes.
	#################################################################################
	def writeReg(self, regID = None, regVal = None, regID2 = None, regVal2 = None):
		# print "\ncurrent cont:" + str(self.cont) 	# TESTPRINT

		if (self.cont):		# If control signal on, proceed to write.
			if (regID2 == None):
				self.regob.regFile[regID] = regVal
			elif (regID == None):
				self.regob.regFile[regID2] = regVal2
			else:
				self.regob.regFile[regID] = regVal
				self.regob.regFile[regID2] = regVal2








		
	
	
	
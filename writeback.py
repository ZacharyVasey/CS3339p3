from reg import RegFile
from postmem import PostMEM

class WriteBack(object):
	def __init__(self, regob):
		print "Testing WriteBack().init..."		# TESTPRINT
		self.regob = regob
		self.cont = False;

	def contOff(self):
		print 'WB control off.'		# TESTPRINT
		self.cont = False;

	def contOn(self):
		print 'WB control on.'		# TESTPRINT
		self.cont = True;


	def wbTest(self, regID, regVal, regID2 = None, regVal2 = None):
		# print "\ncurrent cont:" + str(self.cont)

		if (self.cont):		# If control signal on, proceed to write.
			if (regID2 == None):
				self.regob.regFile[regID] = regVal
			else:
				self.regob.regFile[regID] = regVal
				self.regob.regFile[regID2] = regVal2








		
	
	
	
#====================================================================================
# PreIss
# 	Rather than doing the work of passing all the instruction data the mem and alu 
#	units will need, here we pass the binData index, which gives access to the 
#	exact data the mem and alu will need.
#
#	"The pre-issue buffer has 4 entries, each entry can store a single instruction.  
#	The instructions are sorted in their program order (entry 0 always contains the 
#	oldest instruction and entry 3 contains the newest)."
#
#	"If there is no room in the pre-issue buffer, no instructions can be fetched at 
#	the current cycle."
#
#	"If there is only one empty slot in the pre-issue buffer, only one instruction 
#	will be fetched."
# 	
#	Holds 4 entries.  NOT FIFO.  Program order, so there is no need to monitor
# 	first in.  We pass binData indices, which are already - by their nature -  are 
#	already in program order.
#									
#	 
#	
#====================================================================================
class PreIss(object):
	
	def __init__(self):
		self.preIssBuff = [None, None, None, None]

	def printBuff(self):
		lines = '\nPRE-ISSUE BUFFER\n'
		for priInd, pri in enumerate(self.preIssBuff):
			lines += 'Entry ' + str(priInd) + ': ' + str(pri) + '\n'
		print lines

	def countEmpties(self):
		c = 0;
		for pri in self.preIssBuff:
			if pri == None:
				c += 1
		return c

	def sortBuff(self):
		self.preIssBuff.sort()

	def feedBuff(self, bdx, bdx2 = None):
		count = self.countEmpties()
		if (bdx2 == None):
			# If good empty test, do work to feed one entry & return success.
			if (count != 0):
				for priInd, pri in enumerate(self.preIssBuff):
					if pri == None:
						self.preIssBuff[priInd] = bdx
						return True		# Return success of feed.
			# If bad empty test, return failure.  
			else:
				print 'ERROR: attempt to feed full buffer.  The instruction(s)' \
					+ ' should NOT have been \nfetched in the first place if ' \
					+ 'there is no room if the pre-issue buffer!'
				return False
		else:
			# If good empty test, do work to feed two entries.
			if (count >= 2): 
				for priInd, pri in enumerate(self.preIssBuff):
					if pri == None:
						self.preIssBuff[priInd] = bdx
						break
				for priInd, pri in enumerate(self.preIssBuff):
					if pri == None:
						self.preIssBuff[priInd] = bdx2
						return True		
			# Do work to terminate program if not room for BOTH entries.
			# The instructions should have never have been fetched in the 
			# FIRST place if no room in buffer.  
			else:
				print 'ERROR: attempt to feed full buffer.  The instruction(s)' \
					+ ' should NOT have been \nfetched in the first place if ' \
					+ 'there is no room if the pre-issue buffer!'				
				return False

	def emptyBuff(self, priInd, pri):
		if self.preIssBuff[priInd] == pri:
			self.preIssBuff[priInd] = None
			return True
		return False


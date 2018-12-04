#====================================================================================
# PreMem
# 	Holds 2 entries.  FIFO.  1 - oldest. 0 - newest.
#	Armed with the static BDX, PreMem can reference BinData for all the data it needs
#	based on a single index.	
#	When the memBuffer is fed, it is given a BDX its FI (first in/oldest) changed to 0.
#	When a memBuffer is emptied (one entry at a time), its BDX is changed to None.
#									
#										FI		BDX	
#									-----------------
#								0	| False	|	96	|
#									-----------------
#								1	| True	|  104	|
#									-----------------
#====================================================================================
class PreMem(object):
	def __init__(self):
		self.memBuff = [[None, None], [None, None]]

	def printBuff(self):
		print '\nPRE-MEM memBuffER'
		print 'Entry 1:  ' + '[OLDEST - ' + str(self.memBuff[0][0]) + ' | BDX - ' \
			+ str(self.memBuff[0][1]) + ']'
		print 'Entry 2:  ' + '[OLDEST - ' + str(self.memBuff[1][0]) + ' | BDX - ' \
			+ str(self.memBuff[1][1]) + ']'	

	# If both entries are empty, empty neither, feed 1st.
	# If ONE entry is empty, feed the empty, dump the full.
	# If BOTH entries are full, empty the oldest, and feed NEITHER.

	def emptyBuff(self):
		retVal = -1
		# Test if BOTH entries are full (defer to oldest).
		if (self.memBuff[0][1] != None) and (self.memBuff[1][1] != None):
			if self.memBuff[0][0] == True:		# If first entry is oldest.
				retVal = self.memBuff[0][1]		# Grab the PC index.
				self.memBuff[0][1] = None		# Empty the entry.
				self.memBuff[1][0] = True		# Now other non-empty entry is oldest.
				self.memBuff[0][0] = False 		# And empty list is "young."
				return retVal
			else:
				retVal = self.memBuff[1][1]	# Grab the PC index.
				self.memBuff[1][1] = None		# Empty the entry.
				self.memBuff[1][0] = False		# Now other non-empty entry is oldest.
				self.memBuff[0][0] = True 		# And empty list is "young."		
				return retVal
		# Test if BOTH entries are empty.  Return -1.
		if (self.memBuff[0][1] == None) and (self.memBuff[1][1] == None):
			return False
		# At this point one entry is empty, one is not.
		if (self.memBuff[0][1] != None):
			retVal = self.memBuff[0][1]		# Grab the PC index.
			self.memBuff[0][1] = None		# Empty the entry.
			self.memBuff[1][0] = True		# Now other non-empty entry is oldest.
			self.memBuff[0][0] = False 		# And empty list is "young."
			return retVal
		else:
			retVal = self.memBuff[1][1]		# Grab the PC index.
			self.memBuff[1][1] = None		# Empty the entry.
			self.memBuff[1][0] = False		# Now other non-empty entry is oldest.
			self.memBuff[0][0] = True 		# And empty list is "young."		
			return retVal		

	def feedBuff(self, pc):
		# Test if BOTH entries are empty.
		if (self.memBuff[0][1] == None) and (self.memBuff[1][1] == None):
			self.memBuff[0][1] = pc 		# Dump in first entry.
			self.memBuff[0][0] = True		# This entry is oldest.
			self.memBuff[1][0] = False 	
			return True
		# Test if BOTH entries are full.
		if (self.memBuff[0][1] != None) and (self.memBuff[1][1] != None):
			return False
		# Test if FIRST entry is empty
		if (self.memBuff[0][1] == None):
			self.memBuff[0][1] = pc 		# Fill entry with PC index.
			self.memBuff[0][0] = False		# Set entry FI/oldest to false. (Its now youngest.)
			self.memBuff[1][0] = True		# Set OTHER entry to oldest.  (It doesn't matter if
			return True						# the other entry is empty.)
		# Test if SECOND entry is empty
		if (self.memBuff[1][1] == None):
			self.memBuff[1][1] = pc 
			self.memBuff[1][0] = True
			self.memBuff[0][0] = False
			return True
		return False						# Failure to feed memBuffer.
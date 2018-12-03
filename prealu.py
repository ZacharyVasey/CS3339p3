#====================================================================================
# PreAlu
# 	Holds 2 entries.  FIFO.  1 - oldest. 0 - newest.
# 	What does it need?  All information necessary to perform arithmetic operations.
#		Take it straight from BinData object.
#		There we have a matrix of information: columns of data, rows of instructions.
#		How do we know which row to access?  
#			The PC.  
#				We must NOT reach out to PC unit FROM PreAlu to get the row.
#				We must pass a STATIC PC value TO the PreALU.
#	Armed with the static PC, PreALU can reference BinData for all the data it needs
#	based on a single index.
#	
#	When the aluBuffer is fed, it is given a PC its FI (first in/oldest) changed to 0.
#	When a aluBuffer is emptied (one entry at a time), its PC is changed to None.
#									
#										FI		PC	
#									-----------------
#								0	| False	|	96	|
#									-----------------
#								1	| True	|  104	|
#									-----------------
#====================================================================================
class PreAlu(object):
	def __init__(self):
		self.aluBuff = [[None, None], [None, None]]

	def printBuff(self):
		print '\nPRE-ALU aluBuffER'
		print 'Entry 1:  ' + '[OLDEST - ' + str(self.aluBuff[0][0]) + ' | PC - ' \
			+ str(self.aluBuff[0][1]) + ']'
		print 'Entry 2:  ' + '[OLDEST - ' + str(self.aluBuff[1][0]) + ' | PC - ' \
			+ str(self.aluBuff[1][1]) + ']'	

	# If both entries are empty, empty neither, feed 1st.
	# If ONE entry is empty, feed the empty, dump the full.
	# If BOTH entries are full, empty the oldest, and feed NEITHER.

	def emptyBuff(self):
		retVal = -1
		# Test if BOTH entries are full (defer to oldest).
		if (self.aluBuff[0][1] != None) and (self.aluBuff[1][1] != None):
			if self.aluBuff[0][0] == True:		# If first entry is oldest.
				retVal = self.aluBuff[0][1]		# Grab the PC index.
				self.aluBuff[0][1] = None		# Empty the entry.
				self.aluBuff[1][0] = True		# Now other non-empty entry is oldest.
				self.aluBuff[0][0] = False 		# And empty list is "young."
				return retVal
			else:
				retVal = self.aluBuff[1][1]	# Grab the PC index.
				self.aluBuff[1][1] = None		# Empty the entry.
				self.aluBuff[1][0] = False		# Now other non-empty entry is oldest.
				self.aluBuff[0][0] = True 		# And empty list is "young."		
				return retVal
		# Test if BOTH entries are empty.  Return -1.
		if (self.aluBuff[0][1] == None) and (self.aluBuff[1][1] == None):
			return False
		# At this point one entry is empty, one is not.
		if (self.aluBuff[0][1] != None):
			retVal = self.aluBuff[0][1]		# Grab the PC index.
			self.aluBuff[0][1] = None		# Empty the entry.
			self.aluBuff[1][0] = True		# Now other non-empty entry is oldest.
			self.aluBuff[0][0] = False 		s# And empty list is "young."
			return retVal
		else:
			retVal = self.aluBuff[1][1]	# Grab the PC index.
			self.aluBuff[1][1] = None		# Empty the entry.
			self.aluBuff[1][0] = False		# Now other non-empty entry is oldest.
			self.aluBuff[0][0] = True 		# And empty list is "young."		
			return retVal		

	def feedBuff(self, pc):
		# Test if BOTH entries are empty.
		if (self.aluBuff[0][1] == None) and (self.aluBuff[1][1] == None):
			self.aluBuff[0][1] = pc 		# Dump in first entry.
			self.aluBuff[0][0] = True		# This entry is oldest.
			self.aluBuff[1][0] = False 	# Being paranoid.
			return True
		# Test if BOTH entries are full.
		if (self.aluBuff[0][1] != None) and (self.aluBuff[1][1] != None):
			return False
		# Test if FIRST entry is empty
		if (self.aluBuff[0][1] == None):
			self.aluBuff[0][1] = pc 		# Fill entry with PC index.
			self.aluBuff[0][0] = False		# Set entry FI/oldest to false. (Its now youngest.)
			self.aluBuff[1][0] = True		# Set OTHER entry to oldest.  (It doesn't matter if
			return True					# the other entry is empty.)
		# Test if SECOND entry is empty
		if (self.aluBuff[1][1] == None):
			self.aluBuff[1][1] = pc 
			self.aluBuff[1][0] = True
			self.aluBuff[0][0] = False
			return True
		return False						# Failure to feed aluBuffer.







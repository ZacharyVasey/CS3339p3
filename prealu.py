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
#	When the buffer is fed, it is given a PC its FI (first in/oldest) changed to 0.
#	When a buffer is emptied (one entry at a time), its PC is changed to None.
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
		self.buff = [[None, None], [None, None]]

	def printBuff(self):
		print '\nPRE-ALU BUFFER'
		print 'Entry 1:  ' + '[OLDEST - ' + str(self.buff[0][0]) + ' | PC - ' \
			+ str(self.buff[0][1]) + ']'
		print 'Entry 2:  ' + '[OLDEST - ' + str(self.buff[1][0]) + ' | PC - ' \
			+ str(self.buff[1][1]) + ']'	

	# If both entries are empty, empty neither, feed 1st.
	# If ONE entry is empty, feed the empty, dump the full.
	# If BOTH entries are full, empty the oldest, and feed NEITHER.

	def emptyBuff(self):
		retVal = -1
		# Test if BOTH entries are full (defer to oldest).
		if (self.buff[0][1] != None) and (self.buff[1][1] != None):
			if self.buff[0][0] == True:		# If first entry is oldest.
				retVal = self.buff[0][1]	# Grab the PC index.
				self.buff[0][1] = None		# Empty the entry.
				self.buff[1][0] = True		# Now other non-empty entry is oldest.
				self.buff[0][0] = False 	# And empty list is "young."
				return retVal
			else:
				retVal = self.buff[1][1]	# Grab the PC index.
				self.buff[1][1] = None		# Empty the entry.
				self.buff[1][0] = False		# Now other non-empty entry is oldest.
				self.buff[0][0] = True 		# And empty list is "young."		
				return retVal
		# Test if BOTH entries are empty.  Return -1.
		if (self.buff[0][1] == None) and (self.buff[1][1] == None):
			return -1
		# At this point one entry is empty, one is not.
		if (self.buff[0][1] != None):
			retVal = self.buff[0][1]	# Grab the PC index.
			self.buff[0][1] = None		# Empty the entry.
			self.buff[1][0] = True		# Now other non-empty entry is oldest.
			self.buff[0][0] = False 	# And empty list is "young."
			return retVal
		else:
			retVal = self.buff[1][1]	# Grab the PC index.
			self.buff[1][1] = None		# Empty the entry.
			self.buff[1][0] = False		# Now other non-empty entry is oldest.
			self.buff[0][0] = True 		# And empty list is "young."		
			return retVal		

	def feedBuff(self, pc):
		# Test if BOTH entries are empty.
		if (self.buff[0][1] == None) and (self.buff[1][1] == None):
			self.buff[0][1] = pc 		# Dump in first entry.
			self.buff[0][0] = True		# This entry is oldest.
			self.buff[1][0] = False 	# Being paranoid.
			return True
		# Test if BOTH entries are full.
		if (self.buff[0][1] != None) and (self.buff[1][1] != None):
			return -1
		# Test if FIRST entry is empty
		if (self.buff[0][1] == None):
			self.buff[0][1] = pc 		# Fill entry with PC index.
			self.buff[0][0] = False		# Set entry FI/oldest to false. (Its now youngest.)
			self.buff[1][0] = True		# Set OTHER entry to oldest.  (It doesn't matter if
			return True					# the other entry is empty.)
		# Test if SECOND entry is empty
		if (self.buff[1][1] == None):
			self.buff[1][1] = pc 
			self.buff[1][0] = True
			self.buff[0][0] = False
			return True
		return False						# Failure to feed buffer.







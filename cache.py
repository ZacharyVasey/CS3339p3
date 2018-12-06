#========================================================================
# Class Cache
#  Aint nothin counterfeit here.
#========================================================================
import copy
class Cache(object):
	def __init__(self, bindata):
		self.bdo = bindata
		self.setIndexMask = 0x18
		self.ch = []
		# Initialize empty cache.  ch -> 4 sets -> 2 blocks
		bl = [0, 0, 0, 0, 0, 0]
		st = []
		for x in range(0, 4):
			for y in range(0, 2):
				st = copy.deepcopy([])
				st.append(copy.deepcopy(bl))
				st.append(copy.deepcopy(bl))
			self.ch.append(copy.deepcopy(st))

	##############################################################################
	#	printCache: 	Prints formatted cache.
	##############################################################################	
	def printCache(self):
		lines = "\nCACHE\t[V, D, T, W, W, LRU]"
		for num, set in enumerate(self.ch):
			lines += '\nSet' + str(num) + '\t'
			for block in set:
				lines += '\n\t' + str(block)
		print lines

	##############################################################################
	#	getBlockOffset: 	Calculated block offset (word 0 or word 1) within a block.
	#		Takes:		Memory address.
	#		Returns:	0 or 1 (placement in block, not truth value).
	##############################################################################
	def getBlockOffset(self, pc):
		if pc % 8 == 0:
			return 0
		return 1

	##############################################################################
	#	getSetIndex: 	Calculates which set a memory address belongs to.
	#		Takes:		Memory address.
	#		Returns:	setIndex: 0, 1, 2, or 3
	##############################################################################
	def getSetIndex(self, pc):
		setIndex = None
		#print "SetIndexMask:", self.setIndexMask, "~", str(bin(self.setIndexMask))
		setIndex = self.setIndexMask & pc
		#print "SetIndexMask & PC", setIndex
		setIndex = setIndex >> 3
		#print "SetIndex >> 3:  ", setIndex
		return setIndex

	##############################################################################
	#	getTag: 	Calculates which tag of a memory address.
	#		Takes:		Memory address.
	#		Returns:	Tag.
	##############################################################################
	def getTag(self, pc):
		return pc >> 5

	##############################################################################
	#	getCacheAddr: 	Generates a cache address to specific word of data.
	#		Takes:		Memory address.
	#		Returns:	[setIndex, Block, BlockOffset]
	##############################################################################
	def getCacheAddr(self, pc):
		
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blo = self.getBlockOffset(pc)
		# print "SI: ", setIndex
		# print "TG: ", tag

		for block in range(0, 2):						# Test both blocks.
			# If address exists in cache and is valid YAY!
			if (tag == self.ch[setIndex][block][2]) and (self.ch[setIndex][block][0] == 1):
					self.updateLRU([setIndex, block, blo])	# Update LRU.
					return [setIndex, block, blo]			# If yes to both: return addr.
		
		# Fetch the words we need from binData.
		word1 = self.bdo.data[((pc-96)/4)]					# Grab word.
		if blo == 0:
			word2 = self.bdo.data[((pc-96)/4)+1]			# Grab word's right neighbor.
		else:
			word2 = self.bdo.data[((pc-96)/4)-1]			# Grab words left neighbor.

		# Find out how many, if any, invalid blocks exist.
		ivb = -1
		for block in range(0, 2):
			if self.ch[setIndex][block][0] == 0:
				ivb = block 

		# If we have an invalid block YAY we dump the new data there. 
		if ivb != -1:
			if blo == 0:
				self.ch[setIndex][ivb] = [1, 0, tag, word1, word2, 1]
			else:
				self.ch[setIndex][ivb] = [1, 0, tag, word2, word1, 1]
			self.updateLRU([setIndex, ivb, blo])
			return [setIndex, ivb, blo]
		
		# If we have NO invalid blocks, we write over the least recently used.
		if self.ch[setIndex][0][5] == 0:
			if blo == 0:
				self.ch[setIndex][0] = [1, 0, tag, word1, word2, 1]
			else:
				self.ch[setIndex][0] = [1, 0, tag, word2, word1, 1]
			self.updateLRU([setIndex, 0, blo])
			return [setIndex, 0, blo]
		else:
			if blo == 0:
				self.ch[setIndex][1] = [1, 0, tag, word1, word2, 1]
			else:
				self.ch[setIndex][1] = [1, 0, tag, word2, word1, 1]
			self.updateLRU([setIndex, 0, blo])
			return [setIndex, 1, blo]

		return [None, None, None]
	
	##############################################################################
	#	getData: 	Returns a specific word of data from cache.
	#		Takes:		Memory address.
	#		Returns:	A word of data in cache.
	##############################################################################
	def getData(self, pc):
		# Discover if pc is in cache.
		hit = self.getCacheAddr(pc)
		if hit[0] != None:
			return self.ch[hit[0]][hit[1]][hit[2]+3]
		else:
			return None
	
	##############################################################################
	#	hasEmptyBlock: 	Tests for 1 or 2 empty blocks within a single set.
	#		Takes:		Memory address.
	#		Returns:	Truth value.
	##############################################################################
	def hasEmptyBlock(self, pc):
		setIndex = getSetIndex(pc)
		for row in self.ch[setIndex]:
			if row[0] == 0:
				return True
		return False

	##############################################################################
	#	clearCache: 	Returns a specific word of data from cache.
	#		Takes:		Memory address.
	#		Returns:	A word of data in cache.
	##############################################################################
	def clearCache(self):
		bl = [0, 0, 0, 0, 0, 0]
		st = []
		for setInd in range(0, 4):
			for bloInd in range(0, 2):
				self.ch[setInd][bloInd] = [0, 0, 0, 0, 0, 0]

	def updateLRU(self, cAddr):
		self.ch[cAddr[0]][cAddr[1]][5] = 1		# Update lru bit (5th in block).
		if cAddr[1] == 0:						# If block is first in set (0).
			self.ch[cAddr[0]][1][5] = 0			# Set the second block's LRU to 0.
		else:									# If not first, then it MUST be second.
			self.ch[cAddr[0]][0][5] = 0			# Set first block's LRU to 0.

	##############################################################################
	#	fetchData: 		Returns a specific word of data from cache.
	#		Takes:		Memory address.
	#		Returns:	A word of data in cache.
	##############################################################################
	def fetchData(self, mAddr, mAddr2 = None):
		data = None
		data2 = None
		
		cAddr = self.getCacheAddr(mAddr)	# Test if mAddr is in cache.
		if cAddr[0] != None:				# If address is not empty...
			data = self.getData(mAddr)		# Grab the data.
			self.updateLRU(cAddr)				# Update LRU bit.

		if mAddr2 != None:						# If there are two data requests...
			cAddr2 = self.getCacheAddr(mAddr2)			# Grab the cache address.
			if cAddr2[0] != None:				# If cache entry is not empty.
				data2 = self.getData(mAddr2)	# Grab data at entry.
				self.updateLRU(cAddr2)			# Update LRU bit.
		return [data, data2]

	##############################################################################
	#	testDataFetch: 	Tests fetching data and updating LRU.  If hit, returns
	#					correct data.  If miss, fetches data from testfile.
	#		Takes:		1 or 2 memory addresses.
	#					1 or 2 expected results.
	##############################################################################
	def testDataFetch(self, memAddr, expect, memAddr2 = None, expect2 = None):
		
		intro = "\nFetch data @ " + str(memAddr)		# Print intro.
		if memAddr2 != None:
			intro += ", " + str(memAddr2)
		print intro

		hit = self.getCacheAddr(memAddr)				# Get hit truth for first.
		if hit[0] == None:
			truth = False
		else:
			truth = True
		print "Hit " + str(memAddr) + ": " + str(truth)

		if memAddr2 != None:
			hit2 = self.getCacheAddr(memAddr2)			# Get hit truth for first.
			if hit2[0] == None:
				truth2 = False
			else:
				truth2 = True
			print "Hit " + str(memAddr2) + ": " + str(truth2)

		tempLines = "Expect: [" + str(expect)
		if memAddr2 != None:
			tempLines += ", " + str(expect2) + "]"
		else:
			tempLines += ", None]"
		print tempLines

		data = self.fetchData(memAddr, memAddr2)
		print "Result:", data

		self.printCache()
	
	##############################################################################
	#	fabTestCache: 	Fabricates a base cache populated with entries, some with
	#					valid bits on, some off.  
	#		Structure:	Addresses 96 - 124 have values 501 - 508.
	#	`				Addresses 192 - 220 have values 509 - 516.
	##############################################################################
	def fabTestCache(self):
		#			   [V, D, T, W, W, LRU]
		pc = 96
		tag = self.getTag(pc)
		si = self.getSetIndex(pc)
		bo = self.getBlockOffset(pc)
		block = self.ch[si][0] = [1, 0, tag, 501, 502, 0]
		# print "\nPC :", pc
		# print "Tag:", tag 
		# print "SI ", si
		# print "BO :", bo
		# print "block: ", block

		pc += 8	
		tag = self.getTag(pc)
		si = self.getSetIndex(pc)
		bo = self.getBlockOffset(pc)
		block = self.ch[si][0] = [1, 0, tag, 503, 504, 0]
		# print "\nPC :", pc
		# print "Tag:", tag 
		# print "SI ", si
		# print "BO :", bo
		# print "block: ", block	

		pc += 8	
		tag = self.getTag(pc)
		si = self.getSetIndex(pc)
		bo = self.getBlockOffset(pc)
		block = self.ch[si][0] = [0, 0, tag, 505, 506, 1]
		# print "\nPC :", pc
		# print "Tag:", tag 
		# print "SI ", si
		# print "BO :", bo
		# print "block: ", block	

		pc += 8
		tag = self.getTag(pc)
		si = self.getSetIndex(pc)
		bo = self.getBlockOffset(pc)
		block = self.ch[si][0] = [0, 0, tag, 507, 508, 1]
		# print "\nPC :", pc
		# print "Tag:", tag 
		# print "SI ", si
		# print "BO :", bo
		# print "block: ", block	

		pc = 192
		tag = self.getTag(pc)
		si = self.getSetIndex(pc)
		bo = self.getBlockOffset(pc)
		block = self.ch[si][1] = [1, 0, tag, 509, 510, 1]
		# print "\nPC :", pc
		# print "Tag:", tag 
		# print "SI ", si
		# print "BO :", bo
		# print "block: ", block	
		
		pc += 8
		tag = self.getTag(pc)
		si = self.getSetIndex(pc)
		bo = self.getBlockOffset(pc)
		block = self.ch[si][1] = [0, 0, tag, 511, 512, 1]
		# print "\nPC :", pc
		# print "Tag:", tag 
		# print "SI ", si
		# print "BO :", bo
		# print "block: ", block	

		pc += 8
		tag = self.getTag(pc)
		si = self.getSetIndex(pc)
		bo = self.getBlockOffset(pc)
		block = self.ch[si][1] = [0, 0, tag, 513, 514, 0]
		# print "\nPC :", pc
		# print "Tag:", tag 
		# print "SI ", si
		# print "BO :", bo
		# print "block: ", block	

		pc += 8
		tag = self.getTag(pc)
		si = self.getSetIndex(pc)
		bo = self.getBlockOffset(pc)
		block = self.ch[si][1] = [1, 0, tag, 515, 516, 0]
		# print "\nPC :", pc
		# print "Tag:", tag 
		# print "SI ", si
		# print "BO :", bo
		# print "block: ", block	

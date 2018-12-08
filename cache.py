##############################################################################
#	Cache Class: 	2-Way 4-Set 2-Block Cache.  Maintains a cache and based
# 					on provided PC address, provides or loads a word of data.
##############################################################################
import copy
class Cache(object):
	def __init__(self, bindata):
		
		self.bdo = bindata
		self.setIndexMask = 0x18
		self.ch = []
		self.setCount = 4
		self.blockCount = 2
		# Initialize empty cache.  ch -> 4 sets -> 2 blocks
		bl = [0, 0, 0, 0, 0]
		set = [copy.deepcopy(bl), copy.deepcopy(bl), 0]
		for setC in range(0, self.setCount):
			self.ch.append(copy.deepcopy(set))
	############################################################################
	#	printCache: 	Prints formatted cache.
	############################################################################
	def printCache(self):
		lines = "\nCACHE\t\t[ V, D, T,  W, W ]"

		for setC in range (0, self.setCount):
			lines += '\nSet ' + str(setC) + ' - LRU ' + str(self.ch[setC][2])
			for blockC in range (0, self.blockCount):
				lines += '\n\tBlock ' + str(blockC) + '\t[(' + str(self.ch[setC][blockC][0]) + ', ' \
					+ str(self.ch[setC][blockC][1]) + ', ' + str(self.ch[setC][blockC][2]) \
					+ ') <' + str(self.ch[setC][blockC][3]) + ', ' \
					+ str(self.ch[setC][blockC][4]) + '>]'
		print lines
	############################################################################
	#	getBlockOffset: 	Calculated block offset (word 0 or word 1) within a block.
	#		Takes:			Memory address.
	#		Returns:		0 or 1 (placement in block, not truth value).
	############################################################################
	def getBlockOffset(self, pc):
		if pc % 8 == 0:
			return 0
		if pc % 8 == 4:
			return 1
		return -1
	############################################################################
	#	getSetIndex: 	Calculates which set a memory address belongs to.
	#		Takes:		Memory address.
	#		Returns:	setIndex: 0, 1, 2, or 3
	############################################################################
	def getSetIndex(self, pc):
		setIndex = None
		# print "SetIndexMask:", self.setIndexMask, "~", str(bin(self.setIndexMask))
		setIndex = self.setIndexMask & pc
		#print "SetIndexMask & PC", setIndex
		setIndex = setIndex >> 3
		#print "SetIndex >> 3:  ", setIndex
		return setIndex
	############################################################################
	#	getTag: 	Calculates which tag of a memory address.
	#		Takes:		Memory address.
	#		Returns:	Tag.
	############################################################################
	def getTag(self, pc):
		return pc >> 5
	############################################################################
	#	getTag: 	Calculates which tag of a memory address.
	#		Takes:		Memory address.
	#		Returns:	Tag.
	############################################################################
	def getCacheAddr(self, pc):
		cAddr = [None, None, None]
		tag = self.getTag(pc)
		setIndex = self.getSetIndex(pc)
		blockOff = self.getBlockOffset(pc)

		for block in range (0, 2):
			if self.ch[setIndex][block][0] == 1:			# Is block valid?
				if self.ch[setIndex][block][2] == tag:		# Does tag match?
					return [setIndex, block, blockOff]		# Return that addr.
		return cAddr 	# Return None set.
	############################################################################
	#	getData: 		Grabs data, either from cache or memory.
	#		Takes:		Memory address.
	#		Returns:	Word.
	############################################################################
	def getData(self, pc):
		cAddr = self.getCacheAddr(pc)

		if cAddr[0] != None:									# Hit.
			self.ch[cAddr[0]][2] = cAddr[1]						# Update LRU.
			return self.ch[cAddr[0]][cAddr[1]][cAddr[2] + 3]	# Return data.
		else:													# Results in a miss.  
			bdoInd = (pc-96)/4									# Cache must pull from memory.
			# bdoDat = self.bdo.data[bdoInd]					# FOR DECIMAL DATA
			bdoDat = self.bdo.machineLines[bdoInd]
			nbrInd = -1
			tag = self.getTag(pc)
			setIndex = self.getSetIndex(pc)
			blockOff = self.getBlockOffset(pc)
			# Determine which memory neighbor to grab (left v right).
			if pc % 8 == 0:
				# nbrDat = self.bdo.data[bdoInd+1]				# FOR DECIMAL DATA
				nbrDat = self.bdo.machineLines[bdoInd+1]
				nbrInd = 4
			else: 
				# nbrDat = self.bdo.data[bdoInd-1]				# FOR DECIMAL DATA
				nbrDat = self.bdo.machineLines[bdoInd-1]
				nbrInd = 3
			# Determine which block to overwrite.
			block = -1		
			for blockInd in range(0, self.blockCount):			# Check for invalid bits.
				if self.ch[setIndex][blockInd][0] == 0:
					block = blockInd
					break
			if (block != -1):	# We have an empty block!
				# Write over current data.
				self.ch[setIndex][block][blockOff+3] = bdoDat
				# Don't forgot neighbor data.
				self.ch[setIndex][block][nbrInd] = nbrDat
				# Turn valid bit on.
				self.ch[setIndex][block][0] = 1
				# Update tag.
				self.ch[setIndex][block][2] = tag
				# Update LRU.
				self.ch[setIndex][2] = block
			else:				# No empty block.  Must determine via LRU.
				# Grab LRU index.
				block = self.ch[setIndex][2]
				# Write over current data.
				self.ch[setIndex][block][blockOff+3] = bdoDat
				# Don't forgot neighbor data.
				self.ch[setIndex][block][nbrInd] = nbrDat
				# Update tag.
				self.ch[setIndex][block][2] = tag				
				# Update LRU.
				self.ch[setIndex][2] = block

		cAddr = self.getCacheAddr(pc)
		if cAddr[0] != None:									# Hit.
			self.ch[cAddr[0]][2] = cAddr[1]						# Update LRU.
			return self.ch[cAddr[0]][cAddr[1]][cAddr[2] + 3]	# Return data.
	############################################################################
	#	clearCache: 	Zeroes out cache.
	############################################################################
	def clearCache(self):
		for setInd in range(0, 4):
			self.ch[setInd][2] = 0
			for blockInd in range(0, 2):
				self.ch[setInd][blockInd] = [0, 0, 0, 0, 0]	
	############################################################################
	#	fabTestCache: 	Fabricates a base cache populated with entries, some with
	#					valid bits on, some off.  
	#		Structure:	Addresses 96 - 124 have values 501 - 508.
	#	`				Addresses 192 - 220 have values 509 - 516.
	############################################################################
	def fabTestCache(self):
		self.ch[0][2] = 1
		self.ch[2][2] = 1
		
		pc = 104		# 104
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blockOff = self.getBlockOffset(pc)
		self.ch[setIndex][0] = [1, 0, tag, 1, 2]
		pc += 8			# 112
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blockOff = self.getBlockOffset(pc)
		self.ch[setIndex][0] = [1, 0, tag, 3, 4]
		pc += 8			# 120
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blockOff = self.getBlockOffset(pc)
		self.ch[setIndex][0] = [1, 0, tag, 5, 6]
		pc += 8			# 128
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blockOff = self.getBlockOffset(pc)
		self.ch[setIndex][0] = [1, 0, tag, 7, 8]
		pc += 8			# 136
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blockOff = self.getBlockOffset(pc)
		self.ch[setIndex][1] = [1, 0, tag, 9, 10]
		pc += 8			# 144
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blockOff = self.getBlockOffset(pc)
		self.ch[setIndex][1] = [0, 0, tag, 11, 12]	
		pc += 8			# 152
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blockOff = self.getBlockOffset(pc)
		self.ch[setIndex][1] = [0, 0, tag, 13, 14]	
		pc += 8			# 160
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blockOff = self.getBlockOffset(pc)
		self.ch[setIndex][1] = [1, 0, tag, 15, 16]	
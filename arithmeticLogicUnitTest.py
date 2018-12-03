from arithmeticLogicUnit import ArithmeticLogicUnit
from prealu import PreALU
from postalu import PostALU

def main():
    # Register 1
    register_one = [6, 7, 9, 64, 6, 2, 1, 35, 44, 8, 55, 31, '']
    # Register 2
    register_two = [4, 3, 10, 2, 3, 6, 4, 74, 62, 12, 7, 3, '']
    # Immediate
    immediate = ['', '', '', '', '', '', '', '', 86, 255, '', '', '']
    # Shift
    shift = ['', '', 3, 4, '', '', '', 3, '', '', 1, 2, '']
    # OpcodeString
    opcodeString = ["ADD", "SUB", "LSL", "LSR", "AND", "ORR", "EOR", "ASR", "ADDI", "SUBI", "MOVK", "MOVZ", "NOP"]

    # Create Pre ALU
    preALU = PreALU()
    # Create ALU
    ALU = ArithmeticLogicUnit()
    # Create post ALU unit
    postALU = PostALU()

    # index to help with testing
    index = 0
    # Expected result
    expectedResult = 0

    # ALU Computer TEST ADD
    ALU.compute(opcodeString[index], register_one[index], register_two[index])
    print opcodeString[index] + ", " + str(register_one[index]) + ", " + str(register_two[index])
    print "Result: " + str(ALU.getOutput())
    expectedResult = register_one[index] + register_two[index]
    print "Expected: " + str(expectedResult) + "\n"
    index = index + 1

    # ALU Computer TEST SUB
    ALU.compute(opcodeString[index], register_one[index], register_two[index])
    print opcodeString[index] + ", " + str(register_one[index]) + ", " + str(register_two[index])
    print "Result: " + str(ALU.getOutput())
    expectedResult = register_one[index] - register_two[index]
    print "Expected: " + str(expectedResult) + "\n"
    index = index + 1

    # ALU Computer TEST LSL
    ALU.compute(opcodeString[index], register_one[index], shift[index])
    print opcodeString[index] + ", " + str(register_one[index]) + ", " + str(shift[index])
    print "Result: " + str(ALU.getOutput())
    expectedResult = (register_one[index] % (1 << 64)) << shift[index]
    print "Expected: " + str(expectedResult) + "\n"
    index = index + 1

    # ALU Computer TEST LSR
    ALU.compute(opcodeString[index], register_one[index], shift[index])
    print opcodeString[index] + ", " + str(register_one[index]) + ", " + str(shift[index])
    print "Result: " + str(ALU.getOutput())
    expectedResult = (register_one[index] % (1 << 64)) >> shift[index]
    print "Expected: " + str(expectedResult) + "\n"
    index = index + 1

    # ALU Computer TEST AND
    ALU.compute(opcodeString[index], register_one[index], register_two[index])
    print opcodeString[index] + ", " + str(register_one[index]) + ", " + str(register_two[index])
    print "Result: " + str(ALU.getOutput())
    expectedResult = register_one[index] & register_two[index]
    print "Expected: " + str(expectedResult) + "\n"
    index = index + 1

if __name__== "__main__":
	main()

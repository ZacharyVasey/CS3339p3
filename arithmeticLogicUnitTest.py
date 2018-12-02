from arithmeticLogicUnit import ArithmeticLogicUnit
from prealu import PreALU
from postalu import PostALU

def main():
    # Register 1
    register_one = 6
    # Register 2
    register_two = 12
    # Immediate
    immediate = 1
    # OpcodeString
    opcodeString = "ADD"
    # Create Pre ALU
    preALU = PreALU()
    # Create ALU
    ALU = ArithmeticLogicUnit()
    # Create post ALU unit
    postALU = PostALU()
    # ALU Computer
    ALU.compute(opCodeStr, Reg1, Reg2)
    # assign output to post ALU
    postALU.setContent(ALU.getOutput())

if __name__== "__main__":
	main()
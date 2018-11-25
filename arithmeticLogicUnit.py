################################
# ALU
# The ALU handles all non-memory instructions (everything except LDUR and STUR and branch instructions that are handled in the IF stage).
# All ALU operations take one clock cycle.
# When the ALU finishes, the instruction is moved from the pre-ALU buffer to the post-ALU buffer.
# The ALU can only fetch one instruction from the pre-ALU buffer per clock cycle.
################################
class ArithmeticLogicUnit(object):
    def __init__(self):
        pass
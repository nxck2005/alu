from helpers import Helper
from numpy import *

# instruction set.
# some left blank
# 6 bit opcode, rest are needed data as per instruction
# 6 - 10 bits for operands as needed - 16 data bits
#    register reference or addressing mode

instructionSet = {
    "000000": "NOP", # no operation
    "000001": "ADD", # add value to accumulator
    "000010": "SUB", # subtract value from accumulator
    "000011": "ADC", # add value to accumulator, with carry flag
    "000100": "SBB", # subtract value from accumulator, with carry flag as borrow
    "000101": "AND", # do a logical AND between provided operand and AX, store result in AX
    "000110": "NOT", # logical NOT on the value provided, store in AX
    "000111": "OR",  # logical OR between value provided and AX, store result in AX
    "001000": "XOR", # logical XOR between value provided
    "001001": "LHA", # load immediate value to high 2byte of AX
    "001010": "LLA", # load immediate value to low 2byte of AX
    "001011": "LHB", # load immediate value to high 2byte of BX
    "001100": "LLB", # load immediate value to low 2byte of BX
    "001101": "LHC", # load immediate value to high 2byte of CX
    "001110": "LLC", # load immediate value to low 2byte to CX
    "001111": "INC", # increment a register
    "010000": "DEC", # decrement a register
    "010001": "JMP", # jump to a row of instruction
    "010010": "JZ",  # jump to row if ZF = 1
    "010011": "JNZ", # jump to row if ZF = 0
    "010100": "MOV", # move immediate value or register value to a register; needs more documentation
    "010101": "RCR", # rotate contents of register right
    "010110": "RCL", # rotate contents of register left
}



# implement all instructions here

def NOP():
    pass

# take a value, add it to ax
def ADD(reg1: list, reg2: list) -> list:
    pass

def SUB(reg1: list, reg2: list) -> list:
    pass

def ADC(reg1: list, reg2: list) -> list:
    pass

def SBB(reg1: list, reg2: list) -> list:
    pass
    
def AND():
    pass

def NOT():
    pass

def OR():
    pass

def XOR():
    pass
from helpers import Helper
import typing
from numpy import *



instructionSet = {
    (0,0,0,0,0,0): "NOP", # no operation
    (0,0,0,0,0,1): "ADD", # add value to accumulator
    (0,0,0,0,1,0): "SUB", # subtract value from accumulator
    (0,0,0,0,1,1): "ADC", # add value to accumulator, with carry flag
    (0,0,0,1,0,0): "SBB", # subtract value from accumulator, with carry flag as borrow
    (0,0,0,1,0,1): "AND", # do a logical AND between provided operand and AX, store result in AX
    (0,0,0,1,1,0): "NOT", # logical NOT on the value provided, store in AX
    (0,0,0,1,1,1): "OR",  # logical OR between value provided and AX, store result in AX
    (0,0,1,0,0,0): "XOR", # logical XOR between value provided 
    (0,0,1,0,0,1): "LHA", # load immediate value to high 2byte of AX
    (0,0,1,0,1,0): "LLA", # load immediate value to low 2byte of AX
    (0,0,1,0,1,1): "LHB", # load immediate value to high 2byte of BX
    (0,0,1,1,0,0): "LLB", # load immediate value to low 2byte of BX
    (0,0,1,1,0,1): "LHC", # load immediate value to high 2byte of CX
    (0,0,1,1,1,0): "LLC", # load immediate value to low 2byte to CX
    (0,0,1,1,1,1): "INC", # increment a register
    (0,1,0,0,0,0): "DEC", # decrement a register--
    (0,1,0,0,0,1): "JMP", # jump to a row of instruction
    (0,1,0,0,1,0): "JZ",  # jump to row if ZF = 1
    (0,1,0,0,1,1): "JNZ", # jump to row if ZF = 0
    (0,1,0,1,0,0): "MOV", # move immediate value or register value to a register; needs more documentation
    (0,1,0,1,0,1): "RCR", # rotate contents of register right
    (0,1,0,1,1,0): "RCL", # rotate contents of register left
}



# All instructions here
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
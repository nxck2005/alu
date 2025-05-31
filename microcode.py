from helpers import Helper
from numpy import *
import logging
from constants import *

# instruction set.
# some left blank
# 8 bit opcode, 24 bit extra data
# arithmetic instructions start w 1 in their first bit until leading zero problem is fixed

ml = logging.getLogger(__name__)

instructionSet = {
    "00000000": "NOP", # no operation
    "10000001": "ADD", # add value to accumulator
    "10000010": "SUB", # subtract value from accumulator
    "10000011": "ADC", # add value to accumulator, with carry flag
    "10000100": "SBB", # subtract value from accumulator, with carry flag as borrow
    "00000101": "AND", # do a logical AND between provided operand and AX, store result in AX
    "00000110": "NOT", # logical NOT on the value provided, store in AX
    "00000111": "OR",  # logical OR between value provided and AX, store result in AX
    "00001000": "XOR", # logical XOR between value provided
    "00001001": "LHA", # load immediate value to high halfword of AX
    "00001010": "LLA", # load immediate value to low halfword of AX
    "00001011": "LHB", # load immediate value to high halfword of BX
    "00001100": "LLB", # load immediate value to low halfword of BX
    "00001101": "LHC", # load immediate value to high halfword of CX
    "00001110": "LLC", # load immediate value to low halfword to CX
    "00001111": "INC", # increment a register
    "00010000": "DEC", # decrement a register
    "00010001": "JMP", # jump to a row of instruction
    "00010010": "JZ",  # jump to row if ZF = 1
    "00010011": "JNZ", # jump to row if ZF = 0
    "00010100": "MOV", # move next row into the register defined by the last 3 bits of the row; 0,1,2
    "00010101": "RCR", # rotate contents of register right
    "00010110": "RCL", # rotate contents of register left
}

def NOP(alu, memory):
    ml.info("Microcode executed for instruction NOP")
    pass

# add next row to accumulator
def ADD(alu, memory):
    ml.info("AX value before: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Value to add: %s", memory.MEMORY[alu.pc - 1][opcodeSize:])
    alu.REGISTERS[0] = Helper.hexToBin(int(
        (Helper.binToHex(alu.REGISTERS[0])[2:] + Helper.binToHex(memory.MEMORY[alu.pc - 1][opcodeSize:])[2:]), 16))
    ml.info("Microcode executed for instruction ADD")
    pass

def SUB(alu, memory):
    ml.info("Microcode executed for instruction SUB")
    pass

def ADC(alu, memory):
    ml.info("Microcode executed for instruction ADC")
    pass

def SBB(alu, memory):
    ml.info("Microcode executed for instruction SBB")
    pass
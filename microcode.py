from helpers import Helper
from numpy import *
import logging
from constants import *

# instruction set.
# some left blank
# 8 bit opcode, 24 bit extra data
# arithmetic instructions start w 1 in their first bit, change, leading zero prob is fixed

ml = logging.getLogger(__name__)

instructionSet = {
    "10000000": "NOP", # no operation DONE
    "10000001": "ADD", # add value to accumulator DONE
    "10000010": "SUB", # subtract value from accumulator DONE
    "10000011": "ADC", # add value to accumulator, with carry flag DONE
    "10000100": "SBB", # subtract value from accumulator, with carry flag as borrow DONE
    "10000101": "AND", # do a logical AND between provided operand and AX, store result in AX
    "10000110": "NOT", # logical NOT on the value provided, store in AX
    "10000111": "OR",  # logical OR between value provided and AX, store result in AX
    "10001000": "XOR", # logical XOR between value provided
    "10001001": "LHA", # load immediate value to high halfword of AX DONE
    "10001010": "LLA", # load immediate value to low halfword of AX DONE
    "10001011": "LHB", # load immediate value to high halfword of BX DONE
    "10001100": "LLB", # load immediate value to low halfword of BX DONE
    "10001101": "LHC", # load immediate value to high halfword of CX DONE
    "10001110": "LLC", # load immediate value to low halfword to CX DONE
    "10001111": "INC", # increment a register
    "10010000": "DEC", # decrement a register
    "10010001": "JMP", # jump to a row of instruction
    "10010010": "JZ",  # jump to row if ZF = 1
    "10010011": "JNZ", # jump to row if ZF = 0
    "10010100": "MOV", # move next row into the register defined by the last 3 bits of the row; 0,1,2
    "10010101": "RCR", # rotate contents of register right
    "10010110": "RCL", # rotate contents of register left
}

# no operation, does nothing
def NOP():
    ml.info("NOP encountered in an instruction row. No operation performed.")
    ml.info("Microcode executed for instruction NOP")
    pass

# add next row to accumulator
def ADD(alu, memory):
    ml.info("AX value before: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Value to add: %s", memory.MEMORY[alu.pc - 1][opcodeSize:])

    # Get the hexadecimal string for AX and the operand
    ax_hex = Helper.binToHex(alu.REGISTERS[0])[2:]
    operand_hex = Helper.binToHex(memory.MEMORY[alu.pc - 1][opcodeSize:])[2:]

    # Convert the hexadecimal strings to integers
    ax_int = int(ax_hex, 16)
    operand_int = int(operand_hex, 16)

    # Perform the addition plus mask to take care of overflow
    result_int = (ax_int + operand_int) & 0xFFFFFFFF
    
    result_list = Helper.hexToBin(result_int)

    # Convert the integer result back to binary and store it in AX
    alu.REGISTERS[0] = result_list
    ml.info("Microcode executed for instruction ADD")

# subtract next row from accumulator
def SUB(alu, memory):
    ml.info("AX value before: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Value to add: %s", memory.MEMORY[alu.pc - 1][opcodeSize:])

    # Get the hexadecimal string for AX and the operand
    ax_hex = Helper.binToHex(alu.REGISTERS[0])[2:]
    operand_hex = Helper.binToHex(memory.MEMORY[alu.pc - 1][opcodeSize:])[2:]

    # Convert the hexadecimal strings to integers
    ax_int = int(ax_hex, 16)
    operand_int = int(operand_hex, 16)

    # Perform the subtraction and mask for underflow
    result_int = (ax_int - operand_int) & 0xFFFFFFFF
    
    result_list = Helper.hexToBin(result_int)

    # Convert the integer result back to binary and store it in AX
    alu.REGISTERS[0] = result_list
    ml.info("Microcode executed for instruction SUB")

# add next row to accumulator, with carry flag
def ADC(alu, memory):
    ml.info("AX value before: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Value to add: %s", memory.MEMORY[alu.pc - 1][opcodeSize:])

    # Get the hexadecimal string for AX and the operands
    ax_hex = Helper.binToHex(alu.REGISTERS[0])[2:]
    operand_hex = Helper.binToHex(memory.MEMORY[alu.pc - 1][opcodeSize:])[2:]
    cf_hex = Helper.binToHex(alu.FLAGS[1])

    # Convert the hexadecimal strings to integers
    ax_int = int(ax_hex, 16)
    operand_int = int(operand_hex, 16)
    cf_int = int(cf_hex, 16)

    # Perform the addition plus mask to take care of overflow
    result_int = (ax_int + operand_int + cf_int) & 0xFFFFFFFF
    result_list = Helper.hexToBin(result_int)

    # Convert the integer result back to binary and store it in AX
    alu.REGISTERS[0] = result_list
    ml.info("Microcode executed for instruction ADC")
    pass

# subtract next row from accumulator, with carry flag as borrow
def SBB(alu, memory):
    ml.info("AX value before: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Value to add: %s", memory.MEMORY[alu.pc - 1][opcodeSize:])

    # Get the hexadecimal string for AX and the operands
    ax_hex = Helper.binToHex(alu.REGISTERS[0])[2:]
    operand_hex = Helper.binToHex(memory.MEMORY[alu.pc - 1][opcodeSize:])[2:]
    cf_hex = Helper.binToHex(alu.FLAGS[1])

    # Convert the hexadecimal strings to integers
    ax_int = int(ax_hex, 16)
    operand_int = int(operand_hex, 16)
    cf_int = int(cf_hex, 16)

    # Perform the addition plus mask to take care of overflow
    result_int = (ax_int - (operand_int + cf_int)) & 0xFFFFFFFF
    
    result_list = Helper.hexToBin(result_int)

    # Convert the integer result back to binary and store it in AX
    alu.REGISTERS[0] = result_list
    ml.info("Microcode executed for instruction SBB")
    pass

# load higher halfword, last 16 bits of row to AX
def LHA(alu, memory):
    ml.info("AX value before: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Immediate value to load: %s", memory.MEMORY[alu.pc - 1][16:])

    target_binary = memory.MEMORY[alu.pc - 1][16:]
    
    alu.REGISTERS[0][0:16] = target_binary
    ml.info("AX value after loading high halfword: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Microcode executed for instruction LHA")
    pass

# load lower halfword, first 16 bits of row to AX
def LLA(alu, memory):
    ml.info("AX value before: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Immediate value to load: %s", memory.MEMORY[alu.pc - 1][16:])

    target_binary = memory.MEMORY[alu.pc - 1][16:]
    
    alu.REGISTERS[0][16:] = target_binary
    ml.info("AX value after loading low halfword: %s", Helper.binToHex(alu.REGISTERS[0]))
    ml.info("Microcode executed for instruction LLA")
    pass

# load higher halfword, last 16 bits of row to BX
def LHB(alu, memory):
    ml.info("BX value before: %s", Helper.binToHex(alu.REGISTERS[1]))
    ml.info("Immediate value to load: %s", memory.MEMORY[alu.pc - 1][16:])

    target_binary = memory.MEMORY[alu.pc - 1][16:]
    
    alu.REGISTERS[1][0:16] = target_binary
    ml.info("BX value after loading high halfword: %s", Helper.binToHex(alu.REGISTERS[1]))
    ml.info("Microcode executed for instruction LHB")
    pass

# load lower halfword, last 16 bits of row to BX
def LLB(alu, memory):
    ml.info("BX value before: %s", Helper.binToHex(alu.REGISTERS[1]))
    ml.info("Immediate value to load: %s", memory.MEMORY[alu.pc - 1][16:])

    target_binary = memory.MEMORY[alu.pc - 1][16:]
    
    alu.REGISTERS[1][16:] = target_binary
    ml.info("BX value after loading low halfword: %s", Helper.binToHex(alu.REGISTERS[1]))
    ml.info("Microcode executed for instruction LLB")
    pass

def LHC(alu, memory):
    ml.info("CX value before: %s", Helper.binToHex(alu.REGISTERS[2]))
    ml.info("Immediate value to load: %s", memory.MEMORY[alu.pc - 1][16:])

    target_binary = memory.MEMORY[alu.pc - 1][16:]
    
    alu.REGISTERS[2][0:16] = target_binary
    ml.info("CX value after loading high halfword: %s", Helper.binToHex(alu.REGISTERS[2]))
    ml.info("Microcode executed for instruction LHC")
    pass

def LLC(alu, memory):
    ml.info("CX value before: %s", Helper.binToHex(alu.REGISTERS[2]))
    ml.info("Immediate value to load: %s", memory.MEMORY[alu.pc - 1][16:])

    target_binary = memory.MEMORY[alu.pc - 1][16:]
    
    alu.REGISTERS[2][16:] = target_binary
    ml.info("CX value after loading low halfword: %s", Helper.binToHex(alu.REGISTERS[2]))
    ml.info("Microcode executed for instruction LLC")
    pass
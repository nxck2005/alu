# Program to simulate an ALU.
# ALU takes speed as an argument. Mem takes rows
# Three registers, one accumulator and two data.
# The three registers are hardcoded for now. If changed, change all references.

# by @nxck2005

__version__ = "0.0.9.dev"
__author__ = "nxck2005"

# 32 bit word size
validArchSizes = 32
opcodeSize = 8

# values to enforce overflow/underflow
# python just adds a bit/digit/hex blabla
maxValue = 0xFFFFFFFF
minValue = 0x00000000

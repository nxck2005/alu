# Program to simulate an ALU.
# ALU takes speed as an argument. Mem takes rows
# Three registers, one accumulator and two data.

# by @nxck2005

__version__ = "0.0.3.dev"
__author__ = "nxck2005"


from numpy import random, array, copy
from helpers import Helper
from microcode import *

# 32 bit

validArchSizes = 32


class ALU:     
    def __init__(self, speed: int = 4):
        bits = validArchSizes
        
        # for genning registers
        sizes = [bits, bits, bits]
        
        self.REGISTERS = [0,1,2]
        self.bits = bits
        self.speed = speed
        self.FLAGS = [0,0,0]
        
        self.REGISTERS = [[0]*size for size in sizes]
        
        # For random generation, uncomment the next declaration and loop,
        # and comment the one before.
        # i = 0
        # for i in range(len(sizes)):
        #     self.REGISTERS[i] = random.randint(0, 2, size=bits)
        
        # cycles passed
        self.cycles = 0
        
        # program counter
        self.pc = 0
        
        print(f"ALU initialized. Architecture: {self.bits} bit.")
        print(f"Running at {self.speed} Hz.")
        
        # remove this after alpha
        print("Registers:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")
        
    def registers(self):
        print(f"Registers status after {self.cycles} cycles:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")
        
    def status(self):
        print(f"Architecture size: {self.bits}bit")
        print(f"Clock speed: {self.speed} Hz")
        print(f"Registers status after {self.cycles} cycles:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")
        
    
    # DEBUG INSTRUCTION
    # changes a register
    # TODO
    def poke(self, val, rNo):
        reg = array(Helper.hexToBin(val))
        if len(reg) != 32:
            print("Poke failed. Invalid length")
            return
        old = self.REGISTERS[rNo]
        self.REGISTERS[rNo] = copy(reg)
        print("Poked ALU! This is a debug function and can be deprecated.")
        print(f"Old: {old}")
        print(f"New: {reg}")
        print(f"On register {rNo}")
        return
        
        
    # Functions after here are incomplete and need work. Don't use
        
    def runCycle(self, memory, row=0):
        
        # pipeline
        # for execution:
        # fetch the row of instruction from memory
        # decode what to do, first half is opcode, second is data
        # execute, copy result to AX if arithmetic is done
        # one clock cycle passes after appropriate time.
        
        # FETCH
        
        opcode = self.fetch(memory.MEMORY[row])
        
        
        return
        
    def decode(self, opcode):
        opcode = tuple(opcode)
        try:
            if instructionSet[opcode]:
                return instructionSet[opcode]
        except:
            print("Opcode couldn't be decoded. DECODE returned NOP")
            return "NOP"
            
    # update opcode length when its decided
    def fetch(self, row):
        bits = (row[0:6])
        return bits
    
    def execute(self, memory):
        self.pc += 1
        if self.pc >= len(memory.MEMORY):
            self.pc = 0
        self.cycles += 1
        return
    
        
    
class Memory:
    def __init__(self, rows):
        archsize = validArchSizes
        self.rows = rows
        self.archsize = archsize
        self.MEMORY = []
        for _ in range(self.rows):
            # For only zeros, uncomment the next line, and comment the next.
            # self.MEMORY.append([0]*archsize)
            self.MEMORY.append(random.randint(0, 2, size=archsize))
        print(f'Memory initialized. {self.rows} lines.')
        
        # remove this after alpha
        print("  ", end='')
        print()
        i = 0
        for line in self.MEMORY:
            print(f"{i} {line}")
            i += 1
            
    def editIndex(self, row, index, new):
        if new in (0,1) and row <= self.rows and index <= self.archsize:
            self.MEMORY[row][index] = new
        else:
            print("Must be 0 or 1. Not modified.")
        return
    
    def editRow(self, row, newrow):
        if len(newrow) != self.archsize:
            print("Length of new row must be equal to the already existing architecture size. Not modified.")
            print(f"Archsize: {self.archsize}")
            return   
        for x in newrow:
            if x not in (0,1):
                print('Every value in new row must be 0 or 1. Not modified.')
                return
        self.MEMORY[row] = newrow.copy()
    
    def memory(self):
        print("  ", end='')
        i = 0
        for line in self.MEMORY:
            print(f"{i} {line}")
            i += 1
            
    def status(self):
        print(f"Memory size: {self.rows} rows, Total: {(self.rows * self.archsize / 8):.2f} B")
        print("  ", end='')
        i = 0
        for line in self.MEMORY:
            print(f"{i} {line}")
            i += 1
    
def main():
    print(Helper.hexToBin(0xFF))

if __name__ == '__main__':
    main()
from numpy import random, array, copy
from helpers import Helper
from microcode import *
from constants import validArchSizes, maxValue, minValue

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
    
    # DEBUG INSTRUCTIONS
    # changes a register
    # Remove after beta
    def poke(self, val, rNo):
        reg = array(Helper.hexToBin(val))
        if val > maxValue or val < minValue:
            print("Poke failed. Invalid length")
            return
        if rNo not in (0,1,2):
            print("Poke failed. Invalid register reference.")
            return
        old = self.REGISTERS[rNo]
        self.REGISTERS[rNo] = copy(reg)
        print("Poked ALU! This is a debug function and can be deprecated.")
        print(f"Old: {old}")
        print(f"New: {reg}")
        print(f"On register {rNo}")
        return
    
    # i know, i know, wrapper function but it feels more readable to me
    def reset(self):
        self.__init__()
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
    
    
def main():
    pass

if __name__ == '__main__':
    main()
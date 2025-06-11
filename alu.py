from numpy import random, array, copy
from helpers import Helper
import microcode
from constants import validArchSizes, maxValue, minValue
import logging
from memory import Memory

# get namespaced logger
aluLogger = logging.getLogger(__name__)

class ALU:     
    def __init__(self):
        aluLogger.debug('Called ALU init')
        bits = validArchSizes
        self.bits = bits

        # Zero, carry, sign, overflow
        self.FLAGS = ['0','0','0','0']
        
        # for genning registers
        sizes = [bits, bits, bits]
        self.REGISTERS = [0,1,2]
        
        self.REGISTERS = [['0']*size for size in sizes]
        
        # For random generation, uncomment the next declaration and loop,
        # and comment the one before.
        # i = 0
        # for i in range(len(sizes)):
        #     self.REGISTERS[i] = random.randint(0, 2, size=bits)
        
        # cycles passed
        self.cycles = 0
        
        # program counter
        self.pc = 0
        
        # last operation
        self.lastoperation = 'NOP'
        
        print(f"ALU initialized. Architecture: {self.bits} bit.")
        print(self.REGISTERS)
        
    def registers(self):
        print(f"Registers status after {self.cycles} cycles:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")
        
    def status(self):
        print(f"Architecture size: {self.bits}bit")
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
    
    ## Checks before and after execution of a word
    # increment pc and cycles
    def execPre(self, memory):
        self.pc += 1
        if self.pc >= len(memory.MEMORY):
            self.pc = 0
        self.cycles += 1
        return
    
    # memory overflow and underflow checks
    # and updation of flags
    # TODO add underflow check and make sign check better
    def execPost(self, memory):
        
        targetLength = validArchSizes
        aluLogger.info("Target length for overflow check: %s", targetLength)
        
        # check memory overflow
        for i in range(len(memory.MEMORY)):
            val = int(Helper.binToHex(memory.MEMORY[i]), 16)
            if val > maxValue:
                aluLogger.info("Memory Overflow detected: %s, trimming bits", memory.MEMORY[i])
                memory.MEMORY[i] = memory.MEMORY[i][-targetLength:]
                aluLogger.info("Row trimmed to: %s", memory.MEMORY[i])

        # check register overflow
        overflowHappened = 0
        for i in range(len(self.REGISTERS)):
            val = int(Helper.binToHex(self.REGISTERS[i]), 16)
            if val > maxValue:
                aluLogger.info("Register Overflow detected: %s, trimming bits", self.REGISTERS[i])
                self.REGISTERS[i] = self.REGISTERS[i][-targetLength:]
                aluLogger.info("Register trimmed to: %s", self.REGISTERS[i])
                overflowHappened = 1
        
        # overflow flag
        if overflowHappened == 1:
            self.FLAGS[3] = 1
            aluLogger.info("Overflow happened hence setting OF flag")
        else:
            self.FLAGS[3] = 0
            aluLogger.info("No overflow, flag OF reset")
            
        # zero flag
        if int((Helper.binToHex(self.REGISTERS[0])), 16) == 0x0:
            aluLogger.info("AX value: %s, setting ZF flag", Helper.binToHex(self.REGISTERS[0]))
            self.FLAGS[0] = 1
        else:
            aluLogger.info("AX value: %s, resetting ZF flag", Helper.binToHex(self.REGISTERS[0]))
            self.FLAGS[0] = 0
        
        # sign
        if int((Helper.binToHex(self.REGISTERS[0])), 16) > 0x80000000:
            aluLogger.info("AX value: %s, setting SF flag", Helper.binToHex(self.REGISTERS[0]))
            self.FLAGS[2] = 1
        else:
            aluLogger.info("AX value: %s, resetting SF flag", Helper.binToHex(self.REGISTERS[0]))
            self.FLAGS[2] = 0
            
            
        
        
    def execute(self, memory, instruction):
        # kinda ugly, but i just want an MVP working. clean it up
        self.execPre(memory)
        aluLogger.info("Execute pre-req's done; cycles, PC increased")
        try:
            opcode = Helper.decodeOpcode(instruction)
            operation = microcode.instructionSet[opcode]
            aluLogger.info("Decoded opcode: %s", opcode)
            aluLogger.info("Decoded operation: %s", operation)
            self.lastoperation = operation
        except:
            # todo: add more verbose logs
            aluLogger.error("An error occured while decoding the instruction. Maybe the instruction for the decoded opcode doesn't exist?", exc_info=True)
            aluLogger.error("Proceeding with a NOP...")
            operation = "NOP"
            self.lastoperation = operation
        finally:
            try:
                microcodeFunc = getattr(microcode, operation)
            except:
                aluLogger.error("An error occured while finding microcode for the decoded instruction. Maybe it doesn't exist?", exc_info=True)
                aluLogger.error("Proceeding with a NOP...")
                microcodeFunc = getattr(microcode, "NOP")
                self.lastoperation = "NOP"
            finally:
                microcodeFunc(self, memory)
            aluLogger.info("Executed instruction. Exec cycle complete")
            self.execPost(memory)
            aluLogger.info("Post checks done")
            memory.writeMemory()      
        return
    
def main():
    pass

if __name__ == '__main__':
    main()
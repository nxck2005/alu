# Program to simulate an ALU.
# ALU takes speed as an argument. Mem takes rows
# Three registers, one accumulator and two data.

# 32 bit
validArchSizes = 32

# instruction set
# some left blank

# 6 bit opcode, rest are needed data as per instruction

instructionSet = {
    (0,0,0,0): "NOP", # no operation
    (0,0,0,1): "ADD", # add value to accumulator
    (0,0,1,0): "SUB", # subtract value from accumulator
    (0,0,1,1): "ADC", # add value to accumulator, with carry flag
    (0,1,0,0): "SBB", # subtract value from accumulator, with carry flag as borrow
    (0,1,0,1): "AND", # do a logical AND between provided operand and AX, store result in AX
    (0,1,1,0): "NOT", # logical NOT on the value provided, store in AX
    (0,1,1,1): "OR",  # logical OR between value provided and AX, store result in AX
    (1,0,0,0): "XOR", # logical XOR between value provided 
    (1,0,0,1): "LHA", # load immediate value to high 2byte of AX
    (1,0,1,0): "LLA", # load immediate value to low 2byte of AX
    (1,0,1,1): "LHB", # load immediate value to high 2byte of BX
    (1,1,0,0): "LLB", # load immediate value to low 2byte of BX
    (1,1,0,1): "LHC", # load immediate value to high 2byte of CX
    (1,1,1,0): "LLC", # load immediate value to low 2byte to CX
    (1,1,1,1): "INC", # increment a register
}

class ALU:
    # Flags: ZF, CF, OF
    FLAGS = [0, 0, 0]
        
    def __init__(self, speed: int = 4):
        
        bits = validArchSizes
        
        # for genning registers
        sizes = [bits, bits, bits]
        
        self.bits = bits
        self.speed = speed
        self.FLAGS = [0,0,0]
        self.REGISTERS = [[0]*size for size in sizes]
        self.cycles = 0
        
        print(f"ALU initialized. Architecture: {self.bits} bit.")
        print(f"Running at {self.speed} Hz.")
        print("Registers:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")
        
    def registers(self):
        print(f"Registers status after {self.cycles} cycles:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")
        
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

    def status(self):
        print(f"Architecture size: {self.bits}bit")
        print(f"Clock speed: {self.speed} Hz")
        print(f"Registers status after {self.cycles} cycles:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")
        
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
        bits = (row[0:4])
        return bits
    
    def execute(self):
        pass
        

class Memory:
    def __init__(self, rows):
        archsize = validArchSizes
        self.rows = rows
        self.archsize = archsize
        self.MEMORY = []
        for _ in range(self.rows):
            self.MEMORY.append([0]*archsize)
        print(f'Memory initialized. {self.rows} lines.')
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
    speed = 4
    memsize = 8 # rows
    
    # bits = int(input("Number of bits for ALU: "))
    # speed = int(input("Speed for ALU in Hz: "))
    # memsize = int(input("Rows of memory: "))
    
    alu = ALU(speed)
    mem = Memory(memsize)

    

if __name__ == '__main__':
    main()
import typing

class ALU:
    # Flags: ZF, CF, OF
    FLAGS = [0, 0, 0]
        
    def __init__(self, speed: int = 4, bits: int = 8):
        
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
        
    def printRegisters(self):
        print("Registers:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")


class Memory:
    def __init__(self, rows, archsize):
        self.rows = rows
        self.archsize = archsize
        self.MEMORY = []
        for _ in range(self.rows):
            self.MEMORY.append([0]*archsize)
        print(f'Memory initialized. {self.rows} lines.')
        print("  ", end='')
        for i in range(self.rows):
            print(f' {i}', end=" ")
        print()
        i = 0
        for line in self.MEMORY:
            print(f"{i} {line}")
            
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
    
    def printMemory(self):
        print("  ", end='')
        for i in range(self.rows):
            print(f' {i}', end=" ")
        print()
        i = 0
        for line in self.MEMORY:
            print(f"{i} {line}")
            i += 1
            

def main():
    speed = 4
    bits = 8
    memsize = 8
    # bits = int(input("Number of bits for ALU: "))
    # speed = int(input("Speed for ALU in Hz: "))
    # memsize = int(input("Rows of memory: "))
    alu = ALU(speed, bits)
    mem = Memory(memsize, bits)
    
    mem.editIndex(1, 3, 1)
    mem.printMemory()
    

if __name__ == '__main__':
    main()
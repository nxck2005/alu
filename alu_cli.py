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
        print(f"ALU initialized. Architecture: {self.bits} bit.")
        print(f"Running at {self.speed} Hz.")
        print("Registers:")
        print(f"AX: {self.REGISTERS[0]}")
        print(f"BX: {self.REGISTERS[1]}")
        print(f"CX: {self.REGISTERS[2]}")

class Memory:
    def __init__(self, rows, archsize):
        self.rows = rows
        self.MEMORY = []
        for _ in range(rows):
            self.MEMORY.append([0]*archsize)
        print(f'Memory initialized. {rows} lines.')
        print(self.MEMORY)
        

def main():
    speed = 4
    bits = 8
    memsize = 16
    bits = int(input("Number of bits for ALU: "))
    speed = int(input("Speed for ALU in Hz: "))
    memsize = int(input("Rows of memory: "))
    alu = ALU(speed, bits)
    mem = Memory(memsize, bits)

if __name__ == '__main__':
    main()
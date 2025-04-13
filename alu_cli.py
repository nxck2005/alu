import typing

class ALU:
    
    # Flags: ZF, CF, OF
    FLAGS = [0, 0, 0]
    
    REGISTERS = [
        []
    ]
        
    def __init__(self, speed: int = 4, bits: int = 8):
        self.bits = bits
        self.speed = speed
        print(f"ALU initialized. Architecture: {self.bits} bit.")
        print(f"Running at {self.speed} Hz.")


def main():
    speed = 4
    bits = 8
    input("Number of bits for ALU: ", speed)
    alu = ALU(4, 8)

if __name__ == '__main__':
    main()
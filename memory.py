from numpy import random, array, copy
from helpers import Helper
from microcode import *
from constants import validArchSizes, maxValue, minValue

class Memory:
    def __init__(self, rows: int = 20):
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
            
    def status(self):
        print(f"Memory size: {self.rows} rows, Total: {(self.rows * self.archsize / 8):.2f} B")
        print("  ", end='')
        i = 0
        for line in self.MEMORY:
            print(f"{i} {line}")
            i += 1
    
    # DEBUG INSTRUCTIONS
    # Changes a memory row
    # TODO
    def poke(self, rowNo, value):
        row = array(Helper.hexToBin(value))
        if value > maxValue or value < minValue:
            print("Poke failed. Invalid length")
            return
        if not 0 <= rowNo <= len(self.MEMORY):
            print("Poke failed. Invalid memory reference")
            return
        old = self.MEMORY[rowNo]
        self.MEMORY[rowNo] = copy(row)
        print("Poked memory! This is a debug function and can be deprecated.")
        print(f"Old: {old}")
        print(f"New: {self.MEMORY[rowNo]}")
        print(f"On row number {rowNo}")
        return
    
    # wrapper function but it feels more readable to me
    def reset(self):
        self.__init__()
        return
    
def main():
    pass

if __name__ == '__main__':
    main()
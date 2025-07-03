from numpy import random, array, copy
from helpers import Helper
from microcode import *
from constants import validArchSizes, maxValue, minValue
import json

memLogger = logging.getLogger(__name__)

class Memory:
    def __init__(self, rows: int = 20, zero=False):
        archsize = validArchSizes
        self.rows = rows
        self.archsize = archsize
        self.MEMORY = []
        try:
            if zero == False:
                self.readMemory("memory.json")
            else:
                self.readMemory("zero.json")
            memLogger.info("Initialised mem from file")   
        except:
            memLogger.error("An error occured while reading from persistent memory. Falling back to random generation")
            self.MEMORY.append(random.randint(0, 2, size=archsize))        
            
    def status(self):
        print(f"Memory size: {self.rows} rows, Total: {(self.rows * self.archsize / 8):.2f} B")
        print("  ", end='')
        i = 0
        for line in self.MEMORY:
            print(f"{i} {line}")
            i += 1
    
    # DEBUG INSTRUCTION
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
        print(f"Writing..")
        self.writeMemory()
        print("Done!")
        return
    
    def readMemory(self, fname='memory.json'):
        fname = str(fname)
        try:
            with open(fname, "r") as f:
                memory_list = json.load(f)
                self.MEMORY = [array(lst) for lst in memory_list]
            memLogger.info("Memory read")
        except:
            memLogger.error("Error occured while reading from file", exc_info=True)
        return

    def writeMemory(self, fname='memory.json'):
        fname = str(fname)
        try:
            with open(fname, 'w') as f:
                f.write('[\n')  # start of json array
                
                # convert each row to json string
                rows = []
                for arr in self.MEMORY:
                    # convert numpy array to list and format as json without spaces
                    row_json = json.dumps(arr.tolist(), separators=(',', ':'))
                    rows.append(row_json)
                
                # join rows with comma and newline, and indent each row
                formatted = ',\n'.join(rows)
                f.write(' ' * 4 + formatted.replace('\n', '\n' + ' ' * 4))
                
                f.write('\n]')  # end of json array
        except:
            memLogger.error("Error occured while writing to file", exc_info=True)
            return
        finally:
            memLogger.info("Memory written")
        return
        
    # wrapper function but it feels more readable to me
    def reset(self):
        self.__init__(zero=True)
        self.writeMemory()
        return
    
def main():
    pass

if __name__ == '__main__':
    main()
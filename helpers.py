import logging
import typing

mcLogger = logging.getLogger(__name__)


class Helper:
    @staticmethod
    def ensureBinLength(register):
        if len(register) != 32:
            while len(register) != 32:
                register.insert(0, 0)
        return register
       
    @staticmethod
    def binToDec(register):        
        mcLogger.debug("binary to decimal called")
        decimal = 0       
        # pass an register that assumes an array.
        # outputs the equivalent decimal number    
        # arrays of values corresponding to place values       
        placevalues = []
        i = 0
        while i < len(register):           
            # for each value, index is like the exponent (2^0, 2^1)
            placevalues.append(2 ** i)
            i += 1        
        placevalues.reverse()   
        j = 0
        val = 0
        while j < len(register):           
            # value of the current place e.g. 2^3 * (1 or 0)
            val += register[j] * placevalues[j]    
            # add that to total
            decimal += val
            # reset buffer
            val = 0
            j += 1
        return decimal
    
    @staticmethod    
    def decToBin(number):
        mcLogger.debug("decimal to binary called")
        # uses division by 2
        num = number   
        binary = []   
        # quotient and remainder
        q = None
        r = None
        # divide by 2 until quotient becomes 0
        while q != 0:
            # append the remainder to the binary, and quotient becomes the dividend for next iter
            q = num // 2
            r = num % 2
            binary.append(r)
            num = q
        Helper.ensureBinLength(binary)   
        return binary
    
    @staticmethod
    def binToHex(r):
        mcLogger.debug("binary to hex called")
        binVal = ""
        for digit in r:
            binVal += str(digit)
        h = hex(int(binVal, 2)) # take the string as a int w base 2
        return h  
    
    @staticmethod
    def hexToBin(hexval):
        mcLogger.debug("hex to binary called")
        binval = bin(hexval)
        reg = []
        for digit in binval[2:]:
            reg.append(digit)
        Helper.ensureBinLength(reg)
        return reg
    
    @staticmethod
    def decodeOpcode(instruction):
        mcLogger.info("Decoding opcode from instruction %s", instruction)
        try:
            opcode = ""
            ocBits = instruction[:8]
            opcode = opcode.join(map(str, ocBits))
            mcLogger.debug("Decoded opcode: %s", opcode)
            return opcode
        except:
            mcLogger.error("An exception occured while decoding.")
            return ""
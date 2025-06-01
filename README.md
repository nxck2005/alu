# ALUSim

A ALU/assembly sim with a web interface for educational purposes.
This does compute!

## Key Features

- 32-bit word size
- Support for 3 CPU registers for operations
- Accumulator-centric (like 8080)
- Memory and program counter to store programs and data (unified)
- Basic instruction set (arithmetic, logical, data movement, control flow)
- Web interface using flask

## To run:

```bash
git clone https://github.com/nxck2005/alu.git
cd alu
pip install -r requirements.txt
flask --app app run
```

## Short term todo
- fix the leading zero problem (when the first 4 bits are 0, the hex comes out to be 1 digit short. this isnt the big problem, but when its done the other way, hex value to binary, and the first bits are 0, theyre not generated in the array)
- add more stringent error checking to values poked in (empty, not numerical etc)
- actually make it do stuff according to microcode

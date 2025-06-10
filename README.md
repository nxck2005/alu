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
- implement all the microcodes
- solve underflow problem
- switch to ajax

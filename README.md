# ALUSim

A 32-bit ALU/assembly sim with a web interface for educational purposes.
This does compute!

## Key Features (planned)

- 32-bit
- Support for 3 CPU registers for operations
- Memory and program counter to store programs and data (unified)
- Basic instruction set (arithmetic, logical, data movement, control flow)
- Planned web interface (flask)

## Short term todo
- add poke function for debug DONE
- add program counter DONE
- add buttons to page for extra func
- make the button POST DONE
- log changes to console, and maybe to a file
- fix the leading zero problem (when the first 4 bits are 0, the hex comes out to be 1 digit short. this isnt the big problem, but when its done the other way, hex value to binary, and the first bits are 0, theyre not generated in the array)

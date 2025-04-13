import pygame
import sys
import time

pygame.init()

# Constants
WIDTH, HEIGHT = 1910, 1005
BIT_SIZE = 30
GAP = 10
START_X, START_Y = 100, 100
FONT_SIZE = 20

WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4-bit ALU Simulator")
font = pygame.font.SysFont("Courier", FONT_SIZE)

# Registers and memory
regA = [0, 0, 0, 1]
regB = [0, 0, 0, 1]
out = [0, 0, 0, 0]

memory = [
    [0, 0, 0, 1],  # ADD 01
    [0, 0, 1, 0],  # ADD 10
    [1, 1, 0, 0],  # JMP 00
    [1, 0, 0, 1],  # MOV 1 to regA
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

RAM = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]

PC = 0
mode = 'STEP'
running_clock = False

# Opcodes
OPCODES = ['ADD', 'SUB', 'MOV', 'JMP']

# Utility functions
def to_int(bits):
    return int("".join(map(str, bits)), 2)

def to_bits(n):
    return [int(b) for b in format(n % 16, '04b')]

def ripple_add(a, b):
    result = []
    carry = 0
    for i in range(3, -1, -1):
        total = a[i] + b[i] + carry
        result.insert(0, total % 2)
        carry = total // 2
    return result

def ripple_sub(a, b):
    # 2's complement of B = invert + 1
    b_inv = [1 - bit for bit in b]
    b_twos = ripple_add(b_inv, [0, 0, 0, 1])
    return ripple_add(a, b_twos)

def draw_bits(bits, x, y, label):
    for i, bit in enumerate(bits):
        color = GREEN if bit else GREY
        pygame.draw.rect(screen, color, (x + i*(BIT_SIZE + GAP), y, BIT_SIZE, BIT_SIZE))
        pygame.draw.rect(screen, BLACK, (x + i*(BIT_SIZE + GAP), y, BIT_SIZE, BIT_SIZE), 2)

    # Label
    lbl = font.render(label, True, WHITE)
    screen.blit(lbl, (x - 70, y + 5))

    # Decimal
    value = to_int(bits)
    dec_lbl = font.render(f"= {value}", True, YELLOW)
    screen.blit(dec_lbl, (x + len(bits)*(BIT_SIZE + GAP) + 10, y + 5))

def draw_memory():
    mem_x, mem_y = 100, 250
    for i, word in enumerate(memory):
        for j, bit in enumerate(word):
            color = RED if i == PC else (GREEN if bit else GREY)
            pygame.draw.rect(screen, color, (mem_x + j*(BIT_SIZE + GAP), mem_y + i*35, BIT_SIZE, BIT_SIZE))
            pygame.draw.rect(screen, BLACK, (mem_x + j*(BIT_SIZE + GAP), mem_y + i*35, BIT_SIZE, BIT_SIZE), 2)
        # Mem address and decoded inst
        inst = to_int(word[:2])
        operand = to_int(word[2:])
        lbl = font.render(f"{i:02d}: {OPCODES[inst]} {operand}", True, WHITE)
        screen.blit(lbl, (mem_x + 200, mem_y + i*35))

def execute():
    global regA, regB, out, PC
    if PC >= len(memory): return
    inst_bits = memory[PC]
    opcode = to_int(inst_bits[:2])
    operand = to_int(inst_bits[2:])

    if opcode == 0:  # ADD
        out = ripple_add(regA, regB)
    elif opcode == 1:  # SUB
        out = ripple_sub(regA, regB)
    elif opcode == 2:  # MOV operand -> regA
        regA = to_bits(operand)  # Use operand as immediate value
    elif opcode == 3:  # JMP (unconditional)
        PC = operand
        return  # Exit to prevent PC increment

    PC = (PC + 1) % len(memory)

def shift_left(reg):
    reg.pop(0)
    reg.append(0)

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                execute()
            elif event.key == pygame.K_c:
                mode = 'CLOCK' if mode == 'STEP' else 'STEP'
            elif event.key == pygame.K_SPACE:
                running_clock = not running_clock
            elif event.key == pygame.K_1:
                shift_left(regA)
            elif event.key == pygame.K_2:
                shift_left(regB)

    if mode == 'CLOCK' and running_clock:
        execute()
        time.sleep(0.25)

    draw_bits(regA, START_X, START_Y, "Reg A")
    draw_bits(regB, START_X, START_Y + 50, "Reg B")
    draw_bits(out, START_X, START_Y + 100, "OUT")

    # Draw memory
    draw_memory()

    # PC & Mode
    pc_lbl = font.render(f"PC = {PC}  | Mode = {mode}", True, YELLOW)
    screen.blit(pc_lbl, (WIDTH - 300, 10))

    pygame.display.flip()
    clock.tick(60)
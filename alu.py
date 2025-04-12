import pygame
import sys
import time
import random

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BIT_SIZE = 30
GAP = 10
START_X, START_Y = 50, 100
CLOCK_SPEED = 4  # Hz

# ALU Ops
INSTRUCTIONS = ["ADD", "SUB", "MOV", "JUMP"]
instruction_pointer = 0

# Colors
BLACK, WHITE, RED, GREEN, BLUE, GREY, YELLOW = (0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255), (180,180,180), (255,255,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4-bit ALU Simulator")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 20)

# Registers
regA = [0, 0, 0, 0]
regB = [0, 0, 0, 0]
out = [0, 0, 0, 0]

# Control
step_mode = True
auto_clock = False
last_tick = time.time()

def draw_bits(bits, x, y, label):
    for i, bit in enumerate(bits):
        color = GREEN if bit else GREY
        pygame.draw.rect(screen, color, (x + i*(BIT_SIZE + GAP), y, BIT_SIZE, BIT_SIZE))
        pygame.draw.rect(screen, BLACK, (x + i*(BIT_SIZE + GAP), y, BIT_SIZE, BIT_SIZE), 2)
    lbl = font.render(label, True, WHITE)
    screen.blit(lbl, (x - 60, y + 5))

def ripple_add(a, b, subtract=False):
    result = []
    carry = 0
    for i in reversed(range(4)):
        ai = a[i]
        bi = b[i] ^ subtract  # For subtraction using 2's comp
        s = ai ^ bi ^ carry
        carry = (ai & bi) | (ai & carry) | (bi & carry)
        result.insert(0, s)
    return result

def execute_instruction():
    global regA, regB, out
    op = INSTRUCTIONS[instruction_pointer]
    if op == "ADD":
        out = ripple_add(regA, regB)
    elif op == "SUB":
        out = ripple_add(regA, regB, subtract=True)
    elif op == "MOV":
        out = regB.copy()
    elif op == "JUMP":
        out = [0, 0, 0, 0] if regA == [0, 0, 0, 0] else [1, 1, 1, 1]  # Mock jump
    else:
        out = [0, 0, 0, 0]

def shift_left(reg):
    reg.pop(0)
    reg.append(random.randint(0,1))

def draw():
    screen.fill(BLACK)
    draw_bits(regA, START_X, START_Y, "Reg A")
    draw_bits(regB, START_X, START_Y + 80, "Reg B")
    draw_bits(out, START_X, START_Y + 160, "OUT")

    # Instruction label
    ins = INSTRUCTIONS[instruction_pointer]
    txt = font.render(f"Instruction: {ins}", True, YELLOW)
    screen.blit(txt, (START_X, START_Y + 240))

    # Mode
    mode = "STEP" if step_mode else "CLOCK (4Hz)"
    mode_txt = font.render(f"Mode: {mode}", True, WHITE)
    screen.blit(mode_txt, (START_X, START_Y + 280))

def main():
    global instruction_pointer, step_mode, auto_clock, last_tick

    running = True
    while running:
        clock.tick(FPS)
        now = time.time()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and step_mode:
                    execute_instruction()
                elif event.key == pygame.K_c:
                    step_mode = not step_mode
                elif event.key == pygame.K_SPACE:
                    auto_clock = not auto_clock
                elif event.key == pygame.K_i:
                    instruction_pointer = (instruction_pointer + 1) % len(INSTRUCTIONS)
                elif event.key == pygame.K_1:
                    shift_left(regA)
                elif event.key == pygame.K_2:
                    shift_left(regB)

        if not step_mode and auto_clock and (now - last_tick) >= 1/CLOCK_SPEED:
            execute_instruction()
            last_tick = now

        draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

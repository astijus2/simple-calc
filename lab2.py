import pygame
import sys, os
import math





#print("\033[?25h", end="")
input("Press Enter to exit...")
os.system('clear')
sys.exit()




















"""
big_spinner = [frame_1, frame_2, frame_3, frame_4]

for i in range(5):
    for frame in big_spinner:
        print(frame, flush=True)      # 1. Print the 3-line frame
        time.sleep(0.2)               # 2. Wait
        print("\033[3A", end="")
"""


"""
spinner = ["|", "/", "-", "\\"]
flush = False
#print("Loading... ", end="")
print("\033[?25l", end="")
for i in range(5):
    print("|", end="\b", flush=True)
    time.sleep(0.2)
    print("/", end="\b", flush=True)
    time.sleep(0.2)
    print("-", end="\b", flush=True)
    time.sleep(0.2)
    print("\\", end="\b", flush=True)
"""
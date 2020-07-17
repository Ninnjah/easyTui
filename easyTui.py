import time
import os

#os.system("mode con cols=width lines=height")
#os.system('color 0A')  0 - BACKGROUND, A - TEXT
#
#   COLORS
#
# 0 = BLACK     8 = GRAY
# 1 = BLUE      9 = BRIGHT-BLUE
# 2 = GREEN     A = BRIGHT-GREEN
# 3 = CYAN      B = BRIGHT-CYAN
# 4 = RED       C = BRIGHT-RED
# 5 = PURPLE    D = BRIGHT-PURPLE
# 6 = YELLOW    E = BRIGHT-YELLOW
# 7 = WHITE     F = BRIGHT-WHITE
#

def title(title):
    length = len(title) + 6
    print('=' * length)
    print('--', title, '--')
    print('=' * length)

def label(label):
    length = len(label) + 6
    print('\n')
    print(' ', label)
    print('-' * length)

def score(name, score):
    length = len(name) + len(str(score)) + 10
    print('\n', name, ': ', score, '  ')
    print('-'* length)

def updatingScore (name, score, freq):
    print(name, ': ', score, '  ', end='\r')
    time.sleep(freq)
    
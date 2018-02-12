from display import *
from draw import *

import random

screen = new_screen()
color = [ 0, 255, 0 ]

def rand(x):
    return random.randint(0,x)

for i in range(100):
    x = rand(500)
    y = rand(500)
    draw_line(x, y, 250, 500, screen, [0, rand(255), rand(255)])
    draw_line(500-x, y, 250, 500, screen, [0, rand(255), rand(255)])

display(screen)
save_extension(screen, 'img.png')

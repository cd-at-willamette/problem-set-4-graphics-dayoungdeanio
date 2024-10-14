########################################
# Name: D'Ante Dean
# Estimated time spent (hrs): 3 Hours
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 35
BRICK_HEIGHT = 32
BRICKS_IN_BASE = 13

def draw_pyramid():
    gw = GWindow(WIDTH, HEIGHT)
    
    start_y = HEIGHT - BRICK_HEIGHT * BRICKS_IN_BASE

    for row in range(BRICKS_IN_BASE):
        #Number of bricks in current row
        n_bricks = BRICKS_IN_BASE - row
        
        #horizontal starting position to center the row
        start_x = (WIDTH - n_bricks * BRICK_WIDTH) // 2

        for brick in range(n_bricks):
            #position for each brick
            x = start_x + brick * BRICK_WIDTH
            y = start_y + row * BRICK_HEIGHT
            
            #Draw the brick
            brick_rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            brick_rect.set_filled(True)
            gw.add(brick_rect)

#My pyramid shapes like an actually pyramid instead of upside down like how you had it on the demo, idk if thats correct.


# Call the function to run
draw_pyramid()


















if __name__ == '__main__':
    draw_pyramid()

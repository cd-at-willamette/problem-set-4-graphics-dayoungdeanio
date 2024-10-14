########################################
# Name: D'Ante Dean
# Estimate time spent (hrs):I dont remember, did it piece by piece over the weekend
########################################

from pgl import GWindow, GRect, GLabel
import random

GW_WIDTH = 300                     
GW_HEIGHT = 300                    
SQUARE_SIZE = 30                    
SCORE_DX = 13                       
SCORE_DY = 13                       
SCORE_FONT = "bold 40pt 'helvetica'"    # Font for score

#function to generate coordinates for the square
def get_random_position():
    x = random.randint(0, GW_WIDTH - SQUARE_SIZE)
    y = random.randint(0, GW_HEIGHT - SQUARE_SIZE)
    return x, y

def clicky_box():
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    #scoreboard set to 0
    score = 0
    score_label = GLabel(f"Score: {score}", SCORE_DX, GW_HEIGHT - SCORE_DY)
    score_label.set_font(SCORE_FONT)
    gw.add(score_label)

    #create the square in the center
    x_center = (GW_WIDTH - SQUARE_SIZE) // 2
    y_center = (GW_HEIGHT - SQUARE_SIZE) // 2
    square = GRect(x_center, y_center, SQUARE_SIZE, SQUARE_SIZE)
    square.set_filled(True)
    square.set_color("blue")
    gw.add(square)

    #callback function for mouse click events
    def on_mouse_down(event):
        nonlocal score
        if (square.get_x() <= event.get_x() <= square.get_x() + SQUARE_SIZE and
            square.get_y() <= event.get_y() <= square.get_y() + SQUARE_SIZE):
            #Move square to new location
            new_x, new_y = get_random_position()
            square.set_location(new_x, new_y)

            #increase score
            score += 1
        else:
            #Reset  score if clicked off square
            score = 0

        #update the score 
        score_label.set_label(f"Score: {score}")

    gw.add_event_listener("click", on_mouse_down)

# Call the function to run
if __name__ == '__main__':
    clicky_box()

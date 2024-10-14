############################################################
# Name: D'Ante Dean
# Est time spent (hr):Ican't remember.
############################################################

from pgl import GWindow, GRect, GPolygon

WIDTH = 600
HEIGHT = 400
STRIPE_HEIGHT = HEIGHT // 3

def draw_bahamian_flag():
    gw = GWindow(WIDTH, HEIGHT)

    # Aquamarine top 
    top_stripe = GRect(0, 0, WIDTH, STRIPE_HEIGHT)
    top_stripe.set_filled(True)
    top_stripe.set_fill_color("#00CED1")
    gw.add(top_stripe)
    
    # Gold 
    middle_stripe = GRect(0, STRIPE_HEIGHT, WIDTH, STRIPE_HEIGHT)
    middle_stripe.set_filled(True)
    middle_stripe.set_fill_color("#FFD700")
    gw.add(middle_stripe)
    
    # Aquamarine bottom 
    bottom_stripe = GRect(0, 2 * STRIPE_HEIGHT, WIDTH, STRIPE_HEIGHT)
    bottom_stripe.set_filled(True)
    bottom_stripe.set_fill_color("#00CED1")
    gw.add(bottom_stripe)
    
    # Black triangle
    triangle = GPolygon()
    triangle.add_vertex(0, 0)                      
    triangle.add_vertex(0, HEIGHT)                 
    triangle.add_vertex(WIDTH // 3, HEIGHT // 2)   
    triangle.set_filled(True)
    triangle.set_fill_color("black")
    gw.add(triangle)
    
# Call the function to run
draw_bahamian_flag()


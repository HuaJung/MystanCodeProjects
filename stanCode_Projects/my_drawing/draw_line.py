"""
File: draw_line.py
Name: HJ
-------------------------
This file makes 2 clicks to draw a line by GOval and GLine
first click is a circle which disappears where the second click connects and becomes a line.
"""
import xml.dom

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GOval
SIZE = 5

# Global variables
window = GWindow(title='draw a line')
first_click = True
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(clicks)


def clicks(m):
    """
    identify whether the first click by true-false switch to create the fist circle when true
    and second click to draw a line and remove the circle when false
    """
    global circle, first_click
    if first_click:
        window.add(circle, m.x-circle.width/2, m.y-circle.height/2)
        first_click = False
    else:
        line = GLine(circle.x, circle.y, m.x, m.y)
        window.add(line)
        window.remove(circle)
        first_click = True



if __name__ == "__main__":
    main()

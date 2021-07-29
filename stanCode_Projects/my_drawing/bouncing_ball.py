"""
File: bouncing_ball.py
Name: HJ
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
bounce_ing = False
replay = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)


def bounce(m):
    global ball, window, bounce_ing, replay
    g = GRAVITY
    if not bounce_ing and replay > 0:
        bounce_ing = True
        while True:
            ball.move(VX, g)
            if ball.y + ball.height >= window.height and g > 0:
                g = -g
                g *= REDUCE
            if ball.x + ball.width >= window.width:
                break
            g += GRAVITY
            pause(DELAY)
        window.add(ball, START_X, START_Y)
        replay -= 1
        bounce_ing = False











if __name__ == "__main__":
    main()

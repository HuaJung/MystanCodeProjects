"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Player must remove all bricks by the paddle within 3 attempts
which one live is deducted once the ball dropped down outside the GWindow.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphics
from campy.graphics.gobjects import GRect

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    This program plays a Python game 'breakout'
    The ball will be bouncing around by the paddle, bricks, and the wall of GWindow
    When the ball hits and removes all bricks, mission is clear, but if players use up 3 lives, game will be over
    """
    graphics = BreakoutGraphics(paddle_width=80, paddle_height=12, brick_cols=16, brick_rows=5)
    window = graphics.get_window()
    vx = graphics.get_dx()
    vy = graphics.get_dy()
    ball = graphics.get_ball()
    lives = NUM_LIVES
    speed_up = False
    # Add animation loop here!
    while True:
        if graphics.game_start:
            ball.move(vx, vy)
        if graphics.collision() or ball.y <= 0:
            # vertical bounce when hitting on the paddle or bricks
            vy = -vy
        # higher the score faster the ball speed
        if 100 <= graphics.get_score() <= 300 and not speed_up:
            vy = vy * 1.5
            speed_up = True
        if graphics.get_score() > 300 and speed_up:
            vy = vy * 1.2
            speed_up = False
        if graphics.get_num_bricks() == 0:
            break
        if ball.x <= 0 or ball.x >= window.width-ball.width:
            # horizon bounce when reaching right or left side of GWindow
            vx = -vx
        if ball.y >= window.height:  # ball drops out of the bottom of GWindow
            lives -= 1
            if lives > 0:
                graphics.game_start = False
                graphics.reset_ball()
            else:
                break
        pause(FRAME_RATE)
    if graphics.get_num_bricks() == 0:
        graphics.clear()
    if lives == 0:
        graphics.game_over()


# def lives_icon(window):
# # add lives icon



if __name__ == '__main__':
    main()

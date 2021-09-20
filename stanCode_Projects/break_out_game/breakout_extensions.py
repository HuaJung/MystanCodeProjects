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
from campy.graphics.gobjects import GRect, GOval, GPolygon

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    This program plays a Python game 'breakout'
    The ball will be bouncing around by the paddle, bricks, and the wall of GWindow
    When the ball hits and removes all bricks, mission is clear, but if players use up 3 lives, game will be over
    """
    graphics = BreakoutGraphics(paddle_height=12, brick_cols=10, brick_rows=10)
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
        if 50 <= graphics.get_score() <= 300 and not speed_up:
            vy = vy * 1.5
            speed_up = True
        if 300 < graphics.get_score() <= 600 and speed_up:
            vy = vy * 1.2
            speed_up = False
        if 600 < graphics.get_score() <= 1000 and not speed_up:
            vy = vy * 1.03
            speed_up = True
        if graphics.get_score() > 1000 and speed_up:
            vy = vy * 1.01
            speed_up = False
        if graphics.get_num_bricks() == 0:
            break
        if ball.x <= 0 or ball.x >= window.width-ball.width:
            # horizon bounce when reaching right or left side of GWindow
            vx = -vx
        if ball.y >= window.height:  # ball drops out of the bottom of GWindow
            if lives == 3:
                window.remove(graphics.get_live3())
            elif lives == 2:
                window.remove(graphics.get_live2())
            elif lives == 1:
                window.remove(graphics.get_live1())
            else:
                break
            lives -= 1
            graphics.game_start = False
            graphics.reset_ball()
        pause(FRAME_RATE)
    if graphics.get_num_bricks() == 0:
        graphics.clear()
    if lives == 0:
        graphics.game_over()


# def remove_live(live_bar_lst, window):
#     live_obj = live_bar_lst.pop()
#     live = window.get_object_at(live_obj.x, live_obj.y)
#     window.remove(live)


# def hearts_icon(window, ball):
#     heart_size = 0.65 * ball.width
#     for i in range(NUM_LIVES):
#         heart_r = GOval(heart_size, heart_size)
#         heart_l = GOval(heart_size, heart_size,)
#         heart_r.filled = True
#         heart_l.filled = True
#         tri = GPolygon()
#         tri.add_vertex((window.width - 8 - (i * (2 * heart_size + 8)), window.height - 7.6 - 1.3 * heart_size))
#         tri.add_vertex((window.width - 8 - heart_size - (i * (2 * heart_size + 8)), window.height - 10))
#         tri.add_vertex((window.width - 8 - 2 * heart_size - (i * (2 * heart_size + 8)),
#                         window.height - 7.6 - 1.3 * heart_size))
#         tri.filled = True
#
#         window.add(heart_l, x=window.width - (8 + 2 * heart_size) - (i * (2 * heart_size + 8))
#                           , y=window.height - 10 - 1.32 * heart_size - heart_size // 2)
#         window.add(heart_r, x=window.width - (8 + heart_size) - (i * (2 * heart_size + 8))
#                           , y=window.height - 10 - 1.32 * heart_size - heart_size // 2)
#         window.add(tri)
#     return True

if __name__ == '__main__':
    main()

"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Create the game 'breakout' setting including bricks, a paddle, a ball, and default speed.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    """
    Set up the 'breakout' game in GWindow, equipped with bricks, a paddle, a ball, and default speed.
    """
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 5 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.__window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.__paddle = GRect(paddle_width, paddle_height)
        self.__paddle_x_position = (window_width-paddle_width)/2
        self.__paddle_y_position = window_height-paddle_offset
        self.__paddle.filled = True
        self.__paddle.fill_color = 'darkgray'
        self.__paddle.color = 'darkgray'
        self.__window.add(self.__paddle, self.__paddle_x_position, self.__paddle_y_position)

        # Center a filled ball in the graphical window
        self.__ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.__ball.filled = True
        self.__ball.fill_color = 'hotpink'
        self.__ball.color = 'hotpink'
        self.__window.add(self.__ball, (window_width - self.__ball.width) / 2, (window_height - self.__ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        self.game_start = False   # set a True-False switch to avoid mouse clicked interruption
        onmouseclicked(self.race_start)
        onmousemoved(self.paddle_move)

        # add score label
        self.__score = 0
        self.__score_label = GLabel('SCORE: '+str(self.__score))
        self.__score_label.font = '-20-bold'
        self.__window.add(self.__score_label, 2, 23)

        # Draw bricks
        self.__b_c = brick_cols
        self.__b_r = brick_rows
        self.__b_s = brick_spacing
        self.__b_o = brick_offset
        self.__num_bricks = self.__b_c * self.__b_r
        for i in range(self.__b_r):
            for j in range(self.__b_c):
                self.__bricks = GRect(brick_width, brick_height)
                self.__bricks.filled = True
                self.__window.add(self.__bricks, j * (brick_width + self.__b_s)
                                  , self.__b_o + i * (brick_height + self.__b_s))
                if i < 1:
                    self.__bricks.fill_color = 'indianred'
                    self.__bricks.color = 'indianred'
                elif 1 <= i <= 2:
                    self.__bricks.fill_color = 'khaki'
                    self.__bricks.color = 'khaki'
                elif 3 <= i <= 4:
                    self.__bricks.fill_color = 'mediumaquamarine'
                    self.__bricks.color = 'mediumaquamarine'
                elif 5 <= i <= 6:
                    self.__bricks.fill_color = 'darksage'
                    self.__bricks.color = 'darksage'
                elif i >= 7:
                    self.__bricks.fill_color = 'deepskyblue'
                    self.__bricks.color = 'deepskyblue'

    def clear(self):
        """
        when all bricks are removed, GWindow shows 'Clear'
        """
        canvas = GRect(self.__window.width, self.__window.height)
        canvas.filled = True
        canvas.fill_color = 'papayawhip'
        canvas.color = 'papayawhip'
        label = GLabel('CLEAR')
        label.font = '-90'
        label.color = 'pink'
        final_score = GLabel('SCORE: '+str(self.__score))
        final_score.font = '-30-bold'
        self.__window.add(canvas, 0, 0)
        self.__window.add(label, (self.__window.width-label.width)/2, self.__window.height/2)
        self.__window.add(final_score, (self.__window.width-final_score.width)/2, self.__window.height/2
                          + label.height)

    def game_over(self):
        """
        when lives are used up, GWindow shows 'Game Over'
        """
        canvas = GRect(self.__window.width, self.__window.height)
        canvas.filled = True
        canvas.fill_color = 'grey'
        canvas.color = 'grey'
        self.__window.add(canvas, 0, 0)
        label = GLabel('GAME OVER')
        label.font = '-100'
        label.color = 'maroon'
        final_score = GLabel('SCORE: '+str(self.__score))
        final_score.font = '-30-bold'
        self.__window.add(label, (self.__window.width-label.width)/2, (self.__window.height+label.height)/2)
        self.__window.add(final_score, (self.__window.width - final_score.width) / 2, self.__window.height / 2
                          + label.height)

    def collision(self):
        """
        the ball hits the brick, removing it and bouncing, while only bounces when hitting the paddle
        """
        # make the ball's 4 coordinates as check points
        check_point1 = self.__window.get_object_at(self.__ball.x, self.__ball.y)
        check_point2 = self.__window.get_object_at(self.__ball.x + self.__ball.width, self.__ball.y)
        check_point3 = self.__window.get_object_at(self.__ball.x, self.__ball.y + self.__ball.height)
        check_point4 = self.__window.get_object_at(self.__ball.x + self.__ball.width, self.__ball.y + self.__ball.height)
        if check_point1 is not None and check_point1 is not self.__score_label:
            if self.__ball.y >= self.__paddle.y - self.__ball.height:  # ball reaches the paddle
                self.__ball.y = self.__paddle.y - self.__ball.height  # reposition the ball over the paddle
            else:  # ball reaches the brick
                if check_point1.y >= self.__b_o+(self.__bricks.height+self.__b_s)*(self.__b_r-2):
                    self.__window.remove(check_point1)
                    self.__num_bricks -= 1
                    self.__score += 5
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
                elif self.__b_o+(self.__bricks.height+self.__b_s)*(self.__b_r-4) <= check_point1.y < self.__b_o\
                        + (self.__bricks.height+self.__b_s)*(self.__b_r-2):
                    self.__window.remove(check_point1)
                    self.__num_bricks -= 1
                    self.__score += 10
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
                elif check_point1.y < self.__b_o+(self.__bricks.height + self.__b_s)*(self.__b_r-4):
                    self.__window.remove(check_point1)
                    self.__num_bricks -= 1
                    self.__score += 15
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
            return True
        elif check_point2 is not None and check_point2 is not self.__score_label:
            if self.__ball.y >= self.__paddle.y - self.__ball.height:  # ball reaches the paddle
                self.__ball.y = self.__paddle.y - self.__ball.height   # reposition the ball over the paddle
            else:  # ball reaches the brick
                if check_point2.y >= self.__b_o+(self.__bricks.height+self.__b_s)*(self.__b_r-2):
                    self.__window.remove(check_point2)
                    self.__num_bricks -= 1
                    self.__score += 5
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
                elif self.__b_o+(self.__bricks.height+self.__b_s)*(self.__b_r-4) <= check_point2.y < self.__b_o\
                        + (self.__bricks.height+self.__b_s)*(self.__b_r-2):
                    self.__window.remove(check_point2)
                    self.__num_bricks -= 1
                    self.__score += 10
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
                elif check_point2.y < self.__b_o+(self.__bricks.height + self.__b_s) * (self.__b_r-4):
                    self.__window.remove(check_point2)
                    self.__num_bricks -= 1
                    self.__score += 15
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
            return True
        elif check_point3 is not None and check_point3 is not self.__score_label:
            if self.__ball.y >= self.__paddle.y - self.__ball.height:  # ball reaches the paddle
                self.__ball.y = self.__paddle.y - self.__ball.height   # reposition the ball over the paddle
            else:  # ball reaches the brick
                if check_point3.y >= self.__b_o + (self.__bricks.height + self.__b_s) * (self.__b_r - 2):
                    self.__window.remove(check_point3)
                    self.__num_bricks -= 1
                    self.__score += 5
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
                elif self.__b_o + (self.__bricks.height + self.__b_s) * (self.__b_r - 4) <= check_point3.y \
                        < self.__b_o + (self.__bricks.height + self.__b_s) * (self.__b_r - 2):
                    self.__window.remove(check_point3)
                    self.__num_bricks -= 1
                    self.__score += 10
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
                elif check_point3.y < self.__b_o + (self.__bricks.height + self.__b_s) * (self.__b_r - 4):
                    self.__window.remove(check_point3)
                    self.__num_bricks -= 1
                    self.__score += 15
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
            return True
        elif check_point4 is not None and check_point4 is not self.__score_label:
            if self.__ball.y >= self.__paddle.y - self.__ball.height:  # ball reaches the paddle
                self.__ball.y = self.__paddle.y - self.__ball.height   # reposition the ball over the paddle
            else:  # ball reaches the brick
                if check_point4.y >= self.__b_o + (self.__bricks.height + self.__b_s) * (self.__b_r - 2):
                    self.__window.remove(check_point4)
                    self.__num_bricks -= 1
                    self.__score += 5
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
                elif self.__b_o + (self.__bricks.height + self.__b_s) * (self.__b_r - 4) <= check_point4.y \
                        < self.__b_o + (self.__bricks.height + self.__b_s) * (self.__b_r - 2):
                    self.__window.remove(check_point4)
                    self.__num_bricks -= 1
                    self.__score += 10
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
                elif check_point4.y < self.__b_o + (self.__bricks.height + self.__b_s) * (self.__b_r - 4):
                    self.__window.remove(check_point4)
                    self.__num_bricks -= 1
                    self.__score += 15
                    self.__score_label.text = 'SCORE: ' + str(self.__score)
            return True

    def race_start(self, event):
        """
        turn on the game_start switch as True for the first click
        """
        if not self.game_start:
            self.game_start = True

    def paddle_move(self, event):
        """
        the paddle can only move within the width of GWindow and the same horizon
        """
        self.__paddle.x = event.x - self.__paddle.width / 2
        self.__paddle.y = self.__paddle_y_position
        if event.x >= self.__window.width - self.__paddle.width / 2:
            self.__paddle.x = self.__window.width - self.__paddle.width
        if event.x <= self.__paddle.width / 2:
            self.__paddle.x = 0

    def reset_ball(self):
        self.__window.add(self.__ball, (self.__window.width-self.__ball.width)/2, (self.__window.height/3))

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def get_ball(self):
        return self.__ball

    def get_window(self):
        return self.__window

    def get_num_bricks(self):
        return self.__num_bricks

    def get_score(self):
        return self.__score


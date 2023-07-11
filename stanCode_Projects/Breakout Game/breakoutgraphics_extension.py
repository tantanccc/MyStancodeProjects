"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    # constructor
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=(window_height - paddle_offset))
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - ball_radius) / 2, y=(window_height - ball_radius) / 2)
        self.ball_radius = ball_radius

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.move_paddle)

        # Draw bricks
        for row in range(brick_rows):  # use "for loop" to create many bricks
            for col in range(brick_cols):
                x = col * (brick_width + brick_spacing)
                y = row * (brick_height + brick_spacing) + brick_offset
                self.brick = GRect(brick_width, brick_height, x=x, y=y)  # set size and position for brick
                self.brick.filled = True  # fill color
                if row in range(0, 2):  # set color
                    self.brick.fill_color = '#005F73'
                elif row in range(2, 4):
                    self.brick.fill_color = '#94D2BD'
                elif row in range(4, 6):
                    self.brick.fill_color = '#E9D8A6'
                elif row in range(6, 8):
                    self.brick.fill_color = '#EE9B00'
                elif row in range(8, 10):
                    self.brick.fill_color = '#BB3E03'
                self.window.add(self.brick)  # add brick

        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset

        # create score board
        self.score = 0
        self.score_label = GLabel('Score:' + str(self.score))
        self.score_label.font = '-15'
        self.window.add(self.score_label, x=20, y=self.score_label.height+20)

    # method
    def move_paddle(self, mouse):
        """
        let paddle moves with mouse
        """
        if mouse.x >= (self.window.width - self.paddle_width / 2):
            self.paddle.x = self.window.width - self.paddle_width
        elif mouse.x <= (0 + self.paddle_width / 2):
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - (self.paddle_width / 2)
            self.paddle.y = self.window.height - self.paddle_offset  # method 1, use "self.paddle_offset"

    def set_ball_velocity(self, _):
        """
        set ball velocity
        """
        if self.__dx == 0 and self.__dy == 0:  # make sure the ball is static
            self.__dx = random.randint(1, MAX_X_SPEED)  # randomly choose x velocity value
            if random.random() > 0.5:  # randomly negating x velocity direction
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
        else:
            pass

    def move_ball(self):
        """
        move the ball with velocity
        """
        self.ball.move(self.__dx, self.__dy)

    def handle_wall_collisions(self):
        """
        handle left, right and up side wall collision
        """
        if self.ball.x <= 0 or self.ball.x >= (self.window.width - self.ball.width):
            self.__dx *= -1
        elif self.ball.y <= 0:
            self.__dy *= -1

    def handle_down_wall_collisions(self):
        """
        handle down side wall fall out
        """
        ball_out = False
        if self.ball.y >= (self.window.height - self.ball.height):
            ball_out = True
            self.__dx = 0
            self.__dy = 0
            self.window.add(self.ball, x=(self.window.width - self.ball_radius) / 2,
                            y=(self.window.height - self.ball_radius) / 2)
        return ball_out

    def remove_brick(self):
        """
        remove the brick, bounce off if touch the paddle, update score board
        """
        object_at_point1 = self.window.get_object_at(self.ball.x, self.ball.y)
        object_at_point2 = self.window.get_object_at(self.ball.x + self.ball.width * 2, self.ball.y)
        object_at_point3 = self.window.get_object_at(self.ball.x + self.ball.width * 2,
                                                     self.ball.y + self.ball.height * 2)
        object_at_point4 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height * 2)

        for i_object in [object_at_point1, object_at_point2, object_at_point3, object_at_point4]:
            if i_object is not None and i_object is not self.score_label:  # can be brick or paddle, both need change velocity direction
                self.__dx *= -1
                self.__dy *= -1
                if i_object is not self.paddle and i_object is not self.score_label:
                    self.window.remove(i_object)
                    self.score += 1
                    self.score_label.text = 'Score:' + str(self.score)    # update/ modify score board
                break

    def change_paddle_color(self):
        """
        change paddle color when getting a higher score
        """
        if self.score in range(5, 10):
            self.paddle.fill_color = '#AE2012'
        elif self.score >= 10:
            self.paddle.fill_color = '#E76F51'

    def increase_ball_velocity(self):
        """
        increase ball velocity gradually when over score 3
        """
        if self.score >= 3:
            self.__dx *= 1.0005
            self.__dy *= 1.0005

    def get_vx(self):
        """
        get velocity in x direction
        """
        return self.__dx

    def get_vy(self):
        """
        get velocity in y direction
        """
        return self.__dy

    def detect_bricks(self):
        no_bricks = False
        detector = 0
        for row in range(self.brick_rows):  # use "for loop" to create many bricks
            for col in range(self.brick_cols):
                x = col * (self.brick_width + self.brick_spacing)
                y = row * (self.brick_height + self.brick_spacing) + self.brick_offset
                if self.window.get_object_at(x, y) is not None:
                    detector += 1
        if detector == 0:
            no_bricks = True
        return no_bricks









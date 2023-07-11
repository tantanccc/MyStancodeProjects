"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        if graphics.handle_down_wall_collisions():
            lives -= 1
            if lives <= 0:             # game over condition 1
                break
        if graphics.detect_bricks():   # game over condition 1
            break
        graphics.move_ball()
        graphics.handle_wall_collisions()
        graphics.remove_brick()
        graphics.change_paddle_color()
        graphics.increase_ball_velocity()

        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

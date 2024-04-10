import pygame
from random import *
import time


class Rect:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def getMiddle(self):
        mid_x = self.x + (self.width//2)
        mid_y = self.y + (self.height//2)
        return mid_x, mid_y

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x,
                                              self.y, self.width, self.height))


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def getMiddle(self):
        return self.x, self.y

    def setCoords(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def draw(self, window):
        pygame.draw.circle(window, self.color,
                           self.getMiddle(), self.radius, 40)


def do_simulation():
    # Initialize Pygame
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 32)
    goal_txt = font.render("Possible Goal", True, (255, 255, 255))
    fail_txt = font.render("No possible goal", True, (255, 255, 255))

    # Set up the window
    window_width = 800
    window_height = 600

    ball_size = 30

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pygame Scene")

    # Set up the rectangle
    goal = Rect((window_width - 400) // 2,
                (window_height - 100) // 2, randint(100, 700), 100, (0, 255, 0))

    blocker = Rect((window_width - randint(0, 600)) //
                   2, (window_height - goal.height) // 2, randint(20, 400), 100, (255, 0, 0))

    ball = Ball(window_width//2, window_height-100, ball_size, (255, 165, 0))
    rectangle_color = (0, 255, 0)  # Red

    open_color = (0, 0, 255)

    area1 = Rect(0, 0, 0, 0, (0, 0, 255))
    area2 = Rect(0, 0, 0, 0, (0, 0, 255))

    items = [goal, blocker]

    if (blocker.x > goal.x):
        area1 = Rect(goal.x, goal.y+goal.height,
                     blocker.x-goal.x, 100, (0, 0, 255))

        items.append(area1)

    if (blocker.x + blocker.width < goal.x + goal.width):
        area2 = Rect(blocker.x+blocker.width, goal.y+goal.height,
                     (goal.x+goal.width)-(blocker.x+blocker.width), 100, (0, 0, 255))
        items.append(area2)

    if (area1.width > area2.width):
        target = area1
        area2.color = (255, 255, 0)
    else:
        target = area2
        area1.color = (255, 255, 0)

    target_area = (-1, -1)
    if (target.width > ball_size):
        ball.setCoords(target.getMiddle())
        ball.y -= 100
        target_area = target.getMiddle()
        target_area = (target_area[0], target_area[1] - 100)

    items.append(ball)

    # Game loop
    running = True
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill((0, 0, 0))  # Black
    for item in items:
        item.draw(window=window)
        # Update the window

    if (target_area != (-1, -1)):
        pygame.draw.line(window, (255, 255, 255),
                         (window_width//2, window_height - 100), target_area)
        window.blit(goal_txt, (window_width//2, window_height-50))
    else:
        window.blit(goal_txt, (window_width//2, window_height-50))

    pygame.display.flip()
    # Quit Pygame
    time.sleep(3)
    pygame.quit()


def main():
    for i in range(10):
        do_simulation()


if __name__ == '__main__':
    main()

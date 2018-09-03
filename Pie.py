import math
import pygame, sys
from pygame.locals import *


class Pie():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 500))
        pygame.display.set_caption("The Pie Game - Press 1, 2, 3, 4")
        self.my_font = pygame.font.Font(None, 60)

        self.x = 300
        self.y = 250
        self.width = 4
        self.color = 200, 80, 60
        self.redius = 200
        self.position = self.x-self.redius, \
                        self.y-self.redius, self.redius*2, self.redius*2

        self.piece1 = False
        self.piece2 = False
        self.piece3 = False
        self.piece4 = False

    def write_blit(self, text, x, y):
        textImage1 = self.my_font.render(text, True, self.color)
        self.screen.blit(textImage1, (x, y))

    def draw_sector(self, start, end, line1_start, line1_end, line2_start, line2_end):
        pygame.draw.arc(self.screen, self.color, self.position, math.radians(start),
                        math.radians(end), self.width)
        pygame.draw.line(self.screen, self.color, line1_start, line1_end, self.width)
        pygame.draw.line(self.screen, self.color, line2_start, line2_end, self.width)


if __name__ == "__main__":
    pie = Pie()
    pygame.init()
    pygame.display.set_caption("The Pie Game - Press 1, 2, 3, 4")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_1:
                    pie.piece1 = True
                elif event.key == pygame.K_2:
                    pie.piece2 = True
                elif event.key == pygame.K_3:
                    pie.piece3 = True
                elif event.key == pygame.K_4:
                    pie.piece4 = True

        pie.screen.fill((0, 0, 200))
        pie.write_blit('1', pie.x + pie.redius / 2 - 20, pie.y - pie.redius / 2)
        pie.write_blit('2', pie.x - pie.redius / 2, pie.y - pie.redius / 2)
        pie.write_blit('3', pie.x - pie.redius / 2, pie.y + pie.redius / 2 - 20)
        pie.write_blit('4', pie.x + pie.redius / 2 - 20, pie.y + pie.redius / 2 - 20)

        if pie.piece1:
            pie.draw_sector(0, 90, (pie.x, pie.y), (pie.x, pie.y-pie.redius),
                            (pie.x, pie.y), (pie.x + pie.redius, pie.y))
        if pie.piece2:
            pie.draw_sector(90, 180, (pie.x, pie.y), (pie.x, pie.y-pie.redius),
                            (pie.x, pie.y), (pie.x - pie.redius, pie.y))

        if pie.piece3:
            pie.draw_sector(180, 270, (pie.x, pie.y), (pie.x - pie.redius, pie.y),
                            (pie.x, pie.y), (pie.x, pie.y + pie.redius))

        if pie.piece4:
            pie.draw_sector(270, 360, (pie.x, pie.y), (pie.x, pie.y + pie.redius),
                            (pie.x, pie.y), (pie.x + pie.redius, pie.y))

        if pie.piece1 and pie.piece2 and pie.piece3 and pie.piece4:
            pie.color = 0, 255, 0

        pygame.display.update()
import pandas as pd
import numpy as np
import pygame
import agent

# define global arguments for visual properties
WIDTH = 1200
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
GREY = (127, 127, 127)
TARGET = [(400, 200), (400, 600), (800, 600), (800, 200)]

class FirstExp(object):
    def __init__(self):
        # screen parameters
        pygame.init()
        size = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode(size)
        self.font = pygame.font.SysFont("Arial", 20)

        # experiments parameters
        self.ISI = 200
        self.display_time = 500
        self.instruction_msg = "Put you fingers on the left and right keys. Click on one of them to start the game"

    def display_text_on_screen(self, text_str):
        text = self.font.render(text_str, True, GREY, BLACK)
        textrect = text.get_rect()
        textrect.centerx = self.screen.get_rect().centerx
        textrect.centery = self.screen.get_rect().centery
        self.screen.blit(text, textrect)
        pygame.display.flip()

    def wait_for_left_right_press(self):
        pygame.event.clear()
        continue_flag = True
        while continue_flag:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        cur_key = "left"
                        continue_flag = False
                    if event.key == pygame.K_RIGHT:
                        cur_key = "right"
                        continue_flag = False
        pygame.event.clear()
        return cur_key

    def start_exp(self):
        # show the instruction
        self.display_text_on_screen(self.instruction_msg)
        self.wait_for_left_right_press()


        # black screen
        self.screen.fill(BLACK)
        pygame.display.flip()
        pygame.time.delay(self.ISI)

        # present target
        pygame.draw.polygon(self.screen, CYAN, TARGET)
        pygame.display.flip()
        pygame.time.delay(self.display_time)

        # clear the keys
        pygame.event.clear()


if __name__ == "__main__":
    game = FirstExp()
    game.start_exp()

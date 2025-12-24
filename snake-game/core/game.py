import pygame
import itertools

from core.grid import Grid
from render.renderer import Renderer
from entities.snake import Snake
from entities.food import Food

ROWS = 10
COLS = 10
CELL_SIZE = 50

class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.grid = Grid(ROWS, COLS, CELL_SIZE)
        self.renderer = Renderer(self.screen, self.grid)
        self.snake = Snake()
        self.tick_ms = 200
        self.acc_ms = 0
        self.state = "PLAYING"
        self.clock = pygame.time.Clock()
        self.food = Food(self.grid.random_free_cell(set(self.snake.body)))
        self.score = 0

        self.walls = True

    def reset(self):
        self.snake = Snake()
        self.acc_ms = 0
        self.state = "PLAYING"
        self.score = 0

    def run(self):
        running = True
        # self.walls = False 

        # playper_pos = pygame.Vector2(self.screen.get_width()/2,self.screen.get_height()/2)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q and self.state != "PLAYING":
                        running = False
                    if event.key == pygame.K_r and self.state == "GAME_OVER":
                        self.reset()
                    if event.key == pygame.K_p and self.state != "GAME_OVER":
                        self.state = "PAUSED" if self.state == "PLAYING" else "PLAYING"
                    # if event.key == pygame.K_p and self.state == "PAUSED":
                    #     self.state = "PLAYING"

                    if event.key == pygame.K_w:
                        self.snake.set_direction((0,-1))
                    elif event.key == pygame.K_s:
                        self.snake.set_direction((0,1))
                    elif event.key == pygame.K_a:
                        self.snake.set_direction((-1,0))
                    elif event.key == pygame.K_d:
                        self.snake.set_direction((1,0))

            dt = self.clock.tick(60) # milliseconds since last frame
            if self.state == "PLAYING":
                self.acc_ms += dt
                if self.acc_ms >= self.tick_ms:
                    self.snake.step(ROWS, COLS, self.walls)
                    snake_head = self.snake.head()
                    # Eats food
                    if snake_head == self.food.pos:
                        self.score += 1
                        self.snake.grow(1)
                        self.food.pos = self.grid.random_free_cell(set(self.snake.body))

                    # self collison
                    snake_body_without_head = set(itertools.islice(self.snake.body, 1, None))
                    if snake_head in snake_body_without_head:
                        self.state = "GAME_OVER"

                    self.acc_ms -= self.tick_ms
                    if self.walls and not self.grid.in_bounds(self.snake.head()):
                        self.state = "GAME_OVER"


            self.renderer.draw_bg()
            self.renderer.draw_grid()
            self.renderer.draw_snake(self.snake)
            self.renderer.draw_food(self.food)
            self.renderer.draw_score(self.score)

            if self.state == "GAME_OVER":
                self.renderer.draw_game_over()
            if self.state == "PAUSED":
                self.renderer.draw_paused()

            pygame.display.flip()

        pygame.quit()
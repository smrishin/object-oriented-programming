import pygame

class Renderer:
    def __init__(self, screen, grid) -> None:
        self.screen = screen
        self.grid = grid
        self.font_big = pygame.font.SysFont(None, 64)
        self.font_sm = pygame.font.SysFont(None, 32)
    
    def draw_bg(self):
        self.screen.fill((30,30,30))
    
    def draw_grid(self):
        for x in range(self.grid.cols):
            for y in range(self.grid.rows):
                rect = pygame.Rect(
                    x * self.grid.cell_size,
                    y * self.grid.cell_size,
                    self.grid.cell_size,
                    self.grid.cell_size
                )
                pygame.draw.rect(self.screen, (40,0,0), rect, 1)

    def draw_snake(self, snake):
        head = True
        for x, y in snake.body:
            px, py = self.grid.to_pixels((x, y))
            s = pygame.Rect(
                px, py, self.grid.cell_size, self.grid.cell_size

            )
            if head:
                pygame.draw.rect(self.screen, (0,0,200), s)
                head = False
            else:
                pygame.draw.rect(self.screen, (0,200,0), s)

    def draw_food(self, food):
        x,y = food.pos
        px, py = self.grid.to_pixels((x, y))
        f = pygame.Rect(
            px, py, self.grid.cell_size, self.grid.cell_size
        )
        pygame.draw.rect(self.screen, (200, 50, 50), f)
    
    def draw_score(self, score):
        score_text = self.font_big.render("SCORE", True, (255, 255, 255))
        score_val = self.font_big.render(f"{score}", True, (255, 255, 255))

        tw, th = score_text.get_size()
        vw, vh = score_val.get_size()

        cx = self.screen.get_width() // 2
        cy = self.screen.get_height() // 2

        grid_width = self.grid.cell_size * self.grid.cols
        sidebar_width = self.screen.get_width() - grid_width
        sidebar_tw_placement = grid_width + (sidebar_width - tw) // 2
        sidebar_vw_placement = grid_width + (sidebar_width - vw) // 2


        self.screen.blit(score_text, (sidebar_tw_placement , cy - th // 2 - 40))
        self.screen.blit(score_val, (sidebar_vw_placement, cy - th // 2 + 10))

    def draw_game_over(self):
        game_over_text = self.font_big.render("GAME OVER", True, (255, 255, 255))
        restart_hint = self.font_sm.render("Press R to restart", True, (200, 200, 200))
        quit_hint = self.font_sm.render("Press Q to Quit", True, (200, 200, 200))

        tw, th = game_over_text.get_size()
        rw, rh = restart_hint.get_size()
        qw, qh = quit_hint.get_size()

        grid_width = self.grid.cell_size * self.grid.cols
        grid_height = self.screen.get_height() // 2

        self.screen.blit(game_over_text, ((grid_width - tw) // 2, grid_height - th // 2 - 20))
        self.screen.blit(restart_hint, ((grid_width - rw) // 2, grid_height + 20))
        self.screen.blit(quit_hint, ((grid_width - qw) // 2, grid_height + 60))

    def draw_paused(self):
        paused_text = self.font_big.render("PAUSED", True, (255, 255, 255))
        unpause_hint = self.font_sm.render("Press P to Unpause", True, (200, 200, 200))
        quit_hint = self.font_sm.render("Press Q to Quit", True, (200, 200, 200))

        tw, th = paused_text.get_size()
        rw, rh = unpause_hint.get_size()
        qw, qh = quit_hint.get_size()

        grid_width = self.grid.cell_size * self.grid.cols
        grid_height = self.screen.get_height() // 2

        self.screen.blit(paused_text, ((grid_width - tw) // 2, grid_height - th // 2 - 20))
        self.screen.blit(unpause_hint, ((grid_width - rw) // 2, grid_height + 20))
        self.screen.blit(quit_hint, ((grid_width - qw) // 2, grid_height + 60))

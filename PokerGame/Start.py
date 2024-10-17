from hand import *
from cards import *
from general_settings import *
import ctypes, pygame, sys

#maintaining resolution
#ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.hand = Hand()

    def run(self):
        self.start_time = pygame.time.get_ticks()

        while True:
            #Quitting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_down = True
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if mouse_down == True:
                            mouse_down = False
                            self.hand = Hand()

        self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
        self.start_time = pygame.time.get_ticks()
        pygame.display.update()
        self.screen.fill(BGcol)
        
        self.hand.update()
        self.clock.tick(FPS)



if __name__ == '__main__':
    game = Game()
    game.run()
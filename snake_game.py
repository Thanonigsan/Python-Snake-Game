import pygame
from random import randint
from pygame.locals import K_d, K_a, K_w, K_s
import time

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

dialogue_font = pygame.font.SysFont('arial', 15)
name_font = pygame.font.SysFont('Helvetica', 20)
game_over_font = pygame.font.SysFont('Verdana', 60)

dialogue = dialogue_font.render("Hello Guys!",
                                True, (255,0,0))
name = name_font.render("Quantum Byte Systems-Nigsan", True, (255,255,0))
game_over = game_over_font.render("Game Over", True, (0,0,255))

class Player:
    x = 0
    y = 0
    d = 0
    positions = []
    length = 4
    
class Apple:
    x = 0
    y = 0

class Game:
    game_width = 10
    game_height = 10
    grid_size = 44
    
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1>=x2 and x1<=x2+bsize:
            if y1>=y2 and y1<=y2+bsize:
                return True
        return False
    
    def __init__(self):
        self._running = True
        self.player = Player()
        self.apple = Apple()
        
        self.apple.x = randint(0,self.game_width)*self.grid_size
        self.apple.y = randint(0,self.game_height)*self.grid_size
        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((640,480), pygame.HWSURFACE)
        pygame.display.set_caption('Snake Game')
        self._background = pygame.image.load("background.png").convert()
        self._snake_image = pygame.image.load("snake.png").convert()
        self._apple_image = pygame.image.load("apple.png").convert()
        self.dialogue_font = pygame.font.SysFont('arial', 15)
        self.name_font = pygame.font.SysFont('Helvetica', 30)
        self.game_over_font = pygame.font.SysFont('Verdana', 60)
        
    def on_render(self):
        self._display_surf.blit(self._background, (0, 0))
        
        for pos in self.player.positions:
            self._display_surf.blit(self._snake_image,(pos[0],pos[1]))
            
        self._display_surf.blit(self._apple_image,(self.apple.x,self.apple.y))
        
        name = self.name_font.render("Quantum Byte Systems-Nigsan", True, (255,255,55))
        self._display_surf.blit(name, (200,400))
            
        pygame.display.flip()
          
    def on_cleanup(self):
        pygame.quit()
               
    def snake_logic(self):
        if self.player.d == 0:
            self.player.x += 44
        elif self.player.d == 1:
            self.player.x -= 44
        elif self.player.d == 2:
            self.player.y -= 44
        elif self.player.d == 3:
            self.player.y += 44
                  
        if len(self.player.positions) < self.player.length:
            self.player.positions.append((self.player.x,self.player.y))
        else:
            self.player.positions.pop(0)
            self.player.positions.append((self.player.x,self.player.y))
            
    def game_play_logic(self):        
        if self.isCollision(self.player.x,self.player.y,self.apple.x,self.apple.y, 44):
            print('collides')
            self.apple.x = randint(0,self.game_width)*self.grid_size
            self.apple.y = randint(0,self.game_height)*self.grid_size
            self.player.length += 1
                
        if len(self.player.positions)>self.player.length-1:
            for i in range(0,self.player.length-1):
                if self.isCollision(self.player.x,self.player.y,self.player.positions[i][0],self.player.positions[i][1],40):
                    print('GAME OVER')
                    exit()                
        
    def game_logic(self):
        self.snake_logic()
        self.game_play_logic()
                   
    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    
            keys = pygame.key.get_pressed()
            
            if keys[K_d]:
                self.player.d = 0
                              
            if keys[K_a]:
                self.player.d = 1
                
            if keys[K_w]:
                self.player.d = 2
                
            if keys[K_s]:
                self.player.d = 3
                
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
    
        while self._running:
            self.handle_events()
            self.game_logic()                                        
            self.on_render()
            time.sleep(0.3)
            
        self.on_cleanup()
        
if __name__ == "__main__" :
    game = Game()
    game.on_execute()
from pygame import *


window = display.set_mode((700,700))
display.set_caption("Pinhponh")
clock = time.Clock() 
game = True
class GameSprite(sprite.Sprite):
    def __init__(self, x , y ,h, w , imegname, run ):
        super().__init__()
        self.image = transform.scale(image.load(imegname), (w , h))
        self.speed = run
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        












while game :

    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255,255,255))


    display.update()
    clock.tick(70)

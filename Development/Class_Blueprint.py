
class Mario :

    _Lives = 3

    def_init_(self, Lives)
    
        self._Lives = Lives

    _speed = 30.0

    def Walk(Me) :
        print("Hello World!")
        print("Lives are: ", self._Lives)

myMario = Mario(3)

print("Lives: " + myMario._lives)



mario1 = Mario()

mario2 = Mario()

mario2.Walk()
mario2._Lives = 5

print("Mario 1's Lives: ", mario1._Lives)
print("mario 2's Lives: ", mario2._Lives)


class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
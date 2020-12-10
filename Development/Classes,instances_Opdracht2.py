class character():

    speed = 10
    points = 0
    sprite = 0
    Health = 20

    def _init_(self) :
        print("The constructor of the character")

    def Walk(self) :
        print("Character is walking", self.speed)

class Mario (character) :

    Lives = 3
    item = None
    sprite = 1

    def Jump(self) :
        print("Mario Jumps up in the air!")
    
    def _init_(self) :

        super()._init_()

        self.speed = 5

        self.Health = 10

    def Walk(self) :
        print("Mario walks differently", self.speed)
    
    def Alive(self) :
        print("Mario has this many lives : ", self.Lives)









class CleverMario (Mario) :
    
    iq = 200

    def Walk(self):
        super().Walk()
        print("And i hope i'm clever")




CharacterA = character()
MarioX = Mario()

CharacterA.Walk()
MarioX.Walk()

print(CharacterA.speed)
print(MarioX.speed)
print(MarioX.Lives)
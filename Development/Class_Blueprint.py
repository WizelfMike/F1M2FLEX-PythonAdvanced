
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


class robot:
    def __init__(self,name):
        self.name=name
        self.position=[0,0]
        print("My name is :",self.name)

    def walk(self,x):
        self.position[0]=self.position[0]+x
        print("new Position:",self.position)
    def eat(self):
        print("I Am Hungry!")

class Robot_Dog(robot):
    def make_noice(self):
        print("Woof! Woof!")
    def eat(self):
        super().eat()
        print("i like meat")

rob = Robot_Dog("jack")
rob.walk(10)
rob.make_noice()
rob.eat()

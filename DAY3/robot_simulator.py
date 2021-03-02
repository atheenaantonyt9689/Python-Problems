EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4

class Robot:


    def __init__ (self,direction=NORTH,x=0,y=0):
        self.direction=direction
        self.x=x
        self.y=y
        self.coordinates=(self.x,self.y)

    def move(self,instructions):
        for i in instructions:
            if self.direction == "R":
                Robot.turn_right(self)
            elif self.direction == "L":
                Robot.turn_left(self)
            elif self.direction =="A":
                Robot.advance(self)
    
    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH
    
    def turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = NORTH
    def advance(self):
        if self.direction == NORTH:
            self.x = self.x + 1
        if self.direction == SOUTH:
            self.x = self.x -1
        if self.direction == EAST:
            self.y =self.y+1
        if self.direction == WEST:
            self.y =self.y -1

        

    
    

robot= Robot(EAST,1,1)
robot.move("RAALAL")


        






        




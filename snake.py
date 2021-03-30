from turtle import Turtle

BOUNDARY = 280
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    """
    Creates a snake game. The time variable essentially determines the speed of the game, the smaller the faster
    the game.
    """
    def __init__(self):
        self.turtles_ = []  # Default value
        self.create_snake()

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self, positions):
        turtle_ = Turtle(shape='square')
        turtle_.color('white')
        turtle_.penup()
        turtle_.goto(positions)
        self.turtles_.append(turtle_)

    def reset_snake(self):
        for t in self.turtles_:
            t.goto(1000,1000)
        self.turtles_.clear()
        self.create_snake()

    def grow(self):
        self.add_segment(self.turtles_[-1].position())

    def snake_move(self):
        for t in range(len(self.turtles_)):
            if len(self.turtles_)-1-t == 0:
                self.turtles_[0].forward(MOVING_DISTANCE)
            else:
                self.turtles_[len(self.turtles_)-1-t].setpos(self.turtles_[len(self.turtles_)-2-t].pos())

    def down(self):
        if self.turtles_[0].heading() == UP:
            return
        self.turtles_[0].setheading(DOWN)

    def up(self):
        if self.turtles_[0].heading() == DOWN:
            return
        self.turtles_[0].setheading(UP)

    def left(self):
        if self.turtles_[0].heading() == RIGHT:
            return
        self.turtles_[0].setheading(LEFT)

    def right(self):
        if self.turtles_[0].heading() == LEFT:
            return
        self.turtles_[0].setheading(RIGHT)

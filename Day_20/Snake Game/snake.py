from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """Create the initial snake."""
        for position in STARTING_POSITIONS:
            self.create_segment(position)

    def create_segment(self, position):
        """Create one segment."""
        segment = Turtle("square")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def extend(self):
        """Add a new segment at the end."""
        self.create_segment(self.snake_body[-1].position())

    def move(self):
        for segment in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
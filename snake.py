from turtle import Turtle

startpos = [(0, 0), (-20, 0), (-40, 0)]
move_dist = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in startpos:
            self.add_segment(pos)
    def add_segment(self,pos):
        new_segment = Turtle("square")  # segment_1.color("white")
        new_segment.color("white")
        new_segment.penup()  # segment_2 = Turtle("square")
        new_segment.goto(pos)
        # segment_2.color("white")
        self.segments.append(new_segment)  # segment_2.goto(-20, 0)
        # segment_3 = Turtle("square")
        # segment_3.color("white")
        # segment_3.goto(-40, 0)
        # segment_1 = Turtle("square")  # t1.shape("square")x
    def extend(self):
        #add a new segment to snake
       self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

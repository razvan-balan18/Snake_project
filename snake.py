from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def move(self):
        for seg_num in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[seg_num - 1].xcor()
            new_y = self.seg[seg_num - 1].ycor()
            self.seg[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.seg.append(new_seg)

    def extend(self):
        self.add_segment(self.seg[-1].position())

    def reset_snake(self):
        for segment in self.seg:
            segment.goto(1000, 1000)
        self.seg.clear()
        self.create_snake()
        self.head = self.seg[0]

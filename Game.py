# simple snake game
# Part-1
import turtle
import time
import random

 # Set up the screen
wn = turtle.Screen()
wn.title("Game by Gauthami")
wn.bgcolor("yellow")
wn.setup(width=400, height=400)
wn.tracer(0)

 # Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape('turtle')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'stop'


# Create target
target = turtle.Turtle()
target.speed(0)
target.shape('square')
target.color('red')
target.penup()
target.goto(0, 100)

segment = []

class directions()
# functions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"
def move():
    if head.direction == 'up':
       y = head.ycor()
       head.sety(y + 30)
    if head.direction == 'down':
       y = head.ycor()
       head.sety(y - 30)
    if head.direction == 'left':
       x = head.xcor()
       head.setx(x + 30)
    if head.direction == 'right':
       x = head.xcor()
       head.setx(x - 30)

# keyboard binding
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Right")
wn.onkey(go_right, "Left")

 # main game loop
while True:
      wn.update()
      if head.distance(target) < 20:
      # move target to  random spots
         x =  random.randint(-190, 190)
         y = random.randint(-190, 190)
         target.goto(x, y)
         # add segment
         new_segment = turtle.Turtle()
         new_segment.speed(0)
         new_segment.shape('turtle')
         new_segment.color('black')
         new_segment.penup()
         segment.append(new_segment)

      # move the segment in reverse Order
      for index in range(len(segment)-1, 0 ,-1):
          x = segment[index-1].xcor()
          y = segment[index - 1].ycor()
          segment[index].goto(x,y)

      # move segment 0 to where head is
      if len(segment) > 0:
          x = head.xcor()
          y = head.ycor()
          segment[0].goto(x,y)
      move()
      delay = 0.1
      time.sleep(delay)

turtle.mainloop()

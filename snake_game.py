# snake game by @Harshdeep_Singh
# step 1 setup the screen
# step 2 make the snake head
# step 3 make snake food
# step 4 make snake body
# step 5 border collision
# step 6 body collision
# step 7 scoring
# step 8 add sound effects


import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# setup of the game
wn = turtle.Screen()
wn.title('Snake game by @Harshdeep Singh')
wn.bgcolor('yellow')
wn.setup(width=1000, height=1000)
# stops the screen updates


# snake head
head = turtle.Turtle()
head.shape('circle')
head.speed(0)
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# snake food
food = turtle.Turtle()
food.shape('turtle')
food.speed(0)
food.color('green')
food.penup()
food.goto(0, 100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 410)
pen.write("Score: 0   High score: 0", align="center", font=("Courier", 24, "normal"))


# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# mainlooop
while True:
    wn.update()
    # check for a collision with borders
    if head.xcor() > 1000 or head.xcor() < -1000 or head.ycor() > 1000 or head.ycor() < -1000:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segments
        segments.clear()

        # Reset the score
        score = 0

        pen.clear()
        pen.write("Score: {} High Sore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # check for a collission with a food
    if head.distance(food) < 20:
        # move head to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(0, 100)
        segments.append(new_segment)

        # shorten delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Sore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move the segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        segments[0].goto(x, y)

    move()

    # CHECK FOR THE COLLISIONS OF HEAD WITH BODY SEGMENTS
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments
            segments.clear()

            # Reset the score
            score = 0

            pen.clear()
            pen.write("Score: {} High Sore: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()







# pong.py Version 0.1.0.0015
# Copyright (c) 2018 Christopher D. Pedersen. All rights reserved.

import turtle
import random
import math

# launch game window
window = turtle.Screen()
# set screensize in pixels and set background color
window.screensize(500, 500, "black")

# create ping pong ball
ball = turtle.Turtle()
# set the ping pong ball's properties
ball.shape("circle")
ball.fillcolor("white")
ball.penup() # move position without drawing on the canvas/window
ball.setposition(0, 0)

# create left ping pong paddle
# REFERENCE (move turtle without drawing line): https://stackoverflow.com/questions/36550242/python-turtle-delete-line
leftPaddle = turtle.Turtle()
# 'speed' at which python will render or draw the ping pong paddle
# By setting the speed to zero, python will render the paddle instantaneously
leftPaddle.speed(0)
leftPaddle.penup() # move position without drawing on the canvas/window
leftPaddle.setposition(-300, 0)
leftPaddle.shape("square")
leftPaddle.shapesize(4.5, 1, 0)
leftPaddle.fillcolor("white")

# create function to move left paddle up
def moveLeftPaddleUp():
    y = leftPaddle.ycor() # get y-axis coordinate of leftPaddle
    y = y + 100 # move y-axis coordinate up 100 pixels
    # set upward boundary of 300 pixels/prevents paddle from moving up indefinitely
    if y <= 300:
        leftPaddle.sety(y) # move left paddle to new position on the y-axis

# create function to move left paddle up
def moveLeftPaddleDown():
    y = leftPaddle.ycor() # get y-axis coordinate of leftPaddle
    y = y - 100 # move y-axis coordinate down 100 pixels
    # set lower boundary of -300 pixels/prevents paddle from moving down indefinitely
    if y >= -300:
        leftPaddle.sety(y) # move left paddle to new position on the y-axis

# create keyboard bindings that listen for up and down button presses
turtle.listen() # instruct turtle module to listen for keyboard events (btn presses)
# bind up button press to function that moves the left paddle up
turtle.onkey(moveLeftPaddleUp, "Up")
# bind down button press to function that moves the left paddle down
turtle.onkey(moveLeftPaddleDown, "Down")

# create the ping pong table
# REFERENCE: https://www.youtube.com/watch?v=FdmjXnyoS0A&list=PLlEgNdBJEO-lqvqL5nNNZC6KoRdSrhQwK&index=3
table = turtle.Turtle()
# 'speed' at which python will render or draw the ping pong table
# By setting the speed to zero, python will render the table instantaneously
table.speed(0)
table.color("white") # ping pong table border color
table.penup() # move position without drawing on the canvas/window
table.setposition(-350, -350)
table.pendown() # place 'pen' down to draw on canvas/window
table.pensize(3) # 'pen' size in pixels
# draw bottom border of ping pong table
table.fd(700) # draw on canvas by moving pen 700 pixels forward
table.lt(90) # rotate pen direction 'left turn' 90 degrees
# draw right border of ping pong table
table.fd(700) # draw on canvas by moving pen 700 pixels forward
table.lt(90) # rotate pen direction 'left turn' 90 degrees
# draw top border of ping pong table
table.fd(700) # draw on canvas by moving pen 700 pixels forward
table.lt(90) # rotate pen direction 'left turn' 90 degrees
# draw left border of ping pong table
table.fd(700) # draw on canvas by moving pen 700 pixels forward
table.lt(90) # rotate pen direction 'left turn' 90 degrees
# end drawing ping pong table
table.hideturtle()

# Main Game Loop
directionOfTravel = "left"
coinToss = random.randint(1, 2)
if coinToss == 1:
    rise = random.randint(1, 100) * 1.0
elif coinToss == 2:
    rise = random.randint(1, 100) * -1.0
run = -100.0
speed = 10.0
serve = True
while True:
    x = ball.xcor() * 1.0 # get x-axis coordinate of ball (multiply by 1.0 to typecast as float)
    y = ball.ycor() * 1.0 # get y-axis coordinate of ball (multiply by 1.0 to typecast as float)

    # DETECT PADDLE STRIKE (BALL MAKING CONTACT WITH PADDLE)
    paddle_y_coordinate = leftPaddle.ycor() # get y-axis coordinate of leftPaddle
    paddle_x_coordinate = leftPaddle.xcor() # get x-axis coordinate of leftPaddle
    if x >= paddle_x_coordinate - 20 and x <= paddle_x_coordinate + 20 and y >= paddle_y_coordinate - 50 and y <= paddle_y_coordinate + 50:
        # Ball has struck the paddle, so change the direction of travel by
        # reversing the run of the slope. For example a run of -5 will become 5
        run = run * -1.0

        # Pythagorean Theorem: a**2 + b**2 == c**2
        a_squared = rise * rise
        b_squared = run * run
        c_squared = a_squared + b_squared
        c = math.sqrt(c_squared)

        # We use a multiplier to make sure the ball travels a constant speed
        # If a multiplier isn't used the ball will travel erratically
        multiplier = speed / c

        # Update X & Y Axis Coordinates & Move Ball
        x = x + (run * multiplier)
        y = y + (rise * multiplier)
        ball.setx(x)
        ball.sety(y)
        # DO NOT RUN THE REST OF THE LOOP, INSTEAD BREAK AND BEGIN EXECUTION
        # OF THE WHILE LOOP AGAIN FROM THE TOP (continue)
        continue

    # DETECT BOUNDARY STRIKES (BOTTOM, TOP, RIGHT, & LEFT EDGES OF THE PING PONG TABLE)
    # CONDITION: GAME HAS JUST BEGUN, BALL IS IN CENTER OF TABLE TRAVELING LEFT
    # NOTE: THIS MARKS THE START OF THE GAME
    if x == 0:
        # Update X & Y Axis Coordinates & Move Ball

        # Pythagorean Theorem: a**2 + b**2 == c**2
        a_squared = rise * rise
        b_squared = run * run
        c_squared = a_squared + b_squared
        c = math.sqrt(c_squared)

        # We use a multiplier to make sure the ball travels a constant speed
        # If a multiplier isn't used the ball will travel erratically
        multiplier = speed / c

        # Update X & Y Axis Coordinates & Move Ball
        x = x + (run * multiplier)
        y = y + (rise * multiplier)
        ball.setx(x)
        ball.sety(y)
    elif x > -350 and x < 350 and y < 350 and y > -350:
        # Update X & Y Axis Coordinates & Move Ball
        # Pythagorean Theorem: a**2 + b**2 == c**2
        a_squared = rise * rise
        b_squared = run * run
        c_squared = a_squared + b_squared
        c = math.sqrt(c_squared)

        # We use a multiplier to make sure the ball travels a constant speed
        # If a multiplier isn't used the ball will travel erratically
        multiplier = speed / c

        # Update X & Y Axis Coordinates & Move Ball
        x = x + (run * multiplier)
        y = y + (rise * multiplier)
        ball.setx(x)
        ball.sety(y)
    # CONDITION: BALL HAS HIT LEFT BOUNDARY
    elif x <= -350:
        # Ball has hit the left boundary, so change the direction of travel by
        # reversing the run of the slope. For example a run of -5 will become 5
        run = run * -1
        # Update X & Y Axis Coordinates & Move Ball
        # Pythagorean Theorem: a**2 + b**2 == c**2
        a_squared = rise * rise
        b_squared = run * run
        c_squared = a_squared + b_squared
        c = math.sqrt(c_squared)

        # We use a multiplier to make sure the ball travels a constant speed
        # If a multiplier isn't used the ball will travel erratically
        multiplier = speed / c

        # Update X & Y Axis Coordinates & Move Ball
        x = x + (run * multiplier)
        y = y + (rise * multiplier)
        ball.setx(x)
        ball.sety(y)
    # CONDITION: BALL HAS HIT RIGHT BOUNDARY
    elif x >= 350:
        # Ball has hit the right boundary, so change the direction of travel by
        # reversing the run of the slope. For example a run of -5 will become 5
        run = run * -1
        # Update X & Y Axis Coordinates & Move Ball
        # Pythagorean Theorem: a**2 + b**2 == c**2
        a_squared = rise * rise
        b_squared = run * run
        c_squared = a_squared + b_squared
        c = math.sqrt(c_squared)

        # We use a multiplier to make sure the ball travels a constant speed
        # If a multiplier isn't used the ball will travel erratically
        multiplier = speed / c

        # Update X & Y Axis Coordinates & Move Ball
        x = x + (run * multiplier)
        y = y + (rise * multiplier)
        ball.setx(x)
        ball.sety(y)
    # CONDITION: BALL HAS HIT TOP BOUNDARY
    elif y >= 350:
        # Ball has hit the top boundary, so change the direction of travel by
        # reversing the rise of the slope. For example a rise of -5 becomes 5
        rise = rise * -1.0
        # Update X & Y Axis Coordinates & Move Ball
        # Pythagorean Theorem: a**2 + b**2 == c**2
        a_squared = rise * rise
        b_squared = run * run
        c_squared = a_squared + b_squared
        c = math.sqrt(c_squared)

        # We use a multiplier to make sure the ball travels a constant speed
        # If a multiplier isn't used the ball will travel erratically
        multiplier = speed / c

        # Update X & Y Axis Coordinates & Move Ball
        x = x + (run * multiplier)
        y = y + (rise * multiplier)
        ball.setx(x)
        ball.sety(y)
    # CONDITION: BALL HAS HIT BOTTOM BOUNDARY
    elif y <= -350:
        # Ball has hit the bottom boundary, so change the direction of travel by
        # reversing the rise of the slope. For example a rise of -5 becomes 5
        rise = rise * -1.0
        # Update X & Y Axis Coordinates & Move Ball
        # Pythagorean Theorem: a**2 + b**2 == c**2
        a_squared = rise * rise
        b_squared = run * run
        c_squared = a_squared + b_squared
        c = math.sqrt(c_squared)

        # We use a multiplier to make sure the ball travels a constant speed
        # If a multiplier isn't used the ball will travel erratically
        multiplier = speed / c

        # Update X & Y Axis Coordinates & Move Ball
        x = x + (run * multiplier)
        y = y + (rise * multiplier)
        ball.setx(x)
        ball.sety(y)

# TODO: Implement Bouncing Algorithm
# Bouncing Algorithm Reference: http://www.101computing.net/bouncing-algorithm/

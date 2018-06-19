# pong.py Version 0.2.1.0001
# Copyright (c) 2018 Christopher D. Pedersen. All rights reserved.

# TODO: Make Computer Opponent Beat-able
# TODO: Make Serves Less Predictable (ball currently served in same direction if player misses serve)
# TODO: Tweak Randomly Generated Ball Trajectories (random rise/run currently generated when ball hits the end of paddles)

import turtle
import random
import math
import time

player1points = 0
player2points = 0

# set ball speed to zero (ball speed will be changed to 10.0 when the game starts)
speed = 0.0

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

# create opponent (right) ping pong paddle
# REFERENCE (move turtle without drawing line): https://stackoverflow.com/questions/36550242/python-turtle-delete-line
rightPaddle = turtle.Turtle()
# 'speed' at which python will render or draw the ping pong paddle
# By setting the speed to zero, python will render the paddle instantaneously
rightPaddle.speed(0)
rightPaddle.penup() # move position without drawing on the canvas/window
rightPaddle.setposition(300, 0)
rightPaddle.shape("square")
rightPaddle.shapesize(4.5, 1, 0)
rightPaddle.fillcolor("white")

# create function to move left paddle up
def moveRightPaddleUp():
    y = rightPaddle.ycor() # get y-axis coordinate of leftPaddle
    y = y + 100 # move y-axis coordinate up 100 pixels
    # set upward boundary of 300 pixels/prevents paddle from moving up indefinitely
    if y <= 300:
        rightPaddle.sety(y) # move left paddle to new position on the y-axis

# create function to move left paddle up
def moveRightPaddleDown():
    y = rightPaddle.ycor() # get y-axis coordinate of leftPaddle
    y = y - 100 # move y-axis coordinate down 100 pixels
    # set lower boundary of -300 pixels/prevents paddle from moving down indefinitely
    if y >= -300:
        rightPaddle.sety(y) # move left paddle to new position on the y-axis

# Create Player 1 Scoreboard 'Pen'
# This 'pen' will be used to draw player 1's scoreboard and update the score
# as the player scores throughout the game
player1ScoreBoardPen = turtle.Turtle()
player1ScoreBoardPen.speed(0)
player1ScoreBoardPen.penup() # move position without drawing on the canvas/window
player1ScoreBoardPen.setposition(-150, 200)
player1ScoreBoardPen.ht() # hide turtle
player1ScoreBoardPen.pencolor("white")
player1ScoreBoardPen.pendown()
# player1ScoreStr = str(player1points)

# Create Player 2 Scoreboard 'Pen'
# This 'pen' will be used to draw player 1's scoreboard and update the score
# as the player scores throughout the game
player2ScoreBoardPen = turtle.Turtle()
player2ScoreBoardPen.speed(0)
player2ScoreBoardPen.penup() # move position without drawing on the canvas/window
player2ScoreBoardPen.setposition(150, 200)
player2ScoreBoardPen.ht() # hide turtle
player2ScoreBoardPen.pencolor("white")
player2ScoreBoardPen.pendown()
# player2ScoreStr = str(player2points)

# Create Pen to Write 'Press Spacebar to Begin'
# This 'pen' will be used to draw player 1's scoreboard and update the score
# as the player scores throughout the game
spaceBarPen = turtle.Turtle()
spaceBarPen.speed(0)
spaceBarPen.penup() # move position without drawing on the canvas/window
spaceBarPen.setposition(0, -250)
spaceBarPen.ht() # hide turtle
spaceBarPen.pencolor("white")
spaceBarPen.pendown()
spaceBarPen.write("Press Spacebar to Begin New Game", align="center", font=("Arial", 24, "normal"))

# Create Pen to Write 'Use Up & Down Arrow Keys to Move Paddle'
# This 'pen' will be used to draw player 1's scoreboard and update the score
# as the player scores throughout the game
instructionsPen = turtle.Turtle()
instructionsPen.speed(0)
instructionsPen.penup() # move position without drawing on the canvas/window
instructionsPen.setposition(0, -275)
instructionsPen.ht() # hide turtle
instructionsPen.pencolor("white")
instructionsPen.pendown()
instructionsPen.write("Use Up & Down Arrow Keys to Move Paddle", align="center", font=("Arial", 18, "normal"))

# This method will cause the game to start when the user hits the spacebar.
# The main gameloop is waiting for the variable runGame to equal true before it
# will start executing the main gameplay logic. So this method works by simply
# changing the value of runGame from False to True.
runGame = False
firstGame = True
def startGame():
    global runGame
    global speed
    global firstGame
    global player1points
    global player2points
    global player1ScoreBoardPen
    global player2ScoreBoardPen
    # Execute this code block if this is the users very first game...
    if runGame == False and firstGame == True:
        speed = 10.0
        runGame = True
        spaceBarPen.undo() # remove 'Press Spacebar to Begin'
        instructionsPen.undo() # remove 'Use Up & Down Arrows to Move Paddle'
        player1ScoreStr = str(player1points)
        player2ScoreStr = str(player2points)
        player1ScoreBoardPen.write(player1ScoreStr, font=("Arial", 48, "normal"))
        player2ScoreBoardPen.write(player2ScoreStr, font=("Arial", 48, "normal"))
        firstGame = False
    # Execute this code if the user presses the space bar in the middle of the game
    elif runGame == True and firstGame == False:
        print("User pressed spacebar in middle of game, do nothing...")
    # Execute this code block if the user is trying to begin a new game
    elif runGame == False and firstGame == False:
        speed = 10.0
        runGame = True
        spaceBarPen.undo() # remove 'Press Spacebar to Begin'
        instructionsPen.undo() # remove 'Use Up & Down Arrow Keys to Move Paddle'
        player1ScoreBoardPen.undo() # Erase old score
        player2ScoreBoardPen.undo() # Erase old score
        player1ScoreStr = str(player1points)
        player2ScoreStr = str(player2points)
        player1ScoreBoardPen.write(player1ScoreStr, font=("Arial", 48, "normal"))
        player2ScoreBoardPen.write(player2ScoreStr, font=("Arial", 48, "normal"))

def endGame():
    global runGame
    global speed
    global player1points
    global player2points
    # reset score (will not appear on screen until new game begins)
    player1points = 0
    player2points = 0
    speed = 0.0
    runGame = False
    spaceBarPen.write("Press Spacebar to Begin New Game", align="center", font=("Arial", 24, "normal"))
    instructionsPen.write("Use Up & Down Arrow Keys to Move Paddle", align="center", font=("Arial", 18, "normal"))

# create keyboard bindings that listen for up and down button presses
turtle.listen() # instruct turtle module to listen for keyboard events (btn presses)
# bind up button press to function that moves the left paddle up
turtle.onkey(moveLeftPaddleUp, "Up")
# bind down button press to function that moves the left paddle down
turtle.onkey(moveLeftPaddleDown, "Down")
# bind space bar to function that starts game
turtle.onkey(startGame, "space")

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

# Initialize Ball Trajectory Variables
coinToss = random.randint(1, 2)
if coinToss == 1:
    rise = random.randint(1, 100) * 1.0
elif coinToss == 2:
    rise = random.randint(1, 100) * -1.0
run = -100.0
# speed variable is declared earlier in the program, see above

# Initialize Computer Opponent's Gameplay Variables
currentGameLoopIterationCount = 0
lastMove = 0

alwaysTrue = True
while True:
    # if alwaysTrue == True doesn't mean anything. I indented several
    # hundred lines of code before so that I could add an if-statement here,
    # but later needed to remove the if-statement and didn't feel like removing
    # 300 lines of indentation.
    if alwaysTrue == True:
        x = ball.xcor() * 1.0 # get x-axis coordinate of ball (multiply by 1.0 to typecast as float)
        y = ball.ycor() * 1.0 # get y-axis coordinate of ball (multiply by 1.0 to typecast as float)

        # DETECT LEFT PADDLE STRIKE (BALL MAKING CONTACT WITH PADDLE)
        paddle_y_coordinate = leftPaddle.ycor() # get y-axis coordinate of leftPaddle
        paddle_x_coordinate = leftPaddle.xcor() # get x-axis coordinate of leftPaddle
        if x >= paddle_x_coordinate - 15 and x <= paddle_x_coordinate + 15 and y >= paddle_y_coordinate - 50 and y <= paddle_y_coordinate + 50:
            # Ball has struck the paddle, so change the direction of travel by
            # reversing the run of the slope. For example a run of -5 will become 5
            run = run * -1.0

            # If the ball strikes the paddle with zero rise, give the ball a little
            # rise to prevent the ball from bouncing back and forth indefinitely
            if rise == 0:
                if random.randint(1, 2) == 1:
                    rise = 10.0
                else:
                    rise = -10.0

            # Get the absolute values of rise
            if rise < 0:
                absoluteValueOfRise = rise * -1.0
            else:
                absoluteValueOfRise = rise
            # Get the absolute value of run
            if run < 0:
                absoluteValueOfRun = run * -1.0
            else:
                absoluteValueOfRun = run

            # If the ball strikes the paddle at an extreme angle, straighten the
            # ball out a little bit so it doesn't keep bounce up and down vertically
            # the whole game.
            if (absoluteValueOfRise / absoluteValueOfRun) > 1:
                if random.randint(1, 2) == 1:
                    rise = run
                else:
                    rise = run * 0.67

            # If the ball hits either of the ends of the paddle, magnify the rise
            # a little bit to make the game a little less predictable
            if y > (paddle_y_coordinate + 25):
                yetAnotherRandomNumber = random.randint(1, 3)
                if yetAnotherRandomNumber == 1:
                    rise = rise * 1.25
                elif yetAnotherRandomNumber == 2:
                    rise = rise * 1.50
                if yetAnotherRandomNumber == 3:
                    rise = rise * 1.75
            elif y < (paddle_y_coordinate - 25):
                yetAnotherRandomNumber = random.randint(1, 3)
                if yetAnotherRandomNumber == 1:
                    rise = rise * 1.25
                elif yetAnotherRandomNumber == 2:
                    rise = rise * 1.50
                if yetAnotherRandomNumber == 3:
                    rise = rise * 1.75

            # Pythagorean Theorem: a**2 + b**2 == c**2
            a_squared = rise * rise
            b_squared = run * run
            c_squared = a_squared + b_squared
            c = math.sqrt(c_squared)

            # We use a multiplier to make sure the ball travels a constant speed
            # If a multiplier isn't used the ball will travel erratically
            multiplier = speed / c

            # Update X & Y Axis Coordinates
            # Note Regarding Bug Fix: We increase the multiplier by 50% to give the
            # ball a little pop coming off the paddle. However, the ball will only
            # move at this 50% faster speed for the immediate move after impacting
            # the paddle and then will slow back down to the regular constant speed.
            # This feature was added to fix a bug caused by the ball not moving far
            # away enough from the paddle immediately after impact.
            x = x + (run * (multiplier * 5.0))
            y = y + (rise * (multiplier * 5.0))
            ball.setposition(x, y)
            # DO NOT RUN THE REST OF THE LOOP, INSTEAD BREAK AND BEGIN EXECUTION
            # OF THE WHILE LOOP AGAIN FROM THE TOP (continue)
            continue

        # DETECT RIGHT PADDLE STRIKE (BALL MAKING CONTACT WITH PADDLE)
        right_paddle_y_coordinate = rightPaddle.ycor() # get y-axis coordinate of rightPaddle
        right_paddle_x_coordinate = rightPaddle.xcor() # get x-axis coordinate of rightPaddle
        if x <= right_paddle_x_coordinate + 15 and x >= right_paddle_x_coordinate - 15 and y >= right_paddle_y_coordinate - 50 and y <= right_paddle_y_coordinate + 50:
            # Ball has struck the paddle, so change the direction of travel by
            # reversing the run of the slope. For example a run of -5 will become 5
            run = run * -1.0

            # If the ball strikes the paddle with zero rise, give the ball a little
            # rise to prevent the ball from bouncing back and forth indefinitely
            if rise == 0:
                if random.randint(1, 2) == 1:
                    rise = 10.0
                else:
                    rise = -10.0

            # Get the absolute values of rise
            if rise < 0:
                absoluteValueOfRise = rise * -1.0
            else:
                absoluteValueOfRise = rise
            # Get the absolute value of run
            if run < 0:
                absoluteValueOfRun = run * -1.0
            else:
                absoluteValueOfRun = run

            # If the ball strikes the paddle at an extreme angle, straighten the
            # ball out a little bit so it doesn't keep bounce up and down vertically
            # the whole game.
            if (absoluteValueOfRise / absoluteValueOfRun) > 1:
                if random.randint(1, 2) == 1:
                    rise = run
                else:
                    rise = run * 0.67

            # If the ball hits either of the ends of the paddle, magnify the rise
            # a little bit to make the game a little less predictable
            if y > (right_paddle_y_coordinate + 25):
                yetAnotherRandomNumber = random.randint(1, 3)
                if yetAnotherRandomNumber == 1:
                    rise = rise * 1.25
                elif yetAnotherRandomNumber == 2:
                    rise = rise * 1.50
                if yetAnotherRandomNumber == 3:
                    rise = rise * 1.75
            elif y < (right_paddle_y_coordinate - 25):
                yetAnotherRandomNumber = random.randint(1, 3)
                if yetAnotherRandomNumber == 1:
                    rise = rise * 1.25
                elif yetAnotherRandomNumber == 2:
                    rise = rise * 1.50
                if yetAnotherRandomNumber == 3:
                    rise = rise * 1.75

            # Pythagorean Theorem: a**2 + b**2 == c**2
            a_squared = rise * rise
            b_squared = run * run
            c_squared = a_squared + b_squared
            c = math.sqrt(c_squared)

            # We use a multiplier to make sure the ball travels a constant speed
            # If a multiplier isn't used the ball will travel erratically
            multiplier = speed / c

            # Update X & Y Axis Coordinates
            # Note Regarding Bug Fix: We increase the multiplier by 50% to give the
            # ball a little pop coming off the paddle. However, the ball will only
            # move at this 50% faster speed for the immediate move after impacting
            # the paddle and then will slow back down to the regular constant speed.
            # This feature was added to fix a bug caused by the ball not moving far
            # away enough from the paddle immediately after impact.
            x = x + (run * (multiplier * 5.0))
            y = y + (rise * (multiplier * 5.0))

            # Move Ball to new Coordinates
            ball.setposition(x, y)
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
            ball.setposition(x, y)
        elif x > -335 and x < 335 and y < 335 and y > -335:
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
            ball.setposition(x, y)
        # CONDITION: BALL HAS HIT LEFT BOUNDARY
        elif x <= -335:
            # Computer Opponent Has Scored a Point
            player2points = player2points + 1
            player2ScoreBoardPen.undo() # erase previous score
            player2ScoreBoardPen.write(str(player2points), font=("Arial", 48, "normal"))
            print("Score:")
            print("Player 1: " + str(player1points))
            print("Player 2: " + str(player2points))
            if player2points == 21:
                # BUGFIX: hideturtle, setposition, and showturtle methods added to prevent
                # the score from incrementing after a game had already been won. Before
                # this bug fix was added, the winning score of 21 would suddenly jump to 22
                ball.ht() # hide turtle while moving ball back to center screen
                ball.setposition(0, 0)
                ball.showturtle() # make ball visible again
                endGame()
            else:
                ball.ht() # hide turtle while moving ball back to center screen
                ball.setposition(0, 0)
                ball.showturtle() # make ball visible again
                leftPaddle.setposition(-300, 0)
                rightPaddle.setposition(300, 0)
                run = -100 # Serve the ball in the direction of player 2
                time.sleep(1) # pause for 2 seconds
        # CONDITION: BALL HAS HIT RIGHT BOUNDARY
        elif x >= 335:
            # Player 1 (Human User) Has Scored a Point
            player1points = player1points + 1
            player1ScoreBoardPen.undo() # erase previous score
            player1ScoreBoardPen.write(str(player1points), font=("Arial", 48, "normal"))
            print("Score:")
            print("Player 1: " + str(player1points))
            print("Player 2: " + str(player2points))
            if player1points == 21:
                # BUGFIX: hideturtle, setposition, and showturtle methods added to prevent
                # the score from incrementing after a game had already been won. Before
                # this bug fix was added, the winning score of 21 would suddenly jump to 22
                ball.ht() # hide turtle while moving ball back to center screen
                ball.setposition(0, 0)
                ball.showturtle() # make ball visible again
                endGame()
            else:
                ball.ht() # hide turtle while moving ball back to center screen
                ball.setposition(0, 0)
                ball.showturtle() # make ball visible again
                leftPaddle.setposition(-300, 0)
                rightPaddle.setposition(300, 0)
                run = 100 # Serve the ball in the direction of player 2
                time.sleep(1) # pause for 2 seconds
        # CONDITION: BALL HAS HIT TOP BOUNDARY
        elif y >= 335:
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
            x = x + (run * (multiplier * 5.0))
            y = y + (rise * (multiplier * 5.0))
            ball.setposition(x, y)
        # CONDITION: BALL HAS HIT BOTTOM BOUNDARY
        elif y <= -335:
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
            x = x + (run * (multiplier * 5.0))
            y = y + (rise * (multiplier * 5.0))
            ball.setposition(x, y)

        # COMPUTER OPPONENT'S GAME PLAY LOGIC GOES HERE (CONTROLS OPPONENT'S PADDLE)
        currentGameLoopIterationCount = currentGameLoopIterationCount + 1
        if currentGameLoopIterationCount == lastMove + 10:
            lastMove = currentGameLoopIterationCount
            # Determine which direction the paddle is headed, and move paddle
            # accordingly
            ballPosition = ball.ycor()
            upperPaddlePosition = rightPaddle.ycor() + 50
            lowerPaddlePosition = rightPaddle.ycor() - 50
            if ballPosition > upperPaddlePosition:
                # move paddle up
                moveRightPaddleUp()
            elif ballPosition < lowerPaddlePosition:
                # move paddle down
                moveRightPaddleDown()

import turtle

# Set up the screen
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Bricks
bricks = []

def create_bricks(rows, cols):
    for row in range(rows):
        for col in range(cols):
            brick = turtle.Turtle()
            brick.speed(0)
            brick.shape("square")
            brick.color("blue")
            brick.shapesize(stretch_wid=1, stretch_len=2)
            brick.penup()
            brick.goto(-290 + col * 75, 250 - row * 30)
            bricks.append(brick)

create_bricks(5, 10)

# Paddle movement
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
        paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
        paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkey(paddle_left, "Left")
win.onkey(paddle_right, "Right")

# Main game loop
while True:
    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border collision
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if (ball.xcor() > brick.xcor() - 37.5 and ball.xcor() < brick.xcor() + 37.5) and \
           (ball.ycor() > brick.ycor() - 15 and ball.ycor() < brick.ycor() + 15):
            ball.dy *= -1
            brick.goto(2000, 2000)  # Move brick off-screen
            bricks.remove(brick)

    # Check for game over
    if not bricks:
        ball.goto(0, 0)
        ball.dy = 0
        ball.dx = 0
        paddle.goto(0, -250)
        break

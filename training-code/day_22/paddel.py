from turtle import Screen, Turtle

# Screen setup
screen = Screen()
screen.bgcolor("tan")
screen.setup(width=800, height=600)
screen.title("PONG")

# Paddle 1 (Right paddle)
paddle_1 = Turtle()
paddle_1.shape("square")
paddle_1.color("black")
paddle_1.shapesize(stretch_len=1, stretch_wid=3)
paddle_1.penup()
paddle_1.goto(350, 0)

def paddle_1_up():
    new_y = paddle_1.ycor() + 20
    paddle_1.goto(paddle_1.xcor(), new_y)

def paddle_1_down():
    new_y = paddle_1.ycor() - 20
    paddle_1.goto(paddle_1.xcor(), new_y)

# Paddle 2 (Left paddle)
paddle_2 = Turtle()
paddle_2.shape("square")
paddle_2.color("black")
paddle_2.shapesize(stretch_len=1, stretch_wid=3)
paddle_2.penup()
paddle_2.goto(-350, 0)

def paddle_2_up():
    new_y = paddle_2.ycor() + 20
    paddle_2.goto(paddle_2.xcor(), new_y)
    paddle_1.speed(1)

def paddle_2_down():
    new_y = paddle_2.ycor() - 20
    paddle_2.goto(paddle_2.xcor(), new_y)
    paddle_2.speed(1)
# Ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.5

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.5
        self.bounce_x()

# Scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.l_misses = 0
        self.r_misses = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=("Courier", 24, "normal"))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("Courier", 24, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_miss(self):
        self.l_misses += 1
        self.l_point()
        if self.l_misses >= 5:
            self.goto(0, 0)
            self.write("Player 1 Wins!", align="center", font=("Courier", 36, "normal"))
            return True
        return False

    def r_miss(self):
        self.r_misses += 1
        self.r_point()
        if self.r_misses >= 5:
            self.goto(0, 0)
            self.write("Player 2 Wins!", align="center", font=("Courier", 36, "normal"))
            return True
        return False

# Ball instance
ball = Ball()
ball.goto(0, 0)

# Scoreboard instance
scoreboard = Scoreboard()

# Key bindings
screen.listen()
screen.onkey(paddle_1_up, "Up")
screen.onkey(paddle_1_down, "Down")
screen.onkey(paddle_2_up, "w")
screen.onkey(paddle_2_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddle_1) < 50 and ball.xcor() > 340) or (ball.distance(paddle_2) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # Detect when paddles miss the ball
    if ball.xcor() > 390:
        if scoreboard.l_miss():
            game_is_on = False
        ball.reset_position()

    if ball.xcor() < -390:
        if scoreboard.r_miss():
            game_is_on = False
        ball.reset_position()

screen.mainloop()

 
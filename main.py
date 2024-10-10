import turtle
import random
import time


#create a screen
screen=turtle.Screen()
screen.bgcolor("#def0c5")
screen.title("Catch The Turtle")

#write name of the game on screen
writing = turtle.Turtle()
writing.penup()
writing.clear()
writing.hideturtle()
writing.goto(0,270 )
writing.color("#0c343d")
writing.write("Catch The Turtle Game!", align="center", font=("Times New Roman",48,"normal"))

#draw the turtle
turtle_icon = turtle.Turtle()
turtle_icon.color("green")
turtle_icon.shape("turtle")
turtle_icon.shapesize(3)
turtle_icon.penup()
turtle_icon.speed(10)

def countdown_timer(seconds):
    # create a turtle for time
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("#0c343d")
    pen.penup()

    while seconds >= 0:
        # count mins and secs
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'

        # clear the screen and write present second
        pen.clear()
        pen.goto(0, 200)
        pen.write(timer, align="center", font=("Times New Roman", 45, "normal"))

        #hold a second
        time.sleep(1)
        seconds -= 1

    #after finished the time
    pen.clear()
    pen.color("red")
    pen.write("Game Over!", align="center", font=("Times New Roman", 45, "normal"))

#moves the turtle for a specified time
def move_turtle():
    x = random.randint(-300, 150)
    y = random.randint(-300, 150)
    turtle_icon.goto(x, y)
    screen.ontimer(move_turtle, 50)


score = 0
scor_table = turtle.Turtle()
scor_table.hideturtle()
scor_table.penup()
scor_table.goto(0,150)
scor_table.write(f"Your score: 0", align="center", font=("Times New Roman", 48, "normal"))
#count the click and write the screen.
def scor(x,y):
    global score
    if turtle_icon.distance(x,y)<=50:
        score= score + 1
        scor_table.clear()
        scor_table.color("#0c343d")
        scor_table.write(f"Your score: {score}", align="center", font=("Times New Roman", 48, "normal"))

screen.onscreenclick(scor)


end_score=turtle.Turtle()
end_score.hideturtle()
end_score.penup()
scor_table.goto(0,150)
def end_game():
    turtle_icon.stamp()
    turtle_icon.hideturtle()
    scor_table.hideturtle()
    end_score.goto(0,150)
    end_score.color("#0c343d")
    end_score.write(f"Your score: {score}", align="center", font=("Times New Roman", 48, "normal"))
    screen.onscreenclick(None)

move_turtle()
countdown_timer(10)
screen.ontimer(end_game,10)




turtle.mainloop()

from turtle import *
import random
is_race_on = False
count = -50
i=0
colors = ["yellow","black","blue","pink","purple","orange"]
turtles = []
screen = Screen()
screen.setup(width=600,height=500)
user_choice = screen.textinput(title="Get your bet", prompt="Choose the color of the turtle").lower()
print(user_choice)

while (i<=5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-295, y=count)
    turtles.append(new_turtle)
    count += 30
    i +=1

if user_choice:
    is_race_on=True
    while is_race_on:
        for i in turtles:
            user_distance = random.randint(0,10)
            i.fd(user_distance)
            if i.xcor() > 295:
                if user_choice == i.pencolor():
                    print(f"Winner is {i.pencolor()} turtle \nCongratulations!You win the game.")
                else:
                    print(f"Winner is {i.pencolor()} turtle.\nYou lost!")
                    exit()
else:
    is_race_on = False


screen.exitonclick()


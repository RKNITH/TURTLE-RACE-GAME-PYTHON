from turtle import Turtle, Screen
import random
screen= Screen()
screen.setup(width=600, height=600)
guess = screen.textinput(title="Turtle Race Game", prompt="Which turtle ein the race, Chhose the color ").lower()
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
y_position =[-200,-100,0,80,160,250]

all_turtle =[]

for i in range(6):
    new_turtle =Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(-280, y_position[i])
    new_turtle.color(colors[i])

    all_turtle.append(new_turtle)

is_race_on =True

while is_race_on:
    for turtle in all_turtle:
        turtle.forward((random.randint(1, 10)))

        if turtle.xcor() >290:
            is_race_on =False

            if guess ==turtle.pencolor().lower():
                print("you win")
            else:
                print("you loose")

            print(f"the winner is {turtle.pencolor()}")        


screen.mainloop()




import turtleimport my_scriptw=turtle.Screen()w.setup(800,600)w.bgcolor("black")w.title("PONG")w.tracer(0)w1=turtle.Screen()#penpen=turtle.Turtle()pen.color("red")pen.penup()pen.goto(0,250)pen.hideturtle()pen.write("MENU",align="center",font=("Arial",30,"normal"))pen.goto(0,50)pen.color("green")pen.write("1- Multiplayer ",align="center",font=("courier",25,"normal"))pen.goto(0,-50)pen.color("green")pen.write("2-Player Vs CPU ",align="center",font=("courier",25,"normal"))pen.goto(0,-150)pen.color("green")pen.write("3-EXIT",align="center",font=("courier",25,"normal"))# cpu levelsdef level1():    w1.clear()    my_script.cpu(0.03)def level2():    w1.clear()    my_script.cpu(0.1)def level3():    w1.clear()    my_script.cpu(0.15)def one():    w.clear()    my_script.multiplayer()def two():    w.clear()    w1.setup(800,600)    w1.bgcolor("black")    w1.title("PONG")    w1.tracer(0)     pen=turtle.Turtle()    pen.color("red")    pen.penup()    pen.goto(0,250)    pen.hideturtle()     pen.write("SELECT LEVEL",align="center",font=("courier",25,"normal"))    pen.color("green")    pen.goto(0,50)    pen.write("1-Extreme",align="center",font=("courier",25,"normal"))    pen.goto(0,-50)    pen.write("2-Normal",align="center",font=("courier",25,"normal"))    pen.goto(0,-150)    pen.write("3-Easy",align="center",font=("courier",25,"normal"))    while True:        w1.listen()        w1.onkeypress(level1,"1")        w1.onkeypress(level2,"2")        w1.onkeypress(level3,"3")        w1.update()    def three():        w.clear()    w.bgcolor("black")    pen.goto(0,0)    pen.color("white")    pen.write("PRESS LEFT CLICK TO EXIT",align="center",font=("courier",25,"normal"))    w.exitonclick()w.listen()w.onkeypress(one,"1")w.onkeypress(two,"2")w.onkeypress(three,"3")w.update()w.mainloop()    
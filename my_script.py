
def multiplayer():
    import turtle
    import pygame
    import winsound
    wn=turtle.Screen()
    wn.bgcolor("black")
    wn.title("pong")
    wn.setup(800,600)
    wn.tracer(0)    
    clock = pygame.time.Clock()
    # PLAYER 1
    paddle_a=turtle.Turtle()
    paddle_a.shape("square")
    paddle_a.speed(0)
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-380,0)
    
    #player 2
    paddle_b=turtle.Turtle()
    paddle_b.shape("square")
    paddle_b.speed(0)
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(380,0)
    
    #ball
    ball=turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(0,0)
    ball.dx=1.3
    ball.dy=1.3
    
    
    #
    global point_a
    global point_b
    point_a=0
    point_b=0
    pen=turtle.Turtle()
    pen.speed(0)
    pen.color("green")
    pen.hideturtle()
    pen.penup()
    pen.goto(0,250)
    s="Player A : 0     Player B : 0"
    pen.write(s, align="Center", font=("Arial",18,"normal"))
    volume()
    wn.update()
    def a_up():
        if paddle_a.ycor()>=260:
            paddle_a.sety(260)
        y=paddle_a.ycor()+20
        paddle_a.sety(y)
        
    def a_down():
        if paddle_a.ycor()<=-260:
            paddle_a.sety(-260)        
        y=paddle_a.ycor()-20
        paddle_a.sety(y)
        
    # player 2 paddle control
    def b_up():
        if paddle_b.ycor()>=260:
            paddle_b.sety(260)        
        y=paddle_b.ycor()+20
        paddle_b.sety(y)
        
    def b_down():
        if paddle_b.ycor()<=-260:
            paddle_b.sety(-260)          
        y=paddle_b.ycor()-20
        paddle_b.sety(y)
        
    
    def speed_up():
        ball.dx=ball.dx*2
        ball.dy=ball.dy*2
    def speed_down():
        ball.dx=ball.dx/2  
        ball.dy=ball.dy/2
    while True:
        wn.update()
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)
        wn.listen()
        
        wn.onkeypress(a_up,"w")
        wn.onkeypress(a_up,"W")
        wn.onkeypress(a_down,"s")
        wn.onkeypress(a_down,"S")
        wn.onkeypress(b_up,"Up")
        wn.onkeypress(b_down,"Down")  
        wn.onkeypress(speed_up,"8")
        wn.onkeypress(speed_down,"2")
        
        #border checking
        if ball.ycor()>=280:
            ball.dy=-(ball.dy)
            ball.sety(280)
        if ball.ycor()<=-280:
            ball.dy=-(ball.dy)
            ball.sety(-280)
        if ball.xcor()>=400:
            ball.goto(0,0)
            point_a=point_a+2
            ball.dx=-(ball.dx)
            pen.clear()
            pen.goto(0,250)
            s="Player A : "+str(point_a)+"    Player B : "+str(point_b)
            pen.write(s, align="Center", font=("Arial",18,"normal"))        
            
        if ball.xcor()<=-400:
            ball.goto(0,0)
            point_b= point_b+2
            ball.dx=-(ball.dx)
            pen.clear()
            pen.goto(0,250)
            s="Player A : "+str(point_a)+"    Player B : "+str(point_b)
            pen.write(s, align="Center", font=("Arial",18,"normal"))        
            
        if ball.xcor()>=360 and paddle_b.ycor()-50<ball.ycor() and paddle_b.ycor()+50>ball.ycor():
            ball.setx(360)
            ball.dx=-(ball.dx)
        if ball.xcor()<=-360 and paddle_a.ycor()-50<ball.ycor() and paddle_a.ycor()+50>ball.ycor():
            ball.setx(-360)
            ball.dx=-(ball.dx)
        if point_a==10:
            winsound.MessageBeep()
            game_over('A',wn,pen)
        if point_b==10:
            winsound.MessageBeep()
            game_over('B',wn,pen)
        clock.tick(60)
            
# cpu
def cpu(n):
    import time
    import turtle
    import pygame
    wn=turtle.Screen()
    wn.bgcolor("black")
    wn.title("pong")
    wn.setup(800,600)
    wn.tracer(0)
    clock = pygame.time.Clock()
    # PLAYER 1
    paddle_a=turtle.Turtle()
    paddle_a.shape("square")
    paddle_a.speed(0)
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-380,0)
    
    #player 2
    # PLAYER 1
    paddle_b=turtle.Turtle()
    paddle_b.shape("square")
    paddle_b.speed(0)
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(380,0)
    
    #ball
    ball=turtle.Turtle()
    ball.shape("square")
    ball.color("red")
    ball.penup()
    ball.goto(0,0)
    ball.dx=1.3
    ball.dy=1.3
    
    
    #
    global point_a
    global point_b
    point_a=0
    point_b=0
    pen=turtle.Turtle()
    pen.speed(0)
    pen.color("green")
    pen.hideturtle()
    pen.penup()
    pen.goto(0,250)
    pen.clear()
    s="Player A : 0     CPU : 0"
    pen.write(s, align="Center", font=("Arial",18,"normal"))
    pen.goto(0,-280) 
    volume()
    def a_up():
        if paddle_a.ycor()>=260:
            paddle_a.sety(260)        
        y=paddle_a.ycor()+20
        paddle_a.sety(y)
        
    def a_down():
        if paddle_a.ycor()<=-260:
            paddle_a.sety(-260)          
        y=paddle_a.ycor()-20
        paddle_a.sety(y)
        
    # player 2 paddle control
    def b_up():
        if paddle_b.ycor()>=260:
            paddle_b.sety(260)        
        y=paddle_b.ycor()+20
        paddle_b.sety(y)
       
    def b_down():
        if paddle_b.ycor()<=-260:
            paddle_b.sety(-260)        
        y=paddle_b.ycor()-20
        paddle_b.sety(y)
       
    def speed_up():
        ball.dx=ball.dx*2
        ball.dy=ball.dy*2
        
    def speed_down():
        ball.dx=ball.dx/2  
        ball.dy=ball.dy/2   
        
    start=time.perf_counter() 
        
    while True:
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)
        wn.listen()
        
        wn.onkeypress(a_up,"w")
        wn.onkeypress(a_up,"W")
        wn.onkeypress(a_down,"s")
        wn.onkeypress(a_down,"S")
        wn.onkeypress(speed_up,"8")
        wn.onkeypress(speed_down,"2")        
        if ball.xcor()>=150 and ball.dx>0:   
            if stop-start>=n:
                start=time.perf_counter()
                if ball.ycor()>paddle_b.ycor():
                    b_up()
                if ball.ycor()<paddle_b.ycor():
                    b_down()
        
        #border checking
        if ball.ycor()>=280:
            ball.dy=-(ball.dy)
            ball.sety(280)
        if ball.ycor()<=-280:
            ball.dy=-(ball.dy)
            ball.sety(-280)
        if ball.xcor()>=400:
            ball.goto(0,0)
            point_a=point_a+2
            ball.dx=-(ball.dx)
            pen.clear()
            pen.goto(0,250)
            s="Player A : "+str(point_a)+"    CPU : "+str(point_b)
            pen.write(s, align="Center", font=("Arial",18,"normal"))        
            
        if ball.xcor()<=-400:
            ball.goto(0,0)
            point_b= point_b+2
            ball.dx=-(ball.dx)
            pen.clear()
            pen.goto(0,250)
            s="Player A : "+str(point_a)+"    CPU : "+str(point_b)
            pen.write(s, align="Center", font=("Arial",18,"normal"))        
            
        if ball.xcor()>=360 and paddle_b.ycor()-50<ball.ycor() and paddle_b.ycor()+50>ball.ycor():
            ball.setx(360)
            ball.dx=-(ball.dx)
        if ball.xcor()<=-360 and paddle_a.ycor()-50<ball.ycor() and paddle_a.ycor()+50>ball.ycor():
            ball.setx(-360)
            ball.dx=-(ball.dx)   
        stop=time.perf_counter()
        if point_a==10:
            winsound.MessageBeep(1)
            game_over('A',wn,pen)
        if point_b==10:
            winsound.MessageBeep(1)
            game_over('CPU',wn,pen)  
        wn.update()
        clock.tick(60)

def game_over(c,wn,pen):
    wn.clear()
    wn.bgcolor("black")
    pen.goto(0,0)
    pen.write("Player "+c+" Wins!!", align="Center", font=("Arial",30,"normal"))
    pen.goto(0,-250)
    pen.write("PRESS LEFT CLICK TO EXIT", align="Center", font=("Courier",18,"normal"))
    wn.exitonclick()

def volume():
    import turtle
    pen=turtle.Turtle()
    pen.speed(0)
    pen.color("green")
    pen.hideturtle()
    pen.penup()    
    pen.goto(0,-280)
    pen.write("To change speed of the ball press 8(inc) or 2(dec)", align="Center", font=("Arial",12,"normal"))    

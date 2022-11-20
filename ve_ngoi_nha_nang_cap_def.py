import turtle


def hcn_draw(toa_do,mau,l,w):
    turtle.penup()
    turtle.goto(toa_do)
    turtle.pendown()
    turtle.hideturtle()
    turtle.fillcolor(mau)
    turtle.begin_fill() 
    for i in range (2):
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(w)
        turtle.right(90)
    turtle.end_fill()
    
def polygon_draw(toa_do,n,canh,mau):
    turtle.penup()
    turtle.goto(toa_do)
    turtle.pendown()   
    turtle.hideturtle()
    turtle.fillcolor(mau)
    turtle.begin_fill() 
    angle = (n-2)*180/n
    for i in range (n):
        turtle.forward(canh)
        turtle.left(180-angle)
    turtle.end_fill()
    
def smoke(toa_do,canh,mau_but="gold3"):
    turtle.penup()
    turtle.goto(toa_do)
    turtle.pendown() 
    turtle.left(90)
    turtle.hideturtle()
    turtle.forward(canh)
    turtle.right(90)

def circle(toa_do,r,mau = "green4"):
    turtle.penup()
    turtle.goto(toa_do)
    turtle.pendown() 
    turtle.pencolor("green4")
    turtle.fillcolor(mau)
    turtle.begin_fill() 
    turtle.circle(r)
    turtle.end_fill()
    
#ngoi nha
house = hcn_draw((0,100),"lightsalmon",200,120)

#cua ra vao
door = hcn_draw((60,80),"lightseagreen",60,70)

#ong khoi
ong_khoi = hcn_draw((60,150),"darkorange",20,50)

#khoi
smoke_1 = smoke((70,152),7)
smoke_2 = smoke((73,152),10)


#mai nha
roof = polygon_draw((0,100),3,80,"red")

#tree1
la_cay_1 = polygon_draw((-200,-200),3,80,"darkolivegreen")
la_cay_2 = polygon_draw((-200,-150),3,80,"darkolivegreen1")
la_cay_3 = polygon_draw((-200,-100),3,80,"darkolivegreen2")
than_cay = hcn_draw((-170,-200),"chocolate4",20,40)

#tree2
than_cay_2 = hcn_draw((-190,100),"chocolate4",20,70)
tan_cay_1 = circle((-200,100),50)
tan_cay_2 = circle((-150,100),60)
tan_cay_3 = circle((-170,70),55)

turtle.done()
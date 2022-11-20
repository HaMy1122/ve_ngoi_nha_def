import turtle

def hcn(toa_do,mau,l,w):
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

#vengoi nha
hcn_1 = hcn((-200,-100),"coral",100,60)
hcn_2 = hcn((-100,-100),"brown",100,60)
hcn_3 = hcn((-200,-160),"green",100,60)
hcn_4 = hcn((-100,-160),"gold",100,60)
hcn_5 = hcn((0,-100),"lightsalmon",200,120)

#ve cua so
cua_so_1 = hcn((-170,-120),"white",30,20)
cua_so_2 = hcn((-70,-120),"white",30,20)
cua_so_3 = hcn((-170,-190),"white",30,20)
cua_so_4 = hcn((-70,-190),"white",30,20)

#cua ra vao
cua_ra_vao_1 = hcn((60,-150),"lightseagreen",35,70)
cua_ra_vao_2 = hcn((95,-150),"lightseagreen",35,70)



turtle.done()


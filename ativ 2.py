import turtle

p = turtle.Pen()
p.speed(0)
turtle.bgcolor('black')

cores=['red','yellow','green','blue','cyan','pink']
for x in range(600):
        resto=x%6
        cor=cores[resto]
        p.pencolor(cor)
        p.forward(x*1)
        p.left(89)
    

import turtle

# 定义画笔
turtle.hideturtle()
turtle.pensize(10)
turtle.pencolor('#388e3c')
turtle.speed(10)

jiaodu = 110
changdu = 80
youyi = 10
z = 1

while z < 10:
    turtle.right(jiaodu)
    turtle.fd(changdu)

    turtle.penup()
    turtle.home()
    turtle.setx(youyi)
    turtle.pendown()

    jiaodu -= 5
    changdu -= 0.3
    youyi += 10
    z += 1

# 定义画笔，深色
turtle.hideturtle()
turtle.pensize(10)
turtle.pencolor('#1b5e20')
turtle.speed(10)

turtle.penup()
turtle.home()
cahngdu = 45
jiaodu = 110
youyi = 10
y = 1
while y < 10:
    turtle.penup()
    turtle.sety(-35)
    turtle.pendown()
    turtle.right(jiaodu)
    turtle.fd(cahngdu)

    turtle.penup()
    turtle.home()
    turtle.setx(youyi)
    turtle.pendown()

    jiaodu -= 5
    changdu -= 0.3
    youyi += 10
    y += 1

# 回归原点
turtle.penup()
turtle.home()
cahngdu = 70
jiaodu = 110
youyi = -50
xiayi = 80
xdian = -50
x = 1
while x < 22:
    turtle.sety(-80)
    turtle.setx(-50)
    turtle.pendown()
    turtle.right(jiaodu)
    turtle.fd(cahngdu)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(0, -80)
    turtle.setx(youyi)
    turtle.pendown()

    jiaodu -= 5
    cahngdu -= 0.3
    youyi += 8
    x += 1
    # xdain +=10

turtle.exitonclick()

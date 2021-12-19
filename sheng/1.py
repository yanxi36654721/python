import turtle

# 初始化画笔
turtle.hideturtle()  # 隐藏画笔
turtle.pensize(10)  # 画笔粗细
turtle.speed(0)  # 画笔速度

# 上部分
turtle.pencolor('#388e3c')

jiaodu = 110
changdu = 100
youyi = 32
z = 1

while z < 10:
    turtle.penup()
    turtle.home()
    turtle.setx(youyi)
    turtle.sety(101)
    turtle.pendown()

    turtle.right(jiaodu)
    turtle.forward(changdu)
    jiaodu -= 5
    changdu -= 0.3
    youyi += 2
    z += 1

# 上部分，深色
turtle.pencolor('#1b5e20')
turtle.penup()
turtle.home()
changdu = 45
jiaodu = 106
youyi = 16
z = 1
while z < 7:
    turtle.penup()
    turtle.sety(46)
    turtle.setx(youyi)
    turtle.pendown()
    turtle.right(jiaodu)
    turtle.forward(changdu)

    turtle.penup()
    turtle.home()
    turtle.pendown()

    jiaodu -= 5
    changdu -= 0.3
    youyi += 10
    z += 1

# 中部分
turtle.pencolor('#388e3c')

jiaodu = 110
changdu = 80
youyi = -10
z = 1

while z < 12:
    turtle.penup()
    turtle.home()
    turtle.setx(youyi)
    turtle.pendown()

    turtle.right(jiaodu)
    turtle.forward(changdu)
    jiaodu -= 4
    changdu -= 0.3
    youyi += 10
    z += 1

# 中部分，深色
turtle.pencolor('#1b5e20')
turtle.penup()
turtle.home()
changdu = 45
jiaodu = 111
youyi = -15
z = 1
while z < 13:
    turtle.penup()
    turtle.sety(-35)
    turtle.setx(youyi)
    turtle.pendown()
    turtle.right(jiaodu)
    turtle.forward(changdu)

    turtle.penup()
    turtle.home()
    turtle.pendown()

    jiaodu -= 3.5
    changdu -= 0.3
    youyi += 10
    z += 1

# 回归原点，绘制下部分
turtle.pencolor('#388e3c')
turtle.penup()
turtle.home()
changdu = 100
jiaodu = 110
youyi = -45
xiayi = 80
xdian = -80
z = 1
turtle.setx(-50)
while z < 20:
    turtle.sety(-80)
    turtle.right(jiaodu)
    turtle.forward(changdu)

    turtle.penup()
    turtle.setheading(0)
    turtle.goto(0, -80)
    turtle.setx(youyi)
    turtle.pendown()

    jiaodu -= 2
    changdu -= 0.3
    youyi += 10
    z += 1

# 下部分深色
turtle.pencolor('#1b5e20')

turtle.penup()
turtle.home()
changdu = 45
jiaodu = 110
xiayi = 55
youyi = -50
z = 1
while z < 20:
    turtle.setheading(0)
    turtle.penup()
    turtle.sety(-130)
    turtle.setx(youyi)
    turtle.pendown()
    turtle.right(jiaodu)
    turtle.forward(changdu)
    turtle.penup()

    jiaodu -= 2
    changdu -= 0.3
    youyi += 10
    z += 1

# 树干
turtle.pencolor('#4e342e')
turtle.penup()
turtle.home()
turtle.setheading(0)
youyi = 21

z = 1
while z < 10:
    turtle.penup()
    turtle.setheading(0)
    turtle.setx(youyi)
    turtle.sety(-182)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()

    youyi += 5
    z += 1

# 五角星
turtle.setheading(0)
turtle.setx(-10)
turtle.sety(145)
turtle.pensize(1)  # 画笔粗细
turtle.pencolor("#ffff00")
turtle.fillcolor("#ffff00")
turtle.begin_fill()
for i in range(5):
    turtle.fd(100)
    turtle.right(144)
turtle.end_fill()

# 灯
turtle.penup()
turtle.goto(30, 95)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(52, 85)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(40, 78)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(20, 65)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(60, 57)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(30, 50)
turtle.pendown()
turtle.dot(7, "blue")




turtle.penup()
turtle.goto(65, 30)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(20, 15)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(20, -5)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(-10, -25)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(70, -10)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(90, -20)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(25, -40)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(65, -45)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(5, -50)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(30, -55)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(105, -60)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(-20, -65)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(50, -65)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(85, -5)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(80, -85)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(-30, -90)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(30, -95)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(50, -90)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(115, -95)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(0, -115)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(75, -110)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(105, -115)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(-25, -120)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(45, -120)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(130, -120)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(-50, -135)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(-10, -140)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(30, -140)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(70, -135)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(125, -150)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(-35, -157)
turtle.pendown()
turtle.dot(7, "red")

turtle.penup()
turtle.goto(10, -150)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(45, -165)
turtle.pendown()
turtle.dot(7, "blue")

turtle.penup()
turtle.goto(105, -170)
turtle.pendown()
turtle.dot(7, "red")

turtle.exitonclick()

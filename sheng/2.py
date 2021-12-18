import turtle

# 定义画笔
# turtle.hideturtle()
turtle.pensize(10)
turtle.pencolor('#1b5e20')
turtle.speed(1)

turtle.penup()
turtle.home()
changdu = 100
jiaodu = 110
youyi = -50
xiayi = 80
xdian = -50
x = 1
turtle.setx(-50)
while x<14:
    turtle.sety(-80)
    turtle.pendown()
    turtle.right(jiaodu)
    turtle.fd(changdu)

    turtle.penup()
    print("落笔")
    turtle.setheading(0)
    print("设置角度0")
    turtle.goto(0,-80)
    print("移动到0，-80")
    turtle.setx(youyi)
    print("右移",youyi)
    turtle.pendown()
    print("起笔")

    jiaodu -= 3
    print("角度-3",jiaodu)
    changdu -=0.3
    print("长度-0.3",changdu)
    youyi += 10
    print("右移+10",youyi)
    x += 1
    print("/n")



turtle.exitonclick()

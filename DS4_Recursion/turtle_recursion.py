'''
    Turtle库是Python语言中一个很流行的绘制图像的函数库，
    想象一个小乌龟，在一个横轴为x、纵轴为y的坐标系原点，(0,0)位置开始，
    它根据一组函数指令的控制，在这个平面坐标系中移动，从而在它爬行的路径上绘制了图形。



    # coding=utf-8
    import turtle
    import time
    
    # 同时设置pencolor=color1, fillcolor=color2
    turtle.color("red", "yellow")
    
    turtle.begin_fill()
    for _ in range(50):
        turtle.forward(200)
        turtle.left(170)
        turtle.end_fill()
        
    turtle.mainloop()




import turtle
import time

myTrutle = turtle.Turtle()
myWin = turtle.Screen()

# 递归三大条件
def drawSpiral(myTrutle,lineLen):
    if lineLen > 0:
        myTrutle.forward(lineLen)
    myTrutle.right(90)
    drawSpiral(myTrutle,lineLen - 5)

drawSpiral(myTrutle,300)

myWin.exitonclick()



'''

import turtle


myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def tree(distance,myTrutle):
    if distance > 5:
        myTurtle.forward(distance)
        myTurtle.right(20)
        tree(distance-15,myTurtle)
        myTurtle.left(40)
        tree(distance-10,myTurtle)
        myTurtle.right(20)
        myTurtle.backward(distance)



tree(100,myTurtle)
myWin.exitonclick()
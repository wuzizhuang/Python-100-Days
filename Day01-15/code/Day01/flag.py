"""
用Python的turtle模块绘制国旗
"""
import turtle


def draw_rectangle(x, y, width, height):
    """绘制矩形"""
    turtle.goto(x, y)  # 移动到起始位置
    turtle.pencolor('red')  # 设置画笔颜色为红色
    turtle.fillcolor('red')  # 设置填充颜色为红色
    turtle.begin_fill()  # 开始填充
    for i in range(2):  # 绘制矩形的四条边
        turtle.forward(width)  # 向前绘制宽度
        turtle.left(90)  # 左转90度
        turtle.forward(height)  # 向前绘制高度
        turtle.left(90)  # 左转90度
    turtle.end_fill()  # 结束填充


def draw_star(x, y, radius):
    """绘制五角星"""
    turtle.setpos(x, y)  # 移动到起始位置
    pos1 = turtle.pos()  # 记录第一个顶点位置
    turtle.circle(-radius, 72)  # 绘制圆弧并记录第二个顶点位置
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)  # 绘制圆弧并记录第三个顶点位置
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)  # 绘制圆弧并记录第四个顶点位置
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)  # 绘制圆弧并记录第五个顶点位置
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')  # 设置画笔和填充颜色为黄色
    turtle.begin_fill()  # 开始填充
    turtle.goto(pos3)  # 连接顶点形成五角星
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()  # 结束填充


def main():
    """主程序"""
    turtle.speed(12)  # 设置绘图速度
    turtle.penup()  # 抬起画笔
    x, y = -270, -180  # 设置国旗起始位置
    width, height = 540, 360  # 设置国旗宽度和高度
    draw_rectangle(x, y, width, height)  # 绘制国旗主体
    pice = 22  # 设置单位长度
    center_x, center_y = x + 5 * pice, y + height - pice * 5  # 计算大星星中心位置
    turtle.goto(center_x, center_y)  # 移动到大星星中心位置
    turtle.left(90)  # 左转90度
    turtle.forward(pice * 3)  # 向前移动3个单位长度
    turtle.right(90)  # 右转90度
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)  # 绘制大星星
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]  # 小星星相对位置
    for x_pos, y_pos in zip(x_poses, y_poses):  # 绘制小星星
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)  # 移动到小星星位置
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())  # 调整方向
        turtle.forward(pice)  # 向前移动一个单位长度
        turtle.right(90)  # 右转90度
        draw_star(turtle.xcor(), turtle.ycor(), pice)  # 绘制小星星
    turtle.ht()  # 隐藏海龟
    turtle.mainloop()  # 显示绘图窗口


if __name__ == '__main__':
    main()  # 运行主程序"""
'''用Python的turtle模块绘制国旗'''
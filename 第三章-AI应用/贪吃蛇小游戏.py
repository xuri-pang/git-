import turtle
import time
import random

# ================= 游戏配置参数 =================
DELAY = 0.1  # 初始移动延迟（控制速度）
SCORE_INCREMENT = 10

# ================= 初始化窗口 =================
wn = turtle.Screen()
wn.title("贪吃蛇小游戏 - by CodeGeeX")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # 关闭自动刷新，手动控制画面更新，使动画更流畅

# ================= 游戏状态变量 =================
score = 0
high_score = 0
direction = "stop"  # 初始方向为停止

# ================= 蛇头 =================
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)

# ================= 蛇身 (列表存储身体节点) =================
segments = []

# ================= 食物 =================
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
# 随机生成食物位置 (对齐到20x20的网格)
x_food = random.randint(-280, 280) // 20 * 20
y_food = random.randint(-280, 280) // 20 * 20
food.goto(x_food, y_food)

# ================= 记分板 =================
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("得分: 0  最高分: 0", align="center", font=("Courier", 24, "normal"))

# ================= 控制函数 =================
def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

# ================= 游戏主逻辑 =================
def update_game():
    global score, high_score, direction, segments

    # 1. 移动蛇身 (从尾部开始，每一节移动到前一节的位置)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # 2. 移动第0节身体到蛇头的位置
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # 3. 移动蛇头
    if direction == "up":
        head.sety(head.ycor() + 20)
    elif direction == "down":
        head.sety(head.ycor() - 20)
    elif direction == "left":
        head.setx(head.xcor() - 20)
    elif direction == "right":
        head.setx(head.xcor() + 20)

    # 4. 检测蛇头与食物的碰撞 (吃到了)
    if head.distance(food) < 20:
        # 食物随机移动到新位置
        x_food = random.randint(-280, 280) // 20 * 20
        y_food = random.randint(-280, 280) // 20 * 20
        food.goto(x_food, y_food)

        # 增加一节蛇身
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")  # 身体颜色稍微区分
        new_segment.penup()
        segments.append(new_segment)

        # 增加分数
        score += SCORE_INCREMENT
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"得分: {score}  最高分: {high_score}", align="center", font=("Courier", 24, "normal"))

    # 5. 检测蛇头与边界的碰撞 (撞墙死亡)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        direction = "stop"

        # 隐藏所有蛇身并清空列表
        for seg in segments:
            seg.goto(1000, 1000)  # 移出屏幕外
        segments.clear()

        # 重置分数
        score = 0
        pen.clear()
        pen.write(f"得分: {score}  最高分: {high_score}", align="center", font=("Courier", 24, "normal"))

    # 6. 检测蛇头与蛇身的碰撞 (咬到自己死亡)
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()

            score = 0
            pen.clear()
            pen.write(f"得分: {score}  最高分: {high_score}", align="center", font=("Courier", 24, "normal"))

    # 7. 刷新屏幕
    wn.update()

    # 8. 循环调用自身，持续更新
    wn.ontimer(update_game, int(DELAY * 1000))

# ================= 键盘绑定 =================
wn.listen()
wn.onkeypress(go_up, "Up")      # 上箭头
wn.onkeypress(go_down, "Down")  # 下箭头
wn.onkeypress(go_left, "Left")  # 左箭头
wn.onkeypress(go_right, "Right")# 右箭头
# 兼容 WASD 键盘操作
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# ================= 启动游戏 =================
update_game()
wn.mainloop()

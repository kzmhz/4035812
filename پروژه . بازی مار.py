import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0

#تنظیمات اولیه
wn = turtle.Screen()
wn.title("bazi")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  #جلوگیری از آپدیت مدام صفحه

#ایجاد سر مار

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# ایجاد غذا
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)




#افزایش طول مار
segments = []

#حرکت مار
#functions
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

#تابع حرکت
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20) 

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

# حرکت مار
wn.listen()
#وقتی روی دکمه‌ای کلیک شد کاری انجام بده
wn.onkeypress(go_up, 'w') 
wn.onkeypress(go_down, 's') 
wn.onkeypress(go_right, 'd') 
wn.onkeypress(go_left, 'a') 


# نمایش امتیاز
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))



while True:   #برای اینکه همیشه اجرا بشه
    wn.update()

    #اگر برخورد با بدن مار یا مرز صفحه داشت:
    #از مرکز صفحه تا چهار جهت فاصله 290 است. 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:  
        time.sleep(1)
        head.goto(0,0) 
        head.direction = 'stop'

        # مخفی کردن قسمت های جدید
        for segment in segments:
            #یعنی اگر به جایی خورد قسمت های مشکی را به خارج از صفحه بفرست
            segment.goto(1000,1000) 

        #پاک کردن قسمت های جدید
        segments.clear()
        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("candara", 24, "bold"))

    #جا به جایی غذا بعد از برخورد مار
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # اضافه کردن بخش جدید به سر مار
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('black')
        new_segment.penup()
        segments.append(new_segment)

        # افزایش امتیاز
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # حرکت به ترتیب معکوس
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # بررسی برخورد سر مار با بدنش
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # مخفی کردن بخش ها
            for segment in segments:
                segment.goto(1000, 1000)

            # پاک کردن قسمت های جدید
            segments.clear()

            # صفر کردن امتیاز
            score = 0
            delay = 0.1

            # به روز رسانی نمایش امتیاز
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

wn.mainloop()  #برای بسته نشدن پنجره

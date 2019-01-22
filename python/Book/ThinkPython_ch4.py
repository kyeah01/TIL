import turtle
bob = turtle.Turtle()
# 4.3.1
#     for i in range(4):
#         t.fd(100)
#         t.rt(90)
# 4.3.2
# def square(t,lenth):
#     for i in range(4):
#         t.fd(lenth)
#         t.rt(90)

# 4.3.3
# def polygon(t,lenth,n):
#     for i in range(n):
#         t.fd(lenth)
#         t.rt(360/n)

lenth = 50
# polygon(bob,lenth,5)

def circle(t,r,time):
    oneju = 3.14 * 2 * r
    for i in range(time):
        t.fd(oneju/time)
        t.rt(360/time)
        
time = 360
r = 10
circle(bob,r,time)
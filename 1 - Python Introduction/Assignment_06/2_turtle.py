import turtle

p = turtle.Pen()
i = 3

s = 60
while i < 10:
    b = 360 / i  # 120
    d = 180 - b
    x = b + (d / 2)
    p.pencolor('white')
    p.forward(5)  # hidden
    p.pencolor('black')
    p.left(x)
    for j in range(i):
        p.forward(s)
        if j != i - 1:
            p.left(b)
        else:
            p.right(d / 2)
            s += 1

    i += 1

turtle.done()

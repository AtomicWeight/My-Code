import turtle
t = turtle.Turtle()
t.speed(-1)
t.left(90)
for x in range(180):
  t.speed(-1)
  t.forward(1)
  t.right(1)
t.right(90)
t.forward(115)

t.left(90)
t.forward(150)
for x in range(360):
  t.forward(1)
  t.right(1)
t.left(90)
t.forward(115)
t.right(90)
for x in range(360):
  t.forward(1)
  t.left(1)
t.left(180)
t.forward(150)

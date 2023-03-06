from turtle import*
import colorsys
bgcolor('black')
speed('fastest')
width(522)
tracer(10110)
h=0
for i in range(500):
 color(colorsys.hsv_to_rgb(h,1,1))
 h+=0.04
 for j in range(4):
  fd(i)
  lt(90)
 penup()
 fd(i*3)
 pendown()
 lt(35)
done()
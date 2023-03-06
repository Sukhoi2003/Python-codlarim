from turtle import*
import colorsys as cs
bgcolor('black')
speed('fastest')
tracer(100)
h=0.05
for i in range(500):
 color(cs.hsv_to_rgb(h,1,1))
 fd(200)
 rt(91)
 circle(40)
 h+=0.03
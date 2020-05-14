
from math import sqrt, sin, cos, pi, atan
#import matplotlib.pyplot as plt
#import numpy as np
from PIL import Image, ImageDraw
#import random as rdm
	
def angle_rel(p0, p1):
	x0, y0 = p0[0], p0[1]
	x1, y1 = p1[0], p1[1]
	if x1 - x0 > 0 and y1 - y0 <= 0: #1er cadran
		angle = pi + atan((y0 - y1)/(x1 - x0))
	elif x1 - x0 < 0 and y1 - y0 <= 0: #2e cadran
		angle = 2*pi - atan((y0 - y1)/(x0 - x1))
	elif x1 - x0 < 0 and y1 - y0 >0: #3e cadran
		angle = atan((y1 - y0)/(x0 - x1))
	elif x1 - x0 >= 0 and y1 - y0 > 0: #4e cadran
		angle = pi/2 + atan((x1 - x0)/(y1 - y0))
	elif x1 - x0 == 0 and y1 - y0 < 0:
		angle = -pi/2
	return angle
	
def Tree(draw, base_points, radius, N, div, deep):
	if deep == 0:
		return "TEST"
	x0,y0 = base_points[0][0], base_points[0][1]
	x1,y1 = base_points[1][0], base_points[1][1]
	angle = angle_rel((x0, y0), (x1, y1))
	for k in range(1,N):
		x_coord = x1 + radius*cos(angle + 2*k*pi/N)
		y_coord = y1 + radius*sin(-angle - 2*k*pi/N)	
		draw.line([(x1,y1), (x_coord, y_coord)], 0, 1)
		Tree(draw, [(x1,y1), (x_coord, y_coord)], radius/div, N, div, deep-1)

def BT_tree(N,deep=3, Xmax=1000, Ymax=1000, center=(500,500), radius=50, div=2):
	im = Image.new('RGB', (Xmax, Ymax), (255,255,255))
	draw = ImageDraw.Draw(im)
	x0,y0 = center[0], center[1]
	for k in range(1,N+1):
		x1 = x0 + radius*cos(2*k*pi/N)
		y1 = y0 + radius*sin(-2*k*pi/N)
		draw.line([(x0,y0), (x1, y1)], 0, 1)
		Tree(draw, [(x0,y0),(x1,y1)], radius, N, div, deep)
	im.save('output.png', 'PNG')
		
BT_tree(3,6)

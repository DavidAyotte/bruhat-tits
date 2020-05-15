
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
	
def Tree(draw, base_points, radius, N, div, deep, colors, width):
	if deep == 0:
		return "TEST"
	if type(colors) is int or type(colors) is tuple:
		color = colors
	if type(colors) is list:
		color = colors[(deep)%(len(colors)-1)]
	x0,y0 = base_points[0][0], base_points[0][1]
	x1,y1 = base_points[1][0], base_points[1][1]
	angle = angle_rel((x0, y0), (x1, y1))
	for k in range(1,N):
		x_coord = x1 + (radius/div)*cos(angle + 2*k*pi/N)
		y_coord = y1 + (radius/div)*sin(-angle - 2*k*pi/N)	
		draw.line([(x1,y1), (x_coord, y_coord)], color, width)
		Tree(draw, [(x1,y1), (x_coord, y_coord)], radius/div, N, div, deep-1, colors, width)

def BT_tree(N,deep=3, Xmax=1000, Ymax=1000, radius=50, div=2, colors=0, background=(255,255,255), width=1, outputname='output'):
	im = Image.new('RGB', (Xmax, Ymax), background)
	draw = ImageDraw.Draw(im)
	x0,y0 = Xmax/2, Ymax/2
	if type(colors) is int or type(colors) is tuple:
		color = colors
	elif type(colors) is list:
		color = colors[0]
		# if len(colors) == deep:
			# color = colors[0]
		# else:
			# raise ValueError("The list colors must be of length deep")
	else:
		raise TypeError("Color must be an integer or a list")
	for k in range(1,N+1):
		x1 = x0 + radius*cos(2*k*pi/N)
		y1 = y0 + radius*sin(-2*k*pi/N)
		draw.line([(x0,y0), (x1, y1)], color, width)
		Tree(draw, [(x0,y0),(x1,y1)], radius, N, div, deep-1, colors, width)
	im.save(outputname + '.png', 'PNG')
		
#tests
BT_tree(3,6,outputname='N3D6div2')
BT_tree(3,6, radius=200, div=1.6,outputname='N3D6rad200div1.6')
BT_tree(3,6, radius=200, div=1.6, width=5,outputname='N3D6rad200div1.6W5')
BT_tree(5,3,Xmax=1500, Ymax=1500, radius=100, div=3, outputname='N5D3div3')
BT_tree(5,5,Xmax=1500, Ymax=1500, radius=100, div=3, outputname='N5D5div3')

#tests colors
col = [34, 55, 75, 134, 155, 201, 210]
BT_tree(3,7, radius=200, div=1.6, colors=col, width=5,outputname='N3D7colors.6W5')
BT_tree(3,7, radius=200, div=1.6, colors=(255, 0, 0), width=5,outputname='N3D7colors.6W5')

rainbow = [ (255,0,0), (255,128,0), (255,255,0), (0,255,0), (0,255,255), (0,0,255), (127,0,255) ]
BT_tree(3,7,radius=200, div=1.6, colors=rainbow, width=5,outputname='N3D7rainbow')
BT_tree(3,15,radius=200, div=1.6, colors=rainbow, width=5,outputname='HyperRainbow')
BT_tree(3,7,radius=200, div=1.6, colors=rainbow, background=(192,192,192), width=5,outputname='HyperRainbow')



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
	
def Tree(draw, base_points, radius, N, div, deep, colors, vertices, theta, width):
	if deep == 0:
		return "TEST"
	if type(colors) is int or type(colors) is tuple:
		color = colors
	if type(colors) is list:
		color = colors[deep-1]
	x0,y0 = base_points[0][0], base_points[0][1]
	x1,y1 = base_points[1][0], base_points[1][1]
	angle = angle_rel((x0, y0), (x1, y1))
	for k in range(1,N):
		x_coord = x1 + (radius/div)*cos(theta+angle + k*2*(pi-theta)/N)
		y_coord = y1 + (radius/div)*sin(-theta-angle - k*2*(pi-theta)/N)
		if vertices:
			draw.ellipse((x_coord-width, y_coord-width, x_coord+width, y_coord+width), fill=(0,0,0))
		draw.line([(x1,y1), (x_coord, y_coord)], color, width)
		Tree(draw, [(x1,y1), (x_coord, y_coord)], radius/div, N, div, deep-1, colors, vertices, theta, width)

def BT_tree(N, deep=3, Xmax=1000, Ymax=1000, radius=50, div=2, rotation=0, theta=0, vertices=None, colors=0, background=(255,255,255), width=1, outputname='output'):
	im = Image.new('RGB', (Xmax, Ymax), background)
	draw = ImageDraw.Draw(im)
	x0,y0 = Xmax/2, Ymax/2
	if type(colors) is int or type(colors) is tuple:
		color = colors
	elif type(colors) is list:
		if len(colors) != deep:
			raise ValueError("The list colors must be of length deep")
		color = colors[0]
		colors = list(reversed(colors))
	else:
		raise TypeError("Color must be an integer or a list")
	for k in range(1,N+1):
		x1 = x0 + radius*cos(rotation + 2*k*pi/N)
		y1 = y0 + radius*sin(-rotation - 2*k*pi/N)
		if vertices:
			draw.ellipse((x1-width, y1-width, x1+width, y1+width), fill=(0,0,0))
		draw.line([(x0,y0), (x1, y1)], color, width)
		Tree(draw, [(x0,y0),(x1,y1)], radius, N, div, deep-1, colors, vertices, theta, width)
	im.save(outputname + '.png', 'PNG')
	
#todo : add doc
#todo : change angle between branchs

if __name__ == "__main__":	
	#tests
	BT_tree(3,6,outputname='N3D6div2')
	BT_tree(3,6, radius=200, div=1.6,outputname='N3D6rad200div1.6')
	BT_tree(3,6, radius=200, div=1.6, width=5,outputname='N3D6rad200div1.6W5')
	BT_tree(5,3,Xmax=1500, Ymax=1500, radius=100, div=3, outputname='N5D3div3')
	BT_tree(5,5,Xmax=1500, Ymax=1500, radius=100, div=3, outputname='N5D5div3')
	BT_tree(3, 7, rotation=pi/3, outputname='N3D7rotation')

	#tests colors
	col = [34, 55, 75, 134, 155, 201, 210]
	BT_tree(3,7, radius=200, div=1.6, colors=col, width=5,outputname='N3D7colors.6W5')
	BT_tree(3,7, radius=200, div=1.6, colors=(255, 0, 0), width=5,outputname='N3D7colors.6W5')

	rainbow = [ (255,0,0), (255,127,0), (255,255,0), (0,255,0), (0,0,255), (75,0,130), (148, 0, 211) ]
	BT_tree(3,7,radius=200, div=1.6, colors=rainbow, width=5,outputname='N3D7rainbow')
	BT_tree(3,7,radius=200, div=1.6, colors=rainbow, background=(204,204,255), width=10, outputname='HyperRainbow')
	
	BT_tree(3,7, Xmax=1500, Ymax=1500, radius=50, width=5,div=1.3, theta=pi/1.3)


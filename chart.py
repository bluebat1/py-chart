import cv2
import numpy as np
class chart :
	data = []
	w = 500
	h = 300
	img = np.zeros((h,w,3), np.uint8)

	# 
	gridResolutionY = 10
	gridFlag = False

	def __init__(self, w = 500, h=300) -> None:
		self.w = w
		self.h = h
		self.img = np.zeros((h,w,3), np.uint8)
		pass
	# 
	def drawGrid(self):
		if self.gridFlag is True:
			return
		for i in range(self.gridResolutionY) :
			rowh = int(self.h - self.h*i/self.gridResolutionY)
			cv2.line(self.img, [0, rowh], [self.w, rowh], (222,222,222))
			pass
		self.gridFlag = True
		pass
	# 
	def DrawLine(self, points:list, color:slice=(222,222,0)):
		_points = []
		_pointsOut = []
		_pCount = len(points)
		_pMax = max(points)
		# scale Y
		for p in points :
			_points.append(p/_pMax*self.h)
			pass
		# scale Y
		step = int(_pCount / self.w)
		for i in range(self.w):
			_pointsOut.append(_points[step*i])
		pass

		# draw grid
		self.drawGrid()

		# draw data line
		beforPoint = (0,0)
		for i in range(len(_pointsOut)):
			newPoint = (i, self.h - int(_pointsOut[i]))
			cv2.line(self.img, beforPoint, newPoint, (color))
			beforPoint = newPoint
			pass

		# output Y Axis scalar
		yCurs = []
		for i in range(self.gridResolutionY) :
			yCurs.append( int(_pMax/self.gridResolutionY*i))
			pass
		print(yCurs)
		pass
	def show(self):
		cv2.imshow("chart", self.img)
		cv2.waitKey()
		pass
	pass
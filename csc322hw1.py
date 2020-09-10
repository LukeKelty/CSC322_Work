from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width,height= 500,500 			# window size

def drawSquare(x,y,width,height):
 glBegin(GL_QUADS) 			# start drawing a square
 glVertex2f(x,y) 			# bottom left point
 glVertex2f(x + width,y)		# bottom right point
 glVertex2f(x + width,y + height)	# top right point
 glVertex2f(x, y + height)		# top left point
 glEnd()				# done drawing

def drawDiamond(x,y,width,height):
 glBegin(GL_QUADS) 			# start drawing a square
 glVertex2f(x,y) 			# bottom point
 glVertex2f(x + width,y+ (height/2))    # right point
 glVertex2f(x, y + height)	        # top point
 glVertex2f(x - width, y + (height/2))		# left point
 glEnd()

def drawOct(x,y,w,h):
 glBegin(GL_POLYGON)
 glVertex2f(x,y)
 glVertex2f(x+(w/4),y+(h/5))
 glVertex2f(x+(w/3),y+(2*h/5))
 glVertex2f(x+(w/2),y+(3*h/5))
 glVertex2f(x+(w/4),y+(4*h/5))
 glVertex2f(x,y+h)
 glVertex2f(x-(w/4),y+(4*h/5))
 glVertex2f(x-(w/2),y+(3*h/5))
 glVertex2f(x-(w/3),y+(2*h/5))
 glVertex2f(x-(w/4),y+(h/5))
 glEnd()

def drawTriangle(x,y,width,height):
 glBegin(GL_TRIANGLES)
 glVertex2f(x,y)
 glVertex2f(x + width,y)
 glVertex2f(x + (width/2),y + height)
 glEnd()

def drawScene():
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 	# clear the screen
 glLoadIdentity() 					# reset position
 refresh2d(width, height)

 glColor3f(0.83,0.69,0.22) 				# set color to gold 
 drawOct(250,100,400,400)
 glColor3f(0.4,0.2,0.6)
 drawTriangle(150,300,60,60)
 drawTriangle(285,300,60,60)
 glColor3f(0,0,0)
 drawTriangle(172.5,310,15,25)
 drawTriangle(307.5,310,15,25)
 glColor3f(0.9,0.1,0.4)
 drawDiamond(250,125,100,125)
 glColor3f(1.0,0.0,0.0)
 drawSquare(225,50,50,150)

 glutSwapBuffers() # important for double buffering

def refresh2d(width, height):
 glViewport(0,0, width, height)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
 glMatrixMode (GL_MODELVIEW)
 glLoadIdentity()


# initialization
glutInit() 							#initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height) 				#set window size
glutInitWindowPosition(0, 0) 					#set window position
wind = glutCreateWindow("CSC 322 Fall 2020 HW1") 		#create window with title
glutDisplayFunc(drawScene) 						#set showScreen function callback
glutIdleFunc(drawScene) 						#draw all the time
glutMainLoop() 							#start everything
from graphics import*

def main():
	win = GraphWin("First Graphics Window", 500, 500)
	c = Circle (Point(100, 100), 50)
	c.draw(win)
	win.getMouse()
	win.close()
main()

def HelloWorld():
	for i in range (0 , 10):
		print("Hello, World")

def AddNumbers():
	FirstNumber = 1
	SecondNumber = 11
	Total = FirstNumber + SecondNumber
	print (Total)
	
if __name__ == '__main__':
	HelloWorld()
	AddNumbers()
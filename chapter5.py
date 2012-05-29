#5.2
def is_triangle(x,y,z):
	if x > y + z or y > x + z or z > x + y:
		return 'No'
	return 'Yes'
	
def is_triangle_dialogue():
	prompt1 = 'Please enter the length of the first stick:'
	prompt2 = 'Please enter the length of the second stick:'
	prompt3 = 'Please enter the length of the third stick:'
	len1 = int(raw_input(prompt1))
	len2 = int(raw_input(prompt2))
	len3 = int(raw_input(prompt3))
	print 'Possible to make a triangle with those sticks:', is_triangle(len1, len2, len3)

#is_triangle_dialogue()

#5.3
def draw(t,length,n):
	if n==0:
		return
	angle = 50
	fd(t,length*n)
	lt(t, angle)
	draw(t,length, n-1)
	rt(t, 2*angle)
	draw(t,length, n-1)
	lt(t, angle)
	bk(t, length*n)

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01
draw(bob, 5, 10)
wait_for_user()

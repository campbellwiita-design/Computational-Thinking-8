# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
s1 = create_sprite("fairy_map" , 0,0)
s2 = create_sprite("tooth_fairy" , 0,0)
s3 = create_sprite("tooth" ,400,150)
s3.hideturtle()
s4 = create_sprite("tooth" ,-840,-530)
s4.hideturtle()
s5 = create_sprite("tooth" ,1170,-300)
s5.hideturtle()
s6 = create_sprite("tooth" ,-545,575)
s6.hideturtle()
points = 0
print("Your stops for tonight are at: the big pond, the blue house, the dock, and the north little bush")
print("Good luck tooth fairy!")
# Section 3: Controls
def move_up():
	s1.setheading(90)
	s1.forward(5)
	s3.setheading(90)
	s3.forward(5)
	s4.setheading(90)
	s4.forward(5)
	s5.setheading(90)
	s5.forward(5)
	s6.setheading(90)
	s6.forward(5)
        
def move_down():
	s1.setheading(270)
	s1.forward(5)
	s3.setheading(270)
	s3.forward(5)
	s4.setheading(270)
	s4.forward(5)
	s5.setheading(270)
	s5.forward(5)
	s6.setheading(270)
	s6.forward(5)

def move_left():
	s1.setheading(180)
	s1.forward(5)
	s3.setheading(180)
	s3.forward(5)
	s4.setheading(180)
	s4.forward(5)
	s5.setheading(180)
	s5.forward(5)
	s6.setheading(180)
	s6.forward(5)
	
    
def move_right():
	s1.setheading(0)
	s1.forward(5)
	s3.setheading(0)
	s3.forward(5)
	s4.setheading(0)
	s4.forward(5)
	s5.setheading(0)
	s5.forward(5)
	s6.setheading(0)
	s6.forward(5)

window.onkeypress(move_up, "Down")
window.onkeypress(move_down, "Up")
window.onkeypress(move_left, "Right")
window.onkeypress(move_right, "Left")


# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# TODO - code for automatic actions
	if get_distance(s2,s3) < 50:
		s3.showturtle()
		points += 1

	if get_distance(s2,s4) < 50:
		s4.showturtle()
		points += 1

	if get_distance(s2,s5) < 50:
		s5.showturtle()
		points += 1

	if get_distance(s2,s6) < 50:
		s6.showturtle()
		points += 1


	window.update()

	if timer==3000:
		s2.write("Children woke up!",font= ("Arial", 20, "normal"))
		window.update()
		time.sleep(3)
		break
	

print("Game Over")

if points==4: 
		s2.write("Good job! You found all the teeth!",font= ("Arial", 20, "normal"))
		
		
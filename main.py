# Cameron Davis
import turtle
import time
import random


def init_turtle():
	panel = turtle.Screen()
	panel.setup(WIDTH, HEIGHT)
	panel.title('Lets Race!')
	panel.bgcolor('green')


WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'lightgreen', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number():
	while True:
		racers = input('Enter the number of racers (2 - 10): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print('Input is not numeric... Try Again!')
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print('Number not in range 2-10. Try Again!')

def race(colors):
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]




def create_turtles(colors):
	turtles = []
	spacing = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacing, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles


racers = get_number()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
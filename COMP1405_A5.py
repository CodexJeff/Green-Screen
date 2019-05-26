# ============================================================
#
# Student Name (as it appears on cuLearn): Jeff Jose
# Course Code (for this current semester): COMP1405B
#
# ============================================================
#Imports Pygame & Initializes It:
import pygame
pygame.init()

#Instructions:
instructions = (input("Do you require instructions? Please enter 'YES' for instructions,\npress 'enter' to continue. ")).upper()
if instructions == 'YES':
	input("\nThis program will merge two images, which are a semi-transparent ghost\non a background image. Your job is to provide the program with the\nbackground and ghost of your choice and the x and y co-ordinates for where the\nghost will appear. Press 'enter' to continue. ")

#Background Select:
background = input("\nWould you like the background 'abandoned_homestead.bmp', 'abandoned_circus.bmp',\nor 'abandoned_plant'. Please type EXACTLY how it stated within the quotations.\n").lower()
while background not in ['abandoned_homestead.bmp', 'abandoned_plant.bmp', 'abandoned_circus.bmp']:

#Displays Backgrounds:
	background = input("- Please type EXACTLY how it is in the quotations. ").lower()
background = pygame.image.load(background)
imagerect = background.get_rect().size
screen = pygame.display.set_mode(imagerect)
xs = imagerect[0]
ys = imagerect[1]
screen.blit(background, (0,0))
pygame.display.update()

#User Enters 'x' Point:
while True:
	try:
		x_component = int(input("\nEnter a positive integer value between 0 and " + str(xs) + " as the 'x co-ordinate' for the ghost. "))
	except ValueError:
		continue
	if x_component >= 0 and x_component <= xs:
		break
#User Enters y Point:
while True:
	try:
		y_component = int(input("Enter a positive integer value between 0 and " + str(ys) + " as the 'y co-ordinate' for the ghost. "))
	except ValueError:
		continue
	if y_component >= 0 and y_component <= ys:
		break
#Ghost Type Select:
ghost = input("\nWhat ghost would you like; 'ghost_with_broom.bmp', 'ghost_with_crutches.bmp',\nor 'ghost_with_frame.bmp'. Please type EXACTLY how it is in the quotations.\n").lower()
while ghost not in ['ghost_with_broom.bmp', 'ghost_with_crutches.bmp', 'ghost_with_frame.bmp']:
	ghost = input("- Please type EXACTLY how it is in the quotations. ").lower()
ghost = pygame.image.load(ghost)
(ghostrect) = ghost.get_rect().size
xs2 = ghostrect[0]
ys2 = ghostrect[1]

#Centers Ghost:
x_component = int(x_component - (xs2 /2))
y_component = int(y_component - (ys2 /2))

#Ghost Removal of Green:
for y in range (ys2):
	for x in range(xs2):
		(r, g, b, _) = ghost.get_at((x, y))
		(r2, g2, b2, _) = background.get_at((x, y))
		if g == 255:
			pass
		else:
			screen.set_at((x_component + x, y_component + y), (((r + r2)/2), ((g + g2)/2), ((b + b2)/2))) #Displays & Makes Transparent

#Loop Till Exit:
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()

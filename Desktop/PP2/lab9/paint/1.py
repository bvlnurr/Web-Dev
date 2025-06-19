import pygame
import math

# Initialize pygame
pygame.init()

# Define a list to store drawing commands
queue = []

# Function to get the coordinates for a rectangle
def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)

# Function to get the coordinates for a square
def getSquare(x1, y1, x2, y2):
    side = max(abs(x2 - x1), abs(y2 - y1))
    x = min(x1, x2)
    y = min(y1, y2)
    return [(x, y), (x + side, y), (x + side, y + side), (x, y + side)]

# Function to get the coordinates for a circle
def getCircle(x1, y1, x2, y2):
    x = x1
    y = y1
    r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
    return (x, y)

# Function to get the coordinates for a right triangle
def getRightTriangle(x1, y1, x2, y2):
    return [(x1, y1), (x1, y2), (x2, y2)]

# Function to get the coordinates for an equilateral triangle
def getEquilateralTriangle(x1, y1, x2, y2):
    side = ((x2-x1)**2 + (y2-y1)**2)**0.5
    height = side * math.sqrt(3) / 2
    x3 = x1 + side / 2
    y3 = y1 - height if y1 > y2 else y1 + height
    return [(x1, y1), (x2, y2), (x3, y3)]

# Function to get the coordinates for a rhombus
def getRhombus(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return [(x1 + dx/2, y1), (x2, y1 + dy/2), (x1 + dx/2, y2), (x1, y1 + dy/2)]  

# Initialize the pygame screen
screen = pygame.display.set_mode((400, 300))

# Create another layer for drawing
another_layer = pygame.Surface((400, 300))

# Initialize variables
done = False
clock = pygame.time.Clock()
tool = 0
tools_count = 8
x1 = 10
y1 = 10
x2 = 10
y2 = 10
color = (255, 255, 255)
isMouseDown = False
screen.fill((0,0,0))

# Define colors
colors = {
    pygame.K_1: (255, 0, 0),  # Red color for '1'
    pygame.K_2: (0, 255, 0),  # Green color for '2'
    pygame.K_3: (0, 0, 255),   # Blue color for '3'
    pygame.K_4: (255, 255, 0)   # Yellow color for '4'
}

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                if tool == 0:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                elif tool == 1: # for drawing squares
                    x1 = event.pos[0]       
                    y1 = event.pos[1]
                elif tool == 2: # draw circle
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                elif tool == 3: # for drawing right triangles
                    x1 = event.pos[0]
                    y1 = event.pos[1] 
                elif tool == 4: # for drawing equilateral triangles
                    x1 = event.pos[0]
                    y1 = event.pos[1]                            
                elif tool == 5: # for drawing rhombus
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                elif tool == 6: # eraser
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    pygame.draw.circle(screen, (0, 0, 0), (x1, y1), 10)
                elif tool == 7: # color selection
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    color = screen.get_at((x1, y1))
                    
            elif event.button == 3: # right click
                tool = (tool + 1) % tools_count
            isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                another_layer.blit(screen, (0, 0))
            isMouseDown = False
                
        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                if tool == 0:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                elif tool == 1: # draw square
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    points = getSquare(x1, y1, x2, y2)
                    pygame.draw.polygon(screen, color, points, 1)
                elif tool == 2: # draw circle
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    center = getCircle(x1, y1, x2, y2)
                    radius = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                    pygame.draw.circle(screen, color, center, radius, 1)                               
                if tool == 3:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    points = getRightTriangle(x1, y1, x2, y2)
                    pygame.draw.polygon(screen, color, points, 1)
                elif tool == 4:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    points = getEquilateralTriangle(x1, y1, x2, y2)
                    pygame.draw.polygon(screen, color, points, 1)
                elif tool == 5:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    points = getRhombus(x1, y1, x2, y2)
                    pygame.draw.polygon(screen, color, points, 1)
                elif tool == 6: # eraser
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    pygame.draw.circle(screen, (0, 0, 0), (x1, y1), 30)
        if event.type == pygame.KEYDOWN:
            if event.key in colors:
                color = colors[event.key]            
    pygame.display.flip()
    clock.tick(60)
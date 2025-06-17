import pygame

queue = []

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)

def getCircle(x1, y1, x2, y2):
    x = x1
    y = y1
    r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
    return (x, y)

pygame.init()

screen = pygame.display.set_mode((600, 500))

another_layer = pygame.Surface((600,500))

done = False
clock = pygame.time.Clock()

tool = 0
# 0 - rectangle
# 1 - circle
# 2 - eraser
# 3 - color selection
tools_count = 4

x1 = 10
y1 = 10
x2 = 10
y2 = 10

w = 100
h = 100

color = (255,255,255)

isMouseDown = False
screen.fill((0,0,0))

colors = {
    pygame.K_1: (255,0,0), 
    pygame.K_2: (0, 255, 0),
    pygame.K_3: (0, 0, 255),
    pygame.K_4: (255, 255, 0) 
}

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if tool == 0:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                elif tool == 1:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                elif tool == 2:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    pygame.draw.circle(screen, (0,0,0), (x1, y1), 10)
                elif tool == 3:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    color = screen.get_at((x1, y1))

            elif event.button == 3:
                tool = (tool + 1) % tools_count
            isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                another_layer.blit(screen, (0, 0))
            isMouseDown = False

        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                if tool == 0:
                    screen.blit(another_layer, (0,0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1,y1,x2,y2)), 1)
                elif tool == 1:
                    screen.blit(another_layer, (0, 0))
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    center = getCircle(x1, y1, x2, y2)
                    radius = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                    pygame.draw.circle(screen, color, center, radius, 1)
                elif tool == 2:
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                        pygame.draw.circle(screen, (0,0,0), (x1, y1), 30)
        if event.type == pygame.KEYDOWN:
            if event.key in colors:
                color = colors[event.key]
            
pygame.dispaly.flip()

clock.tick(60)
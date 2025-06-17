import pygame
import random
import sys

pygame.init()

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
COLORS = {"WHITE": (255, 255, 255), "GREEN": (0, 255, 0), "RED": (255, 0, 0)}
DIRECTIONS = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Define the Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice(list(DIRECTIONS.values()))
        self.color = COLORS["GREEN"]

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        # Calculate the new position of the snake's head
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        # Check if the snake collides with itself or any obstacles
        if len(self.positions) > 2 and new in self.positions[2:] or any(new in obs.positions for obs in obstacles):
            return True  # Game over condition
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        return False

    def reset(self):
        # Reset the snake's attributes
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice(list(DIRECTIONS.values()))

    def draw(self, surface):
        # Draw the snake on the screen
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, COLORS["WHITE"], r, 1)

    def handle_keys(self):
        # Handle the key events to change the snake's direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DIRECTIONS["DOWN"]:
                    self.direction = DIRECTIONS["UP"]
                elif event.key == pygame.K_DOWN and self.direction != DIRECTIONS["UP"]:
                    self.direction = DIRECTIONS["DOWN"]
                elif event.key == pygame.K_LEFT and self.direction != DIRECTIONS["RIGHT"]:
                    self.direction = DIRECTIONS["LEFT"]
                elif event.key == pygame.K_RIGHT and self.direction != DIRECTIONS["LEFT"]:
                    self.direction = DIRECTIONS["RIGHT"]

# Define the Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = COLORS["RED"]
        self.randomize_position()

    def randomize_position(self):
        # Randomize the position of the food
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        # Draw the food on the screen
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, COLORS["WHITE"], r, 1)

# Define the Obstacle class
class Obstacle:
    def __init__(self, num_blocks, vertical=False):
        self.positions = [(0, 0)] * num_blocks
        self.color = COLORS["WHITE"]
        self.vertical = vertical
        self.randomize_position()

    def randomize_position(self):
        # Randomize the position of the obstacle
        start_pos = (random.randint(0, GRID_WIDTH - 2) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 2) * GRID_SIZE)
        if self.vertical:
            self.positions = [(start_pos[0], (start_pos[1] + i * GRID_SIZE) % SCREEN_HEIGHT) for i in range(len(self.positions))]
        else:
            self.positions = [((start_pos[0] + i * GRID_SIZE) % SCREEN_WIDTH, start_pos[1]) for i in range(len(self.positions))]

    def draw(self, surface):
        # Draw the obstacle on the screen
        for pos in self.positions:
            r = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (0, 0, 0), r, 1)

def main():
    global obstacles
    snake = Snake()
    food = Food()
    obstacles = [Obstacle(4, vertical=i%2==0) for i in range(6)]  # Create obstacles
    score = 0
    level = 1
    game_over = False
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)

    while True:
        screen.fill((0, 0, 0))
        snake.handle_keys()
        game_over = snake.move()
        if game_over:
            game_over_text = font.render("Game Over", True, COLORS["WHITE"])
            screen.blit(game_over_text, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            if score % 5 == 0:
                snake.color = random.choice([(0,255,255), (255,255,0)])
            if score % 5 == 0:  # Change the position of obstacles after the snake eats 2 units of food
                for obs in obstacles:
                    obs.randomize_position()
            if score % 5 == 0:  # Increase the level after the snake eats 5 units of food
                level += 1
                obstacles.append(Obstacle(4, vertical=level%2==0))  # Add a new obstacle for each level
                clock.tick(8 + level)
            food.randomize_position()
            game_over = False

        if (snake.get_head_position()[0] < 0 or snake.get_head_position()[0] >= SCREEN_WIDTH or
                snake.get_head_position()[1] < 0 or snake.get_head_position()[1] >= SCREEN_HEIGHT):
            snake.reset()
            score = 0
            level = 1
            obstacles = [Obstacle(4, vertical=i%2==0) for i in range(6)]  # Reset obstacles when hitting the border
            game_over = True

        if not game_over:
            snake.draw(screen)
            food.draw(screen)
            for obs in obstacles:
                obs.draw(screen)

        score_text = font.render(f"Score: {score}", True, COLORS["WHITE"])
        level_text = font.render(f"Level: {level}", True, COLORS["WHITE"])
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))

        pygame.display.update()
        clock.tick(8 + level)

if __name__ == '__main__':
    main()
import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
COLORS = {"WHITE": (255, 255, 255), "GREEN": (0, 255, 0), "RED": (255, 0, 0)}
MOVEMENTS = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}

# Pygame screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake class to represent the snake in the game
class Snake:
    def __init__(self):
        self.size = 1
        self.body = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice(list(MOVEMENTS.values()))  # Start with a random direction
        self.color = COLORS["GREEN"]

    def head(self):
        return self.body[0]

    def move(self):
        current = self.head()
        dx, dy = self.direction
        new_position = (((current[0] + (dx * GRID_SIZE)) % WIDTH), (current[1] + (dy * GRID_SIZE)) % HEIGHT)
        # Check for collision with itself or obstacles
        if len(self.body) > 2 and new_position in self.body[2:] or any(new_position in obstacle.body for obstacle in obstacles):
            return True  # Game over if collision occurs
        else:
            self.body.insert(0, new_position)
            if len(self.body) > self.size:
                self.body.pop()
        return False

    def reset(self):
        self.size = 1
        self.body = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice(list(MOVEMENTS.values()))  # Start with a random direction

    def draw(self, surface):
        for part in self.body:
            rect = pygame.Rect((part[0], part[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, COLORS["WHITE"], rect, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Change direction according to key press, but disallow opposite direction
                if event.key == pygame.K_UP and self.direction != MOVEMENTS["DOWN"]:
                    self.direction = MOVEMENTS["UP"]
                elif event.key == pygame.K_DOWN and self.direction != MOVEMENTS["UP"]:
                    self.direction = MOVEMENTS["DOWN"]
                elif event.key == pygame.K_LEFT and self.direction != MOVEMENTS["RIGHT"]:
                    self.direction = MOVEMENTS["LEFT"]
                elif event.key == pygame.K_RIGHT and self.direction != MOVEMENTS["LEFT"]:
                    self.direction = MOVEMENTS["RIGHT"]

# Food class to represent the food in the game
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = COLORS["RED"]
        self.randomize_position()  # Generate random position for the food
        self.weight = random.randint(1, 2)  # Random weight between 1 and 2
        self.creation_time = time.time()  # Time when the food is created

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, COLORS["WHITE"], rect, 1)

    def is_expired(self, duration):
        # Check if the food is expired based on the duration
        return time.time() - self.creation_time > duration

# Obstacle class to represent obstacles in the game
class Obstacle:
    def __init__(self, blocks, vertical=False):
        self.body = [(0, 0)] * blocks
        self.color = COLORS["WHITE"]
        self.vertical = vertical
        self.randomize_position()  # Generate random position for the obstacle

    def randomize_position(self):
        start = (random.randint(0, GRID_WIDTH - 2) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 2) * GRID_SIZE)
        if self.vertical:
            self.body = [(start[0], (start[1] + i * GRID_SIZE) % HEIGHT) for i in range(len(self.body))]
        else:
            self.body = [((start[0] + i * GRID_SIZE) % WIDTH, start[1]) for i in range(len(self.body))]

    def draw(self, surface):
        for pos in self.body:
            rect = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, (0, 0, 0), rect, 1)

# Main function to run the game
def main():
    global obstacles
    snake = Snake()
    food = Food()
    obstacles = [Obstacle(4, vertical=i%2==0) for i in range(6)]  # Create 6 obstacles with 4 blocks each, alternating between horizontal and vertical
    score = 0
    level = 1
    game_over = False  # Variable to track game over state
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)  # Create a font object

    while True:
        screen.fill((0, 0, 0))  # Fill the screen with black color
        snake.handle_keys()  # Handle keyboard input
        game_over = snake.move()  # Move the snake and check for collisions
        if game_over:
            # Display game over message
            game_over_text = font.render("Game Over", True, COLORS["WHITE"])
            screen.blit(game_over_text, (WIDTH // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(3000)  # Wait for 3 seconds
            pygame.quit()  # Quit Pygame
            sys.exit()  # Exit the program

        # Check if the snake eats the food
        if snake.head() == food.position:
            snake.size += food.weight  # Increase the size of the snake by the weight of the food
            score += food.weight  # Increase the score by the weight of the food
            food = Food()  # Generate a new food with random weight and position
            game_over = False  # Reset game_over when eating food

            # Increase level and add obstacles for every 5 units of food eaten
            if score % 5 == 0:
                level += 1
                obstacles.append(Obstacle(4, vertical=level%2==0))  # Add a new obstacle for each level
                clock.tick(8 + level)
                snake.color = random.choice([(0,255,255), (255,255,0)])  # Change the color of the snake after every 5 units of food

        # Check if the food is expired every 10 seconds
        if food.is_expired(10):
            food = Food()  # Generate a new food with random weight and position

        # Check for border collision
        if (snake.head()[0] < 0 or snake.head()[0] >= WIDTH or
                snake.head()[1] < 0 or snake.head()[1] >= HEIGHT):
            snake.reset()
            score = 0
            level = 1
            obstacles = [Obstacle(4, vertical=i%2==0) for i in range(7)]  # Reset obstacles when hitting the border
            game_over = True  # Set game_over to True when hitting the border

        if not game_over:
            snake.draw(screen)  # Draw the snake
            food.draw(screen)  # Draw the food
            for obs in obstacles:
                obs.draw(screen)  # Draw the obstacles

        # Render the score and level and blit them on the screen
        score_text = font.render(f"Score: {score}", True, COLORS["WHITE"])
        level_text = font.render(f"Level: {level}", True, COLORS["WHITE"])
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))

        pygame.display.update()  # Update the display
        clock.tick(8 + level)  # Adjust game speed based on level

if __name__ == '__main__':
    main()
# Definition of Player object, will hold all the properties of player
class PlayerObj:
    def __init__(self, x):
        self.x = x
        
# Definition of Enemy Object, will hold position of enemy 
class EnemyObj:
    def __init__(self, x, y = 0):
        self.x = x
        self.y = y
        self.hit = False
        self.xspeed = ENEMY_SPEED

# Definition of Bullet Object
class Bullet:
    def __init__(self, x):
        self.x = x
        self.y = VERTICAL_PIXELS - BLOCK_SIZE

if __name__ == "__main__":
    import pygame
    import random
    import sys

    # Settings for Window size
    HORIZONTAL_PIXELS = 1600
    VERTICAL_PIXELS = 900

    # Speed settings
    PLAYER_SPEED = 10
    BULLET_SPEED = 30
    ENEMY_SPEED = 3

    # Size settings
    BLOCK_SIZE = 90
    ENEMY_PADDING = 40
    BULLET_SIZE = 10
    NUM_ENEMIES = 10
    ENEMIES_PER_ROW = 7

    # Delay in frames between every bullet fire
    ATTACK_DELAY = 45
    
    # Settings for the graphics
    FPS = 60

    # Color constants
    PLAYER_COLOR = 46, 125, 50
    ENEMY_COLOR = 216, 67, 21
    BULLET_COLOR = 200, 200, 200
    BG_COLOR = 0, 0, 0

    # Initialise PyGame
    pygame.init()

    # Create screen for showing viusalisation
    size = width, height = HORIZONTAL_PIXELS, VERTICAL_PIXELS
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Invaders")

    # Create a surface on which we will draw our objects
    rect_canvas = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))

    # Create Player near center
    Player = PlayerObj((HORIZONTAL_PIXELS - BLOCK_SIZE) // 2)

    # Move and shoot cooldowns
    move_frame = 0
    attack_cooldown = 0

    # List of bullets and enemies
    bullet_list = []
    all_enemies = []

    # Calculate maximum possible enemies in a row
    max_in_a_row = HORIZONTAL_PIXELS // (BLOCK_SIZE + ENEMY_PADDING)
    if (HORIZONTAL_PIXELS - (max_in_a_row * (BLOCK_SIZE + ENEMY_PADDING))) >= BLOCK_SIZE:
        max_in_a_row += 1
    max_in_a_row = min(max_in_a_row, ENEMIES_PER_ROW)

    # Boolean to tell enemy group to start moving in the opposite direction
    flip = False

    # Create and place enemies at appropriate place
    for i in range(NUM_ENEMIES):
        all_enemies.append(EnemyObj((i % max_in_a_row) * (BLOCK_SIZE + ENEMY_PADDING), ((i // max_in_a_row )) * (BLOCK_SIZE + ENEMY_PADDING)))

    # While game is running, for every frame,
    while True:

        # Store events to process quit and KeyDown events
        events = pygame.event.get()

        # Handle exit event
        for event in events:
            # Let user exit
            if event.type == pygame.QUIT: sys.exit()

        # handle Keypress events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if move_frame == 0:
                move_frame = 1
                Player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            if move_frame == 0:
                move_frame = 1
                Player.x += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            if attack_cooldown == 0:
                attack_cooldown = ATTACK_DELAY
                bullet_list.append(Bullet(Player.x))

        # Fill the screen with BG_COLOR
        screen.fill(BG_COLOR)

        # Move bullets, and delete bullets that leave screen
        bullet_list = [x for x in bullet_list if not x.y < -BULLET_SIZE]
        for p in range(len(bullet_list)):
            if bullet_list[p]:
                bullet_list[p].y -= BULLET_SPEED
                pygame.draw.rect(screen, BULLET_COLOR, pygame.Rect(bullet_list[p].x + ((BLOCK_SIZE - BULLET_SIZE)/2), bullet_list[p].y,  BULLET_SIZE, BULLET_SIZE))

        # Refresh list of alive enemies
        all_enemies = [x for x in all_enemies if not x.hit]

        # You win if you kill them all
        if not all_enemies:
            print("You Win")
            sys.exit()

        # For every alive enemy,
        for enemy in range(len(all_enemies)):

            # Check if enemy has entered player area, if yes, then player loses
            if (all_enemies[enemy].y >= (VERTICAL_PIXELS - BLOCK_SIZE)):
                print("You Lose")
                sys.exit()

            # Move every enemy, and make them turn around if the group hits the border
            all_enemies[enemy].x += all_enemies[enemy].xspeed
            if ((all_enemies[enemy].x <= 0) or (all_enemies[enemy].x >= (HORIZONTAL_PIXELS - BLOCK_SIZE))) and not flip:
                flip = True
            
            # Draw each enemy
            pygame.draw.rect(rect_canvas, ENEMY_COLOR, pygame.Rect(0, 0,  BLOCK_SIZE, BLOCK_SIZE))
            screen.blit(rect_canvas, (all_enemies[enemy].x, all_enemies[enemy].y))

            # Check every active bullet to see if it collides with an enemy
            bullet_list = [x for x in bullet_list if not x.y < -BULLET_SIZE]
            for bullet in range(len(bullet_list)):
                # Check if bullet hit the enemy
                if (bullet_list[bullet].x >= (all_enemies[enemy].x - BULLET_SIZE)) and \
                (bullet_list[bullet].x <= (all_enemies[enemy].x + BLOCK_SIZE)) and \
                (bullet_list[bullet].y <= (all_enemies[enemy].y + BLOCK_SIZE)) and \
                (bullet_list[bullet].y >= all_enemies[enemy].y):
                    # If yes, them move bullet off screen (gets automatically deleted)
                    bullet_list[bullet].x = -100
                    # Mark the enemy as dead (gets deleted next time the alive enemy list is updated)
                    all_enemies[enemy].hit = True

        # If the enemies are supposed to turn around, turn them all around, and then set flip to false for the next edge detection
        if flip:
            for enemy in range(len(all_enemies)):
                all_enemies[enemy].xspeed = -all_enemies[enemy].xspeed
                all_enemies[enemy].y += (BLOCK_SIZE + ENEMY_PADDING)
            flip = False

        # Reduce attack and move cooldowns
        if move_frame > 0:
            move_frame -= 1

        if attack_cooldown > 0:
            attack_cooldown -= 1

        # Handle border cases where Player hits the border
        if Player.x >= (HORIZONTAL_PIXELS - BLOCK_SIZE):
            Player.x = HORIZONTAL_PIXELS - BLOCK_SIZE
        elif Player.x <= 0:
            Player.x = 0

        # Draw player object
        pygame.draw.rect(rect_canvas, PLAYER_COLOR, pygame.Rect(0, 0,  BLOCK_SIZE, BLOCK_SIZE))
        screen.blit(rect_canvas, (Player.x, VERTICAL_PIXELS - BLOCK_SIZE))

        # Update the display
        pygame.display.update()

        # Tick the display as per FPS
        pygame.time.Clock().tick(FPS)
        
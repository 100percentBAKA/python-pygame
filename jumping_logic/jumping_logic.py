import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 800
FPS = 60
VEL = 8

JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
Y_GRAVITY = 1.0

X_POSITION, Y_POSITION = 200, 660

CLOCK = pygame.time.Clock()

is_jumping = False

FONT = pygame.font.Font(None, 50)  # none --> default text
GAME_ENDED_TEXT = "GAME ENDED"
TEXT_X_POSITION = WIDTH // 2 - 100
TEXT_Y_POSITION = HEIGHT // 2
TEXT_SURFACE = FONT.render(GAME_ENDED_TEXT, True, (255, 0, 0))

BACKGROUND = pygame.image.load(os.path.join("jumping_logic", "background.png"))
STANDING_SURFACE = pygame.transform.scale(
    pygame.image.load(os.path.join("jumping_logic", "mario_standing.png")), (48, 64)
)
JUMPING_SURFACE = pygame.transform.scale(
    pygame.image.load(os.path.join("jumping_logic", "mario_jumping.png")), (48, 64)
)
BUG_SURFACE = pygame.transform.scale(
    pygame.image.load(os.path.join("jumping_logic", "bug.png")), (50, 50)
)
bug_rect = BUG_SURFACE.get_rect(center=(WIDTH - 30, 665))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Jumping")


def render(surface, mario_rect):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(surface, mario_rect)
    WIN.blit(BUG_SURFACE, bug_rect)
    pygame.display.flip()


def main():
    running = True

    global is_jumping
    global X_POSITION
    global Y_POSITION
    global Y_VELOCITY
    mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]:
            is_jumping = True

        if key_pressed[pygame.K_RIGHT] and X_POSITION < WIDTH - 30:
            X_POSITION += VEL
        elif key_pressed[pygame.K_LEFT] and X_POSITION > 15:
            X_POSITION -= VEL

        if is_jumping:
            Y_POSITION -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY

            if Y_VELOCITY < -JUMP_HEIGHT:
                Y_VELOCITY = JUMP_HEIGHT
                is_jumping = False

            mario_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
            render(JUMPING_SURFACE, mario_rect)
        else:
            mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
            render(STANDING_SURFACE, mario_rect)

        if bug_rect.x > 0:
            bug_rect.x -= VEL
            WIN.blit(BUG_SURFACE, bug_rect)
        else:
            bug_rect.x = WIDTH - 30
            WIN.blit(BUG_SURFACE, bug_rect)

        if mario_rect.colliderect(bug_rect):
            print("Collision")
            WIN.blit(TEXT_SURFACE, (TEXT_X_POSITION, TEXT_Y_POSITION))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            return

        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()

import player, enemy, pygame, sys, os

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

player = player.Player()
enemy1 = enemy.Enemy()


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    #Input
    enemy1.track(player.getLoc())
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2,0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0,-2)
    if key[pygame.K_DOWN]:
        player.move(0,2)
	
    #Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), enemy1)
    pygame.display.flip()

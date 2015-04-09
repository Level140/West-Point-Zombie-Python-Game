import player, enemy, mapx, pygame, sys, os

bullets = []
pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
screen = pygame.display.set_mode((1400, 800),pygame.FULLSCREEN)
clock = pygame.time.Clock()

player1 = player.Player()
gun = player1.Weapon(10)
enemy1 = enemy.Enemy()
hold=mapx.Map()
walls=hold.drawMap(1)
#LOAD SOUND
pygame.mixer.music.load('./sounds/background.mp3')
pygame.mixer.music.play(-1)


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    #Input
	key = pygame.key.get_pressed()
	if key[pygame.K_ESCAPE]:
		sys.exit(0)
    if key[pygame.K_a]:
        player1.move(-2,0)
        if player1.rect.collidelist(walls)!=-1:
          player1.move(2,0)
    if key[pygame.K_d]:
        player1.move(2, 0)
        if player1.rect.collidelist(walls)!=-1:
          player1.move(-2,0)
    if key[pygame.K_w]:
        player1.move(0,-2)
        if player1.rect.collidelist(walls)!=-1:
          player1.move(0,2)
    if key[pygame.K_s]:
        player1.move(0,2)
        if player1.rect.collidelist(walls)!=-1:
          player1.move(0,-2)
		  
		  
    if key[pygame.K_SPACE]:
        p = player1.getLoc()
        t = pygame.mouse.get_pos()
        dx = t[0] - p[0]
        dy = t[1] - p[1]
        bullets.append([p[0]+25, p[1]+25, dx, dy])


    for b in range(len(bullets)):
        if bullets[b][0] < bullets[b][2]:
            bullets[b][0]+=bullets[b][2]%10
        else:
            bullets[b][0]-=bullets[b][2]%10
        if bullets[b][1] < bullets[b][3]:
            bullets[b][1]+=bullets[b][3]%10
        else:
            bullets[b][1]-=bullets[b][3]%10

    for bullet in bullets:
        if bullet[0]<0:
            bullets.remove(bullet)

    #Drawing
    screen.fill((0,0,0))
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(bullet[0], bullet[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), player1)
    pygame.draw.rect(screen, (0, 255, 0), enemy1)
	#DRAW MAP
    for x in walls:
      pygame.draw.rect(screen,(210,210,210),x)
    pygame.display.flip()

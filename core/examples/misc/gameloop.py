"""
By https://www.youtube.com/channel/UCnpZf32QgSTT-ngdufQpISw

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # мышь и клавиаутра
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # задний фон
    display.blit(имя_изображения, (0, 0))

    # Здесь выполнение всех пользовательских действий, в т.ч. прорисовка других объектов
    # На экране. Это делается после прорисовки фона (чтобы было поверх него), но до update
    clock.tick(FPS)
    pygame.display.update()

"""
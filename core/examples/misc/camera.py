import pygame

pygame.init()

colors = {
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "BLACK": (0, 0, 0),
    "DARK": (32, 32, 32),
}


#
###
class Player:
    def __init__(self):
        self.image = pygame.Surface((16, 16))  # Create Player Image
        self.image.fill(colors["RED"])  # Fill Player Red
        self.rect = pygame.Rect((50, 50), (16, 16))  # Create Player Rect

    def move(self, camera_pos):
        pos_x, pos_y = camera_pos  # Split camera_pos
        #
        key = pygame.key.get_pressed()  # Get Keyboard Input

        dx, dy = 0, 0
        if key[pygame.K_w]:  # Check Key
            dy = -8
        if key[pygame.K_a]:
            dx = -8
        if key[pygame.K_s]:
            dy = 8
        if key[pygame.K_d]:
            dx = 8

        self.rect.move_ip(dx, dy)
        # self.rect.x += dx
        # self.rect.y += dy
        # pos_x -= dx
        pos_y -= dy

        # >>> check border
        # if self.rect.x < 0:  # Simple Sides Collision
        #     self.rect.x = 0  # Reset Player Rect Coord
        #     pos_x = camera_pos[0]  # Reset Camera Pos Coord
        # elif self.rect.x > 984:
        #     self.rect.x = 984
        #     pos_x = camera_pos[0]
        # if self.rect.y < 0:
        #     self.rect.y = 0
        #     pos_y = camera_pos[1]
        # elif self.rect.y > 984:
        #     self.rect.y = 984
        #     pos_y = camera_pos[1]
        # #

        return (pos_x, pos_y)  # Return New Camera Pos

    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))


###
#
#
###
def Main(display, clock):
    # >>> init world
    world = pygame.Surface((1000, 1000))  # Create Map Surface
    # world.fill(colors["BLACK"])             # Fill Map Surface Black
    # render_blue_rectangles(world)

    # >>> init player with camera
    player = Player()  # Initialize Player Class
    camera_pos = (32, 32)  # Create Camara Starting Position

    # >>> gameloop
    while True:
        clock.tick(60)
        # >>> handle_events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # >>> update
        camera_pos = player.move(camera_pos)  # Run Player Move Function And Return New Camera Pos

        # >>> render
        display.fill(colors["BLACK"])  # Fill The Background White To Avoid Smearing
        world.fill(colors["DARK"])  # Refresh The World So The Player Doesn't Smear
        render_blue_rectangles(world)
        player.render(world)  # Render The Player

        display.blit(world, camera_pos)  # Render Map To The Display
        # print(camera_pos)
        pygame.display.update()


def render_blue_rectangles(world):
    for x in range(10):
        pygame.draw.rect(world, colors["BLUE"], ((x * 100, x * 100), (20, 20)))


###
#
if __name__ in "__main__":
    # display = pygame.display.set_mode((512, 512))
    display = pygame.display.set_mode((512, 512))
    pygame.display.set_caption("Scrolling Camera")
    clock = pygame.time.Clock()
    Main(display, clock)  # Run Main Loop

from car import *
from gameInfo import *

pygame.font.init()
def get_font(size):
    return pygame.font.Font("img/font.ttf",size)



def draw(win, images,player_car,computer_car,game_info):
    for img, pos in images:
        win.blit(img, pos)

    lap_text = MAIN_FONT.render(f"Lap {game_info.lap}/5", 1 , (255,255,255))
    win.blit(lap_text, (10,HEIGHT-lap_text.get_height() -  70))

    time_text = MAIN_FONT.render(f"Time: {game_info.get_level_time()} s", 1, (255, 255, 255))
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

    vel_text = MAIN_FONT.render(f"Speed: {round(player_car.vel,1)} px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))


    player_car.draw(win)
    computer_car.draw(win)
    pygame.display.update()

GRASS = scale_img(pygame.image.load("img/grass.jpg"), 2.5)
TRACK = scale_img(pygame.image.load("img/track.png"), 0.99)
BACKGROUND = pygame.image.load("img/background.png")

WIDTH, HEIGHT = BACKGROUND.get_width(), BACKGROUND.get_height()

TRACK_BORDER = scale_img(pygame.image.load("img/track-border.png"), 0.99)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
FINISH_LINE = pygame.image.load("img/finish (1).png")
FINISH_LINE_MASK = pygame.mask.from_surface(FINISH_LINE)
FINISH_LINE_POSITION = (146,250)

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display.set_caption("Oldschool web racing game")

FPS = 60 # liczba klatek
GAME_CLOCK = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0)), (FINISH_LINE, FINISH_LINE_POSITION), (TRACK_BORDER,(0,0))]
PATH = [(199, 84), (42, 115), (75, 515), (195, 701), (339, 813), (417, 688), (510, 524), (668, 649), (702, 824), (840, 607), (797, 401), (580, 407), (437, 341), (544, 262), (772, 295), (791, 139), (630, 82), (329, 85), (327, 260), (286, 434), (170, 352), (185, 254), (170, 200)]

MAIN_FONT = pygame.font.SysFont("comicsans", 44)
lap_number = 1

def blit_text_center(win, font, text):
    render = font.render(text, 1, (200,200,200))
    win.blit(render, (win.get_width()/2 - render.get_width()/2, win.get_height()/2 - render.get_height()/2))                        #renderujemy tekst tak aby był idelanie po środku

def move_player1(player_car):
    keys = pygame.key.get_pressed()

    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_r]:
        moved = True
        player_car.move_backward()
    if keys[pygame.K_s]:
        player_car.brake()
    if not moved:
        player_car.reduce_speed()

def move_player2(player_car):
    keys = pygame.key.get_pressed()

    moved = False

    if keys[pygame.K_LEFT]:
        player_car.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        player_car.rotate(right=True)
    if keys[pygame.K_UP]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_KP0]:
        moved = True
        player_car.move_backward()
    if keys[pygame.K_DOWN]:
        player_car.brake()
    if not moved:
        player_car.reduce_speed()

def handle_collision(player_car, computer_car,game_info,MENU_TEXT, MENU_RECT):
    keys = pygame.key.get_pressed()
    if player_car.collide(TRACK_BORDER_MASK) is not None:
        player_car.bounce()


    computer_finish_poi_collide = computer_car.collide(FINISH_LINE_MASK, *FINISH_LINE_POSITION)
    if computer_finish_poi_collide is not None:
        computer_car.reset_next_lap(game_info.lap)
        game_info.next_lap()
        print(f"{computer_finish_poi_collide}")
        print(f"{game_info.lap}")
    if game_info.race_finished():
        # player_car.reset()
        # computer_car.reset()
        WINDOW.blit(MENU_TEXT, MENU_RECT)
        pygame.display.update()
        print("computer wins")
        return True


    player_finish_poi_collide = player_car.collide(FINISH_LINE_MASK, *FINISH_LINE_POSITION)

    if player_finish_poi_collide is not None:
        print(f"{player_finish_poi_collide}")
        print(f"{player_car.lap_number}")
        if player_finish_poi_collide[1] == 0 and keys[pygame.K_r]:
            player_car.bounce()
        else:
            game_info.next_lap()
            if game_info.race_finished():
                player_car.reset()
                computer_car.reset()
                print("you win")

player_car = PlayerCar(4,4)
computer_car = ComputerCar(2.5,4,PATH)
game_info = GameInfo()
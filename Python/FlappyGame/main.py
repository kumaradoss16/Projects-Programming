import pygame, sys, random
import winsound

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 800))
    screen.blit(floor_surface, (floor_x_pos + 576, 800))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 924:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            winsound.PlaySound('C:/Users/hgf/PycharmProjects/FlappyGame/Sound/sfx_hit.wav', winsound.SND_ASYNC)
            return False
    if bird_rect.top <= -200 or bird_rect.bottom >= 800:
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 2, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = score_surface.get_rect(center=(250, 750))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.mixer.pre_init(frequency= 44100, size= 16, channels= 1, buffer= 712)
pygame.init()
screen = pygame.display.set_mode((576, 924))
clock = pygame.time.Clock()
game_font = pygame.font.Font('C:/Users/hgf/PycharmProjects/FlappyGame/04B_19.ttf', 40)

# Game Variable
gravity = 0.35
bird_movement = 0
game_active = True
score = 0
high_score = 0

bg_surface = pygame.image.load('C:/Users/hgf/PycharmProjects/FlappyGame/Graphics/background-night.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('C:/Users/hgf/PycharmProjects/FlappyGame/Graphics/base.png')
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load('C:/Users/hgf/PycharmProjects/FlappyGame/Graphics/redbird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('C:/Users/hgf/PycharmProjects/FlappyGame/Graphics/redbird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('C:/Users/hgf/PycharmProjects/FlappyGame/Graphics/redbird-upflap.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 462))
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

#bird_surface = pygame.image.load('C:/Users/hgf/PycharmProjects/FlappyGame/Graphics/bluebird-midflap.png').convert_alpha()
#bird_surface = pygame.transform.scale2x(bird_surface)
#bird_rect = bird_surface.get_rect(center=(100, 462))

pipe_surface = pygame.image.load('C:/Users/hgf/PycharmProjects/FlappyGame/Graphics/pipe-red.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1100)
pipe_height = [400, 600, 800]

game_over_surface =  pygame.transform.scale2x(pygame.image.load('C:/Users/hgf/PycharmProjects/FlappyGame/Graphics/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(288, 450))
# Sound
#flap_sound = pygame.mixer.Sound('C:/Users/hgf/PycharmProjects/FlappyGame/Sound/sfx_wing.wav')
#death_sound = pygame.mixer.Sound('C:/Users/hgf/PycharmProjects/FlappyGame/Sound/sfx_hit.wav')
#score_sound = pygame.mixer.Sound('C:/Users/hgf/PycharmProjects/FlappyGame/Sound/sfx_point.wav')
score_sound_countdown = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12
                winsound.PlaySound('C:/Users/hgf/PycharmProjects/FlappyGame/Sound/sfx_wing.wav', winsound.SND_ASYNC)
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (200, 462)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
                bird_surface, bird_rect = bird_animation()

    screen.blit(bg_surface, (0, 0))
    if game_active:
    # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

    # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            winsound.PlaySound('C:/Users/hgf/PycharmProjects/FlappyGame/Sound/sfx_point.wav', winsound.SND_ASYNC)
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')

    floor_x_pos -= 1
    draw_floor()

    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)



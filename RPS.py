import pygame
import random
import time
pygame.init()
clock = pygame.time.Clock()

bg = pygame.image.load("bg.svg")
tie = pygame.image.load("Tie.png")
win_bg = pygame.image.load("Win.png")
lose = pygame.image.load("Lose.png")
s = pygame.display.set_mode((1362, 800))
pygame.display.set_caption("Rock, Paper, Scissors, Shoot!")

win = None
plays = []
play_indx = 0
player = ""

class robot(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        robo_hand = pygame.image.load(image)
        self.image = robo_hand.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class human(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        human_hand = pygame.image.load(image)
        self.image = human_hand.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class you(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        box = pygame.image.load(image)
        self.image = box.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class not_you(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        box = pygame.image.load(image)
        self.image = box.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class one(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        one = pygame.image.load(image)
        self.image = one
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class two(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        two = pygame.image.load(image)
        self.image = two
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class three(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        three = pygame.image.load(image)
        self.image = three
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


sprites = pygame.sprite.Group()
robot1 = robot("robot.png", 1100, 300)
human1 = human("human.png", -35, 300)
you = you("You.png", -200, 30)
not_you = not_you("Robot.png", 900, 30)
one1 = one("1.png", 100, 400)
two2 = two("2.png", 400, 400)
three3 = three("3.png", 700, 400)
sprites.add(robot1, human1, you, not_you, one1, two2, three3)

def robo_logic():
    global sprites, robot, plays, play_indx
    plays = ["Rock.png", "Paper.png", "Scissors.png"]
    play_indx = random.randint(0,2)

    if play_indx == 0:
        robot1 = robot(plays[play_indx], 1100, 300)
        sprites.add(robot1)
    elif play_indx == 1:
        robot1 = robot(plays[play_indx], 1100, 300)
        sprites.add(robot1)
    elif play_indx == 2:
        robot1 = robot(plays[play_indx], 1100, 300)
        sprites.add(robot1)

    time.sleep(1)

def game_logic():
    global play_indx, win, player, s

    if player == "Rock" and play_indx == 0:
        s.blit(tie, (0,0))
        pygame.display.flip()
        time.sleep(2)
        player = ""
    if player == "Rock" and play_indx == 1:
        s.blit(lose, (0,0))
        pygame.display.flip()
        time.sleep(1)
        win = False
    if player == "Rock" and play_indx == 2:
        s.blit(win_bg, (0,0))
        pygame.display.flip()
        time.sleep(1)
        win = True
    if player == "Paper" and play_indx == 0:
        s.blit(win_bg, (0,0))
        pygame.display.flip()
        time.sleep(1)
        win = True
    if player == "Paper" and play_indx == 1:
        s.blit(tie, (0,0))
        pygame.display.flip()
        time.sleep(2)
        player = ""
    if player == "Paper" and play_indx == 2:
        s.blit(lose, (0,0))
        pygame.display.flip()
        time.sleep(1)
        win = False
    if player == "Scissors" and play_indx == 0:
        s.blit(lose, (0,0))
        pygame.display.flip()
        time.sleep(1)
        win = False
    if player == "Scissors" and play_indx == 1:
        s.blit(win_bg, (0,0))
        pygame.display.flip()
        time.sleep(1)
        win = True
    if player == "Scissors" and play_indx == 2:
        s.blit(tie, (0,0))
        pygame.display.flip()
        time.sleep(2)
        player = ""

if __name__ == "__main__":
    start = False
    while True:
        s.blit(bg, (0,0))
        if win == False or win == True:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if one1.rect.collidepoint(x, y):
                    start = True
                    player = "Rock"
                    human1 = human("Rock1.png", -5, 300)
                    sprites.add(human1)
                if two2.rect.collidepoint(x, y):
                    start = True
                    player = "Scissors"
                    human1 = human("Scissors1.png", -5, 300)
                    sprites.add(human1)
                if three3.rect.collidepoint(x, y):
                    start = True
                    player = "Paper"
                    human1 = human("Paper1.png", -5, 300)
                    sprites.add(human1)
        if start:
            robo_logic()
            start = False
        game_logic()
        s.blit(bg, (0,0))
        sprites.draw(s)
        pygame.display.flip()
        clock.tick(50)

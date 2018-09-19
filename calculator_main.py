import pygame
import calculator
import re

pygame.init()

GREY = (50,50,50)
BLACK = (0,0,0)
WHITE = (251,251,251)
YELLOW = (255,255,0)
RED = (255,0,0)

size = (400,480)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Calculator")

pygame.font.init()
font = pygame.font.SysFont('Courier New',60)

clock = pygame.time.Clock()

buttons = {}

ROWS = ("a","b","c","d","e")

ALL_BUTTONS = {
    "a1":"+", "a2":"-","a3":"*", "a4":"/",
    "b1":"7", "b2":"8", "b3": "9",
    "c1":"4", "c2":"5", "c3": "6",
    "d1": "1", "d2": "2", "d3": "3",
    "b4": "clear",
    "c4": "back",
    "d4": "enter",
    "e2": "0",
}

displayed = []
dis_color = WHITE

running = True
while running:
    
    screen.fill(GREY)

    #input area
    pygame.draw.rect(screen, BLACK, [10,10,380,60])

    for i in range(4):
        #row1
        pygame.draw.rect(screen,WHITE,[10 + 100 * i,80,80,60])
        buttons["a" + str(i+1)] = pygame.Rect(10 + 100 * i,80,80,60)
        #row2
        pygame.draw.rect(screen,WHITE,[10 + 100 * i,160,80,60])
        buttons["b" + str(i+1)] = pygame.Rect(10 + 100 * i,160,80,60)
        #row3
        pygame.draw.rect(screen,WHITE,[10 + 100 * i,240,80,60])
        buttons["c" + str(i+1)] = pygame.Rect(10 + 100 * i,240,80,60)
        #row4
        pygame.draw.rect(screen,WHITE,[10 + 100 * i,320,80,60])
        buttons["d" + str(i+1)] = pygame.Rect(10 + 100 * i,320,80,60)

    pygame.draw.rect(screen,WHITE,[110,400,80,60])
    buttons["e2"] = pygame.Rect(110,400,80,60)

    #row 1
    screen.blit(font.render("+",False,BLACK),(35,85))
    screen.blit(font.render("-",False,BLACK),(145,85))
    screen.blit(font.render("x",False,BLACK),(240,85))
    screen.blit(font.render("/",False,BLACK),(343,87))
    #row2
    screen.blit(font.render("7",False,BLACK),(35,167))
    screen.blit(font.render("8",False,BLACK),(141,169))
    screen.blit(font.render("9",False,BLACK),(240,167))
    screen.blit(font.render("CL",False,BLACK),(323,167))
    #row3
    screen.blit(font.render("4",False,BLACK),(35,247))
    screen.blit(font.render("5",False,BLACK),(141,249))
    screen.blit(font.render("6",False,BLACK),(240,247))
    screen.blit(font.render("BK",False,BLACK),(323,247))
    #row4
    screen.blit(font.render("1",False,BLACK),(35,327))
    screen.blit(font.render("2",False,BLACK),(141,329))
    screen.blit(font.render("3",False,BLACK),(240,327))
    screen.blit(font.render("=",False,BLACK),(333,327))
    #0
    screen.blit(font.render("0",False,BLACK),(139,409))
    
    i = 0
    for char in displayed:
        multiplier = abs(i - len(displayed))
        screen.blit(font.render(char,False,dis_color), (380 - multiplier*40, 20))
        i += 1

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            x,y = mouse_pos

            #check if and which button is clicked
            for i in range(5):
                if y >= 80 * (i+1) and y <= 80 * (i+1) + 60:
                    row = ROWS[i]
                    break
            else:
                row = None
            for i in range(4):
                if x >= 10 + (100*i) and x <= 10 + (100*i) + 80:
                    col = str(i + 1)
                    break
            else:
                col = None
            
            if row and col:
                
                if len(displayed) > 0:
                    if displayed[0] == "E":
                        displayed = []
                if dis_color == YELLOW:
                    displayed = []

                button_grid_name = row + col
                button_name = ALL_BUTTONS[button_grid_name]
                button_rect = buttons[button_grid_name]

                if button_name == "clear":
                    displayed = []
                    dis_color = WHITE
                elif button_name == "back":
                    if displayed:
                        displayed.pop()
                    dis_color = WHITE
                elif button_name == "enter":
                    dis_color = YELLOW
                    state = "".join(displayed)
                    try:
                        sections = re.findall(r"[\d]+|[-+*/]",state)
                        result = int(sections[0])
                        if len(sections) > 0:
                            for i in range(len(sections) - 2):
                                if sections[i + 1] in ("+","-","*","/"):
                                    result = calculator.operations[sections[i + 1]](result,int(sections[i + 2]))
                                    if isinstance(result,float):
                                        if result.is_integer():
                                            result = int(result)
                            displayed = []
                            for char in str(result):
                                displayed.append(char)
                            print(state,sections)
                        else:
                            pass
                    except:
                        dis_color = RED
                        displayed = ["E","R","R","O","R"]

                else:
                    if len(displayed) == 9:
                        continue
                    dis_color = WHITE
                    displayed.append(button_name)

        



                
                


                
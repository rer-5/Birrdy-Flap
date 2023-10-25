import pygame
from random import randint
pygame.init()
canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
canvas_rect = canvas.get_rect()
w_canvas = canvas_rect.right
h_canvas = canvas_rect.bottom
clock = pygame.time.Clock()
pygame.display.set_caption("Birrdy Flap")
def window(background):
    global keys, mouse, mousepos, down_track, up_track
    if background:
        canvas.fill(colors["Sky"])
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()[0]
    mousepos = pygame.mouse.get_pos()
    up_track = False
    down_track = False
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                down_track = True
            if event.button == 5:
                up_track = True
def text(text, x, y, si, col, font):
    font = pygame.font.SysFont(font,si)
    texting = font.render(text, True, col)
    x -= texting.get_width()/2
    canvas.blit(texting, (x,y))
def back_button():
    pygame.draw.polygon(canvas, "black",[(100,50),(50,100),(100,150)])
    pygame.draw.rect(canvas, "black", (75,75,100,50))
    if mouse:
        if pygame.Rect(50,50,125,100).collidepoint(mousepos):
            return False
        else:
            return True
    else:
        return True
def setset(min,max):
    sum = max - min
    if mouse and pygame.Rect(w_canvas/2 -300, 300+150*setcount-colour_size, 600, 100).collidepoint(mousepos):
        num = int(((mousepos[0]-((w_canvas - 600)/2))/(600/(sum+1)))) + min
        return num
    else:
        return settings[setting][0]
class Pipe():
    def __init__(self, h, y):
        self.rect = pygame.Rect(w_canvas, y, settings["Pipe Size"][0], h)
        self.cna = True
openui = True
colour_select = False
settings_select = False
cosmetic_select = False
colours = ["black","grey","white","brown","red","yellow","blue","orange","green","purple","blueviolet","magenta","pink","light green","dark green","dark blue","cornflowerblue","cyan", "dark cyan","aquamarine","coral","crimson","deepskyblue"]
colors = {"Body":colours[randint(0,len(colours)-2)],"Beak":"orange","Eye":"black","Wing":"black","Text":"black","Pipe":"green","Sky":"deepskyblue","Grass":"lightgreen","End":"brown"}
colour = "Body"
for red in range(1,6):
    for green in range(1,6):
        for blue in range(1,6):
            colours.append((red*50,green*50,blue*50))
settings = {"Speed":[5,1,25], "Gravity":[100,1,500], "Jump":[7,1,12], "Pipe Size":[75,1,200], "Bird Size":[100,10,200],"Floor Size":[100,10,500],"Fps":[60,10,60]}
bird_rect = pygame.Rect(0,0,0,0)
bird_size = 100
cosmetics = {
    "Body":[2,False,pygame.draw.rect(canvas, colors["Body"], (bird_rect)),pygame.draw.circle(canvas, colors["Body"], [bird_rect.x+bird_size/2,bird_rect.y+bird_size/2], bird_size/2)],
    "Beak":[2,False,pygame.draw.polygon(canvas, colors["Beak"], [(bird_rect.right,bird_rect.top+bird_size/5),(bird_rect.right,bird_rect.top+bird_size/20*9),(bird_rect.right+bird_size*17.5/100,bird_rect.top+bird_size/4)])],
    "Eye":[2,False,pygame.draw.circle(canvas, colors["Eye"], [bird_rect.right-bird_size/5,bird_rect.top+bird_size/5], bird_size/20)],
    "Wing":[2,False,pygame.draw.circle(canvas, colors["Wing"], [bird_rect.x+bird_size/10,bird_rect.bottom-bird_size/10*6], int(bird_size/4), int(bird_size/4), draw_bottom_right=True, draw_bottom_left=True)]
}
bestscore = 0
while True:
    while openui:
        window(True)
        text("Birrdy Flap", w_canvas/2 -10, 60, 300, "black", "jungleadventurer")
        text("Birrdy Flap", w_canvas/2, 50, 300, "white", "jungleadventurer")
        play_rect = pygame.Rect(w_canvas/2 -125, h_canvas/2 - 125, 250, 250)
        pygame.draw.rect(canvas, colors["Grass"], (0,h_canvas-100,w_canvas,100))
        pygame.draw.polygon(canvas, "black",[(w_canvas/2 + 100,h_canvas/2),(w_canvas/2 - 100, h_canvas/2 - 100),(w_canvas/2 - 100, h_canvas/2 + 100)])
        pygame.draw.rect(canvas, "black", play_rect, width=5)
        colour_rect = pygame.Rect(w_canvas/4 -50, h_canvas/2 -125, 100, 100)
        pygame.draw.rect(canvas, colors["Body"], colour_rect)
        cosmetic_rect = pygame.Rect(w_canvas/4 -50, h_canvas/2 +25, 100, 100)
        pygame.draw.rect(canvas, colors["Beak"], cosmetic_rect)
        pygame.draw.circle(canvas, "black", (cosmetic_rect.x+50,cosmetic_rect.y+25),20)
        pygame.draw.rect(canvas,"black",(cosmetic_rect.x+25,cosmetic_rect.bottom-50,50,50))
        settings_rect = pygame.Rect(w_canvas/4*3 -50, h_canvas/2 -50, 100, 100)
        pygame.draw.rect(canvas, "gray", settings_rect)
        pygame.draw.ellipse(canvas, "black", settings_rect, width=5) 
        pygame.draw.circle(canvas, "black", (settings_rect.right-50, settings_rect.bottom-50), 25, width=5)
        if mouse:
            if play_rect.collidepoint(mousepos):
                openui = False
            if colour_rect.collidepoint(mousepos):
                colour_select = True
                colour_size = 0
            if settings_rect.collidepoint(mousepos):
                settings_select = True
                colour_size = 0
            if cosmetic_rect.collidepoint(mousepos):
                cosmetic_select = True
                colour_size = 0
        if keys[pygame.K_SPACE]:
            openui = False
        while colour_select:
            window(True)
            setcount = 0
            for color in colors:
                color_rect = pygame.Rect(50,250+150*setcount-(colour_size),100,100)
                pygame.draw.rect(canvas, colors[color], color_rect)
                if colors[color] == "black":
                    text(str(color),color_rect.x+50,color_rect.y+37.5,50,"white","jungleadventurer")
                else:
                    text(str(color),color_rect.x+50,color_rect.y+37.5,50,"black","jungleadventurer")
                if colour == color:
                    pygame.draw.rect(canvas, "green", color_rect, width=5)
                if mouse:
                    if color_rect.collidepoint(mousepos):
                        colour = color
                setcount += 1
            for clour in colours:
                clour_rect = pygame.Rect(w_canvas/5*(((colours.index(clour))%4)+1)-50,250+150*int(colours.index(clour)/4)-(colour_size),100,100)
                pygame.draw.rect(canvas, clour, clour_rect)
                if clour == colors[colour]:
                    pygame.draw.rect(canvas, "green", clour_rect, width=5)
                if mouse:
                    if clour_rect.collidepoint(mousepos):
                        colors[colour] = clour
            if colour_size < 300+150*int(colours.index(clour)/4)-h_canvas/5*4:
                if keys[pygame.K_DOWN]:
                    colour_size += 10
                if keys[pygame.K_RIGHT] or up_track:
                    colour_size += 100
            if colour_size > 0:
                if keys[pygame.K_UP]:
                    colour_size -= 10
                if keys[pygame.K_LEFT] or down_track:
                    colour_size -= 100
            text("Colour Select", w_canvas/2, 50, 200, colors["Text"], "jungleadventurer")
            colour_select = back_button()
            pygame.display.update()
            clock.tick(60)
        while settings_select:
            window(True)
            canvas.fill("grey")
            setcount = 0
            for setting in settings:
                pygame.draw.rect(canvas, "black", (w_canvas/4 -300, 300+150*setcount-(colour_size), 300, 100),width=5)
                pygame.draw.rect(canvas, "black", (w_canvas-300, 300+150*setcount-(colour_size), 200, 100),width=5)
                text(str(setting), w_canvas/4 -150, 300+150*setcount+25-(colour_size), 75, "black", "jungleadventurer")
                text(str(settings[setting][0]), w_canvas-200, 300+150*setcount+25-(colour_size), 75, "black", "jungleadventurer")
                pygame.draw.rect(canvas, "black", pygame.Rect(w_canvas/2 -300, 300+150*setcount-(colour_size), 600, 100),width=5)
                pygame.draw.rect(canvas, "black", pygame.Rect((settings[setting][0] - settings[setting][1])*(600/(settings[setting][2]-settings[setting][1]+1))+425, 287.25+150*setcount-(colour_size), 50, 125))
                settings[setting][0] = setset(settings[setting][1],settings[setting][2])
                setcount += 1
            text("Settings", w_canvas/2, 50, 200, "black", "jungleadventurer")
            settings_select = back_button()
            pygame.draw.rect(canvas,"black",(w_canvas-350,50,300,100))
            text("Reset to Default",w_canvas-200,87.5,50,"white","jungleadventurer")
            if pygame.Rect(w_canvas-350,50,300,100).collidepoint(mousepos):
                if mouse:
                    settings = {"Speed":[5,1,25], "Gravity":[100,1,500], "Jump":[7,1,12], "Pipe Size":[75,1,200], "Bird Size":[100,10,200],"Floor Size":[100,10,500],"Fps":[60,10,60]}
            if colour_size < 300+150*int(setcount)-h_canvas/5*4:
                if keys[pygame.K_DOWN] or up_track:
                    colour_size += 50
            if colour_size > 0:
                if keys[pygame.K_UP] or down_track:
                    colour_size -= 50
            pygame.display.update()
            clock.tick(60)
        while cosmetic_select:
            window(colors["Sky"])
            setcount = 0
            for cosmetic in cosmetics:
                cosmetic_rect = pygame.Rect(50,250+150*setcount-(colour_size),100,100)
                text(str(cosmetic),cosmetic_rect.x+50,cosmetic_rect.y+37.5,50,colors["Text"],"jungleadventurer")
                for cos in cosmetics[cosmetic]:
                    if cosmetics[cosmetic].index(cos):
                        if cosmetics[cosmetic].index(cos) == 1:
                            pass
                        else:
                            cos
                setcount += 1
            text("Cosmetic Select", w_canvas/2, 50, 200, colors["Text"], "jungleadventurer")
            cosmetic_select = back_button()
            pygame.display.update()
            clock.tick(60)
        pygame.display.update()
        clock.tick(60)
    size = settings["Bird Size"][0] 
    x = w_canvas/4
    y = (h_canvas-settings["Floor Size"][0])/2
    bird_rect = pygame.Rect(x-size/2, y-size/2, size, size)
    running = True
    can = True
    grav = 1
    jt = settings["Jump"][0]
    score = 0
    grass = pygame.Rect(0, h_canvas-settings["Floor Size"][0], w_canvas, settings["Floor Size"][0])
    pipetimer = 0
    pipes = []
    while running:
        window(True)
        cosmetics = {
    "Body":[2,False,[pygame.draw.rect,(bird_rect)],[pygame.draw.circle,[bird_rect.x+bird_size/2,bird_rect.y+bird_size/2], bird_size/2,True,True,True,True]],
    "Beak":[2,False,[pygame.draw.polygon,[(bird_rect.right,bird_rect.top+bird_size/5),(bird_rect.right,bird_rect.top+bird_size/20*9),(bird_rect.right+bird_size*17.5/100,bird_rect.top+bird_size/4)]]],
    "Eye":[2,False,[pygame.draw.circle,[bird_rect.right-bird_size/5,bird_rect.top+bird_size/5], bird_size/20,True,True,True,True]],
    "Wing":[2,False,[pygame.draw.circle,[bird_rect.x+bird_size/10,bird_rect.bottom-bird_size/10*6], int(bird_size/4),False,False,True,True]]
    }
        pygame.draw.rect(canvas, colors["Grass"], grass)
        for pipe in pipes:
            pygame.draw.rect(canvas, colors["Pipe"], pipe.rect)
            pipe.rect.x -= settings["Speed"][0]
            if pipe.rect.right < 0:
                pipes.remove(pipe)
            if pipe.rect.right < bird_rect.left:
                if pipe.cna:
                    score += 0.5
                    pipe.cna = False
            if pygame.Rect.colliderect(pipe.rect, bird_rect):
                running = False 
        if pygame.Rect.colliderect(grass, bird_rect):
            running = False 
        text(str(int(score)), w_canvas/2, 50, 200, colors["Text"], "jungleadventurer")
        for cosmetic in cosmetics:
            if cosmetics[cosmetic][cosmetics[cosmetic][0]]:
                if len(cosmetics[cosmetic][cosmetics[cosmetic][0]]) == 7:
                    cosmetics[cosmetic][cosmetics[cosmetic][0]][0](canvas, colors[cosmetic],cosmetics[cosmetic][2][1],cosmetics[cosmetic][2][2],draw_top_left=cosmetics[cosmetic][2][3],draw_top_right=cosmetics[cosmetic][2][4],draw_bottom_left=cosmetics[cosmetic][2][5],draw_bottom_right=cosmetics[cosmetic][2][6])
                else:
                    cosmetics[cosmetic][cosmetics[cosmetic][0]][0](canvas, colors[cosmetic],cosmetics[cosmetic][2][1])
        if keys[pygame.K_SPACE] or mouse:
            if can:
                grav = 1
                jt = settings["Jump"][0]
                can = False
        elif not keys[pygame.K_SPACE]: 
            can = True
        F =(1/2)*grav*(jt**2)
        bird_rect.y -= F
        jt -= 1  
        if jt < 0:
            grav = settings["Gravity"][0]/-1000
        pipetimer += 1
        if pipetimer >= 500/settings["Speed"][0]:
            r1 = randint(0, h_canvas-200-settings["Floor Size"][0])
            r2 = randint(2*settings["Bird Size"][0], 5*settings["Bird Size"][0])
            pipes.append(Pipe(r1, 0))
            pipes.append(Pipe(h_canvas-settings["Floor Size"][0]-r1-r2, r1+r2))
            pipetimer = 0
        bird_rect.clamp_ip(canvas_rect)
        pygame.display.update()
        clock.tick(settings["Fps"][0])
    gamecard = True
    while gamecard:
        window(False)
        pygame.draw.rect(canvas, colors["End"], (w_canvas/2 -250, h_canvas/2 -250, 500, 500))
        if score > bestscore:
            bestscore = score
        text(f"Your Score: {int(score)}", w_canvas/2, h_canvas/2 -225, 100, colors["Text"], "jungleadventurer")
        text(f"Best Score: {int(bestscore)}", w_canvas/2, h_canvas/2 -150, 100, colors["Text"], "jungleadventurer")
        text("Play again?", w_canvas/2, h_canvas/2 -75, 50, colors["Text"], "jungleadventurer")
        play_rect = pygame.Rect(w_canvas/2 -125, h_canvas/2 - 25, 250, 250)
        pygame.draw.polygon(canvas, "black",[(w_canvas/2 + 100,h_canvas/2 + 100),(w_canvas/2 - 100, h_canvas/2),(w_canvas/2 - 100, h_canvas/2 + 200)])
        pygame.draw.rect(canvas, "black", play_rect, width=5)
        if mouse:
            if play_rect.collidepoint(mousepos):
                gamecard = False
        pygame.draw.polygon(canvas, "black",[(100,50),(50,100),(100,150)])
        pygame.draw.rect(canvas, "black", (75,75,100,50))
        if mouse:
            if pygame.Rect(50,50,125,100).collidepoint(mousepos):
                gamecard = False
                openui = True
        pygame.display.update()
        clock.tick(60)
from pygame import *
import math, random

print """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..:: { PAINT } :..
Designed by Mudassir Chughtai
--------------------------------------
Key             Function
Escape          Quit
u               Undo
r               Redo
s               Save Image
o               Open Image
c               Close Polygon
f               Flip Stamp
Scroll Up       Increase Tool Size
Scroll Down     Decrease Tool Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Font
init()
fnt = font.SysFont("Cambria", 23, True)

# Screen
screen = display.set_mode((1024, 768))
display.set_caption("..:: { PAINT } ::..")

# Tools
tools = ["Pencil", "Line", "Brush", "Airbrush", "Eraser", "Rectangle", "Ellipse", "Polygon", "Bucket", "Dropper", "Stamps", "Fill","None"]
descriptions = ["Draws like a pencil.", "Draws lines. Scroll up or down to change thickness.", "Draws like a brush. Scroll up or down to change thickness.",\
                "Sprays like a can. Scroll up or down to change size.", "Erases. Scroll up or down to change size.",\
                "Draws rectangles. Right click and drag to draw filled rectangles.", "Draws ellipses. Right click and drag to draw filled ellipses.",\
                "Polygon tool. Press 'c' to close the polygon. Right click for filled polygon.", "Fills the screen to the set colour. Right click to clear the screen.",\
                "Selects a colour on the canvas where the mouse is clicked.", "Stamps. Press 'f' to flip. Right click and drag to rotate."]
tool = "Pencil"
txt = descriptions[0]

# Icons
pencilIcon = image.load("Icons//Pencil.PNG")
brushIcon = image.load("Icons//Brush.PNG")
sprayIcon = image.load("Icons//Spray.PNG")
eraseIcon = image.load("Icons//Eraser.PNG")
bucketIcon = image.load("Icons//Bucket.PNG")
dropperIcon = image.load("Icons//Dropper.PNG")

# Stamps
stamps = ["Goku1", "Goku2", "Goku3", "Gohan1", "Gohan2", "Vegeta1", "Vegeta2", "Vegeta3", "Blast1", "Blast2", "Blast3", "Trunks1", "Trunks2", "Trunks3", "ThisGuy", "Piccolo"]
icons = []
icons2 = []
stamp = "None"

for i in range(8):
    icons.append(Rect(105+i*60, 610, 50,50))
    icons2.append(Rect(105+i*60, 670, 50,50))

goku1 = image.load("Stamps//goku1.PNG")
goku2 = image.load("Stamps//goku2.PNG")
goku3 = image.load("Stamps//goku3.PNG")
gohan1 = image.load("Stamps//gohan1.PNG")
gohan2 = image.load("Stamps//gohan2.PNG")
vegeta1 = image.load("Stamps//vegeta1.PNG")
vegeta2 = image.load("Stamps//vegeta2.PNG")
vegeta3 = image.load("Stamps//vegeta3.PNG")
blast1 = image.load("Stamps//blast.PNG")
blast2 = image.load("Stamps//blast2.PNG")
blast3 = image.load("Stamps//blast3.PNG")
trunks1 = image.load("Stamps//trunks1.PNG")
trunks2 = image.load("Stamps//trunks2.PNG")
trunks3 = image.load("Stamps//trunks3.PNG")
thisguy = image.load("Stamps//thisguy.PNG")
piccolo = image.load("Stamps//piccolo.PNG")

stampsBack = image.load("Stamps//Stamps.BMP")

pointList = [] # Polygon
pointList2 = []

# Background
backgroundImg = image.load("Background.PNG")
screen.blit(backgroundImg,(0,0))

# Colour
colourRect = Rect(598,600,403,119)
colour = (0,0,0)
eraserColour = (255,255,255)

# Canvas
canvas = Rect(95,15,906,580)
screen.fill((255,255,255),canvas)

screen2 = screen.copy()

# Text
mouseBack = image.load("Icons//Mouse.BMP")
descriptionBack = image.load("Icons//Descriptions.BMP")

mx = my = 0 # Mouse Location

# Buttons
buttons = []
for i in range(11):
    buttons.append(Rect(15, 15+i*60, 55,55))
draw.rect(screen2,(0,0,255), buttons[0],3)

# Tool widths
brushThickness = 5
airThickness = 10
lineWidth = 1
eraserWidth = 5

undos = []
redos = []

running = True
while running:
    
    omx,omy = mx,my # Old mouse location
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    screen.blit(screen2,(0,0))
    
    draw.rect(screen,colour,Rect(853,722,45,45)) # Rect displaying Colour        
    
    click = False
    rclick = False
    for evt in event.get():
        if evt.type == QUIT: running = False
        if evt.type == KEYDOWN:
            if evt.key == K_ESCAPE: running = False
            if evt.key == K_s: image.save(screen.subsurface(canvas),str(raw_input("Name your file: "))+".BMP") # Saves canvas as a .BMP image
            if evt.key == K_o:
                screen.set_clip(canvas)
                img = image.load(str(raw_input("Enter the name of the file (including the extension): ")))
                screen.blit(img,(95,15))
                screen.set_clip(None)
            if evt.key == K_u:
                if len(undos) > 0:
                    screen2.blit(undos[-1],(95,15))
                    redos.append(undos[-1])
                    if tool == "Polygon":
                        if len(pointList)>1: del pointList[-1]
                    del undos[-1]
            if evt.key == K_r:
                if len(redos) > 0:
                    screen2.blit(redos[-1],(95,15))
                    undos.append(redos[-1])
                    del redos[-1]
            if evt.key == K_f:
                if tool == "Stamps":
                    if stamp == "Goku1": goku1 = transform.flip(goku1,1,0)
                    if stamp == "Goku2": goku2 = transform.flip(goku2,1,0)
                    if stamp == "Goku3": goku3 = transform.flip(goku3,1,0)
                    if stamp == "Gohan1": gohan1 = transform.flip(gohan1,1,0)
                    if stamp == "Gohan2": gohan2 = transform.flip(gohan2,1,0)
                    if stamp == "Vegeta1": vegeta1 = transform.flip(vegeta1,1,0)
                    if stamp == "Vegeta2": vegeta2 = transform.flip(vegeta2,1,0)
                    if stamp == "Vegeta3": vegeta3 = transform.flip(vegeta3,1,0)
                    if stamp == "Blast1": blast1 = transform.flip(blast1,1,0)
                    if stamp == "Blast2": blast2 = transform.flip(blast2,1,0)
                    if stamp == "Blast3": blast3 = transform.flip(blast3,1,0)
                    if stamp == "Trunks1": trunks1 = transform.flip(trunks1,1,0)
                    if stamp == "Trunks2": trunks2 = transform.flip(trunks2,1,0)
                    if stamp == "Trunks3": runks3 = transform.flip(trunks3,1,0)
                    if stamp == "ThisGuy": thisguy = transform.flip(thisguy,1,0)
                    if stamp == "Piccolo": piccolo = transform.flip(piccolo,1,0)
            if evt.key == K_c:
                if tool == "Polygon":
                    if len(pointList) > 1:
                        screen2.blit(copy3,(0,0)) # Gets rid of the parameter markers and draws the polygon
                        mx3,my3 = pointList[0]
                        draw.polygon(screen2,colour,pointList,2)
                        pointList = [] # Clears list
                    if len(pointList2) > 2:
                        screen2.blit(copy4,(0,0))
                        mx4,my4 = pointList2[0]
                        draw.polygon(screen2,colour,pointList2)
                        pointList2 = []
        if evt.type == MOUSEBUTTONDOWN:
            click = True
            redos = []
            if evt.button == 1:
                mxu,myu = mx,my 
                mx2,my2 = mouse.get_pos() # Location of mouse when clicked
                copy = screen.copy()
            if evt.button == 3:
                rclick = True
                mxd,myd = mx,my
                mx5,my5 = mouse.get_pos()
                copy2 = screen.copy()
            # Changes tool thickness within set values
            if evt.button == 4:
                if tool == "Brush":
                    if brushThickness < 45: brushThickness += 1
                if tool == "Airbrush":
                    if airThickness < 100: airThickness += 5
                if tool == "Line":
                    if lineWidth < 10: lineWidth += 2
                if tool == "Eraser":
                    if eraserWidth < 75: eraserWidth += 10
            if evt.button == 5:
                if tool == "Brush":
                    if brushThickness > 2: brushThickness -= 1
                if tool == "Airbrush":
                    if airThickness > 10: airThickness -= 5
                if tool == "Line":
                    if lineWidth > 1: lineWidth -= 2
                if tool == "Eraser":
                    if eraserWidth > 5: eraserWidth -= 10
        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1 or evt.button == 3 and canvas.collidepoint(mx,my): undos.append(screen.subsurface(canvas).copy())
            if evt.button == 1: mx3,my3 = mouse.get_pos()
            if evt.button == 3: mx4,my4 = mouse.get_pos()
    
    # Colour Select
    if colourRect.collidepoint(mx,my) and mb[0] == 1:
        colour = screen.get_at((mx,my))
    
    # Print Description
    screen.blit(descriptionBack,(15,735))
    for i in range(11):
        if tool == tools[i]: txt = descriptions[i]
    
    
    for i in range(11):
        if buttons[i].collidepoint(mx,my):
            txt = descriptions[i] # Print Description
            # Select Tool
            if click == True:
                tool = tools[i]
                screen2.blit(backgroundImg,(0,0))
                draw.rect(screen2,(0,0,255), buttons[i],3)
    
    # Mouse Location
    screen.blit(mouseBack,(900,721))
    text = "-- --" # If mouse not on canvas
    
    # Draw On Canvas
    if canvas.collidepoint(mx,my):
        
        # Mouse Location
        text = "%3d %2d" % (mx-95,my-15)
        
        screen.set_clip(canvas)
        screen2.set_clip(canvas)
        
        if tool == "Pencil":
            mouse.set_visible(False)
            screen.blit(pencilIcon,(mx,my-pencilIcon.get_height()))
            if mb[0] == 1:draw.aaline(screen2,colour,(omx,omy),(mx,my),2)
        if tool == "Line" and mb[0] == 1:
            screen2.blit(copy,(0,0)) # Displays 1 line instead of multiple lines following the mouse
            draw.line(screen2,colour,(mxu,myu),(mx,my),lineWidth)
        if tool == "Brush":
            mouse.set_visible(False)
            screen.blit(brushIcon,(mx,my-brushIcon.get_height()))
            dist = math.hypot((mx-omx),(my-omy))
            if dist == 0: dist = 1
            sx = (mx-omx)/dist
            sy = (my-omy)/dist
            for i in range(int(dist)):
                if mb[0] == 1: draw.circle(screen2,colour,(int(omx+sx*i),int(omy+sy*i)),brushThickness) # Fills in skips
        if tool == "Airbrush":
            mouse.set_visible(False)
            if eraserColour == (0,0,0): draw.circle(screen,(255,255,255),(mx,my),airThickness,1)
            else: draw.circle(screen,(0,0,0),(mx,my),airThickness,1)
            screen.blit(sprayIcon,(mx+5,my-25))
            for i in range(airThickness):
                a = random.randint(mx-airThickness,mx+airThickness)
                b = random.randint(my-airThickness,my+airThickness)
                if mb[0] == 1:
                    if ((a-mx)**2+(b-my)**2)**0.5 < airThickness:
                        screen2.set_at((a,b),colour) # Changes the colour of a pixel within specified distance of mouse location        
        if tool == "Eraser":
            # Square brush tool with white colour
            mouse.set_visible(False)
            if eraserColour == (0,0,0): draw.rect(screen,(255,255,255),Rect((mx-int(eraserWidth/2)),(my-int(eraserWidth/2)),eraserWidth,eraserWidth),1)
            else: draw.rect(screen,(0,0,0),Rect((mx-int(eraserWidth/2)),(my-int(eraserWidth/2)),eraserWidth,eraserWidth),1)
            screen.blit(eraseIcon,(mx,my-eraseIcon.get_width()))
            dist = math.hypot((mx-omx),(my-omy))
            if dist == 0: dist = 1
            sx = (mx-omx)/dist
            sy = (my-omy)/dist
            if mb[0] == 1:    
                for i in range(int(dist)):
                    draw.rect(screen2,eraserColour,Rect((int(omx+sx*i)-int(eraserWidth/2)),(int(omy+sy*i)-int(eraserWidth/2)),eraserWidth,eraserWidth))  # Centers the square on mouse, fills in skips                  
        if tool == "Rectangle":
            if mb[0] == 1:
                screen2.blit(copy,(0,0))
                l = (mx-mxu)
                w = (my-myu)
                draw.rect(screen2,colour,Rect(mxu,myu,l,w),2)
            if mb[2] == 1:
                screen2.blit(copy2,(0,0))
                l = (mx-mxd)
                w = (my-myd)
                draw.rect(screen2,colour,Rect(mxd,myd,l,w))                
        
        if tool == "Ellipse":
            if mb[0] == 1:
                screen2.blit(copy,(0,0))
                l = math.fabs((mx-mxu))
                w = math.fabs((my-myu))
                draw.ellipse(screen2,colour,Rect(min(mx,mxu),min(my,myu),max(l,4),max(w,4)),2)
            if mb[2] == 1:
                screen2.blit(copy2,(0,0))
                l = math.fabs((mx-mxd))
                w = math.fabs((my-myd))
                draw.ellipse(screen2,colour,Rect(min(mx,mxd),min(my,myd),l,w))

        if tool == "Polygon":
            if len(pointList) == 0: copy3 = screen.copy()
            if click == True: pointList.append((mx2,my2)) # Adds click location to list for polygon
            if mb[0] == 1:
                screen2.blit(copy,(0,0))
                draw.circle(screen2,colour,(mx2,my2),1)
            if len(pointList2) == 0: copy4 = screen.copy()
            if rclick == True: pointList2.append((mx5,my5))
            if mb[2] == 1:
                screen2.blit(copy2,(0,0))
                draw.circle(screen2,colour,(mx5,my5),1)
            
        
        if tool == "Bucket":
            mouse.set_visible(False)
            screen.blit(bucketIcon,(mx,my-37))
            if mb[0] == 1:
                screen2.fill(colour,canvas)
                eraserColour = colour
            if mb[2] == 1:
                screen2.fill((255,255,255),canvas)
                eraserColour = (255,255,255)
        
        if tool == "Dropper":
            mouse.set_visible(False)
            screen.blit(dropperIcon,(mx-3,my-40))
            if mb[0] == 1: colour = screen2.get_at((mx,my))
        
        screen.set_clip(None)
        screen2.set_clip(None)

    if tool == "Stamps":
        
        screen2.blit(stampsBack,(105,610)) # Stamp Icons

        # Stamp Selection
        if click == True:
            
            for i in range(8):
                if icons[i].collidepoint(mx,my):
                    stamp = stamps[i]
                if icons2[i].collidepoint(mx,my):
                    stamp = stamps[i+8]

        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            screen2.set_clip(canvas)
            
            if stamp == "Goku1":
                screen.blit(goku1,(mx-goku1.get_width()/2,my-goku1.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(goku1,(mx2-goku1.get_width()/2,my2-goku1.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(goku1,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))            
            if stamp == "Goku2":
                screen.blit(goku2,(mx-goku2.get_width()/2,my-goku2.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(goku2,(mx2-goku2.get_width()/2,my2-goku2.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(goku2,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))  
            if stamp == "Goku3":
                screen.blit(goku3,(mx-goku3.get_width()/2,my-goku3.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(goku3,(mx2-goku3.get_width()/2,my2-goku3.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(goku3,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))  
            if stamp == "Gohan1":
                screen.blit(gohan1,(mx-gohan1.get_width()/2,my-gohan1.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(gohan1,(mx2-gohan1.get_width()/2,my2-gohan1.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(gohan1,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Gohan2":
                screen.blit(gohan2,(mx-gohan2.get_width()/2,my-gohan2.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(gohan2,(mx2-gohan2.get_width()/2,my2-gohan2.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(gohan2,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Vegeta1":
                screen.blit(vegeta1,(mx-vegeta1.get_width()/2,my-vegeta1.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(vegeta1,(mx2-vegeta1.get_width()/2,my2-vegeta1.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(vegeta1,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Vegeta2":
                screen.blit(vegeta2,(mx-vegeta2.get_width()/2,my-vegeta2.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(vegeta2,(mx2-vegeta2.get_width()/2,my2-vegeta2.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(vegeta2,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Vegeta3":
                screen.blit(vegeta3,(mx-vegeta3.get_width()/2,my-vegeta3.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(vegeta3,(mx2-vegeta3.get_width()/2,my2-vegeta3.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(vegeta3,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Blast1":
                screen.blit(blast1,(mx-blast1.get_width()/2,my-blast1.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(blast1,(mx2-blast1.get_width()/2,my2-blast1.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(blast1,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Blast2":
                screen.blit(blast2,(mx-blast2.get_width()/2,my-blast2.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(blast2,(mx2-blast2.get_width()/2,my2-blast2.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(blast2,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Blast3":
                screen.blit(blast3,(mx-blast3.get_width()/2,my-blast3.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(blast3,(mx2-blast3.get_width()/2,my2-blast3.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(blast3,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Trunks1":
                screen.blit(trunks1,(mx-trunks1.get_width()/2,my-trunks1.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(trunks1,(mx2-trunks1.get_width()/2,my2-trunks1.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(trunks1,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Trunks2":
                screen.blit(trunks2,(mx-trunks2.get_width()/2,my-trunks2.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(trunks2,(mx2-trunks2.get_width()/2,my2-trunks2.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(trunks2,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Trunks3":
                screen.blit(trunks3,(mx-trunks3.get_width()/2,my-trunks3.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(trunks3,(mx2-trunks3.get_width()/2,my2-trunks3.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(trunks3,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "ThisGuy":
                screen.blit(thisguy,(mx-thisguy.get_width()/2,my-thisguy.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(thisguy,(mx2-thisguy.get_width()/2,my2-thisguy.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(thisguy,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            if stamp == "Piccolo":
                screen.blit(piccolo,(mx-piccolo.get_width()/2,my-piccolo.get_height()/2))
                if mb[0] == 1:
                    screen2.blit(copy,(0,0))
                    screen2.blit(piccolo,(mx2-piccolo.get_width()/2,my2-piccolo.get_height()/2))
                if mb[2] == 1:
                    screen2.blit(copy,(0,0))
                    ang = math.atan2(-(my-myu),mx-mxu)
                    rotPic = transform.rotate(piccolo,math.degrees(ang))
                    screen2.blit(rotPic,(mxu-rotPic.get_width()/2,myu-rotPic.get_height()/2))
            screen.set_clip(None)
            screen2.set_clip(None)

    if canvas.collidepoint(mx,my) == False: mouse.set_visible(True)

    # Mouse Location
    textPic = fnt.render(text,1,(0,0,0))
    screen.blit(textPic,(905,719))

    # Print Description
    txtPic = fnt.render(txt,1,(0,0,0))
    screen.blit(txtPic,(18,732))

    """draw.rect(screen,(0,0,0),(0,0,800,50))
    for i,re in enumerate(redos):
        screen.blit(transform.scale(re,(60,40)),(i*70,5))"""
    display.flip()

del fnt
quit()

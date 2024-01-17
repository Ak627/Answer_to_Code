#Add these to our player variables
Xmoving = False#add these to the variables section and also to the areas where movement happens(ie with the input)
Ymoving = False
direction  = [False, False, False, False]#direction list that holds where the player is facing(ex. Left = 0, Right = 1, etc.)


#LEFT MOVEMENT
if keys[0]==True:
    Xmoving = True#adding the fact that the character is moving in the x position
    vx=-3
    RowNum = 0 #left movement will start on our first row
#RIGHT MOVEMENT
elif keys[1] == True:
    Xmoving = True
    vx = 3
    RowNum = 1#notice what's different between LEFT and RIGHT
#turn off velocity
else:
    Xmoving = False
    vx = 0
#UP movement
if keys[2]==True:
    Ymoving = True
    vy=-3
    RowNum = 2 #left movement will start on our first row
#DOWN MOVEMENT
elif keys[3] == True:
    Ymoving = True#adding the fact that the character is moving in the y position
    vy = 3
    RowNum = 3
#turn off velocity
else:
    Ymoving = False
    vy = 0
#ANIMATION-------------------------------------------------------------------
    
# Update Animation Information
# Only animate when in motion either horizontally or vertically
if Xmoving == True or Ymoving == True:
    ticker += 1
    if ticker%10 ==0:
        frameNum += 1
    if frameNum > 7:
        frameNum = 0
    
if direction[0] == True:#checks what direction we are facing and switches our row number to that area
    RowNum = 0
elif direction[1] == True:
    RowNum = 1
elif direction[2] == True:
    RowNum = 2
elif direction[3] == True:
    RowNum = 3


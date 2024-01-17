Xmoving = False#add these to the variables section and also to the areas where movement happens(ie with the input)
Ymoving = False
direction  = Left#add direction in the same areas relating to where our player is facing


if Xmoving == True or Ymoving == True:
    ticker += 1
if ticker%10 ==0:
    frameNum += 1
if frameNum > 7:
    frameNum = 0
    
    
if direction == Left:
    RowNum = 0
elif direction == Right:
    RowNum = 1
elif direction == Up:
    RowNum = 2
elif direction == Down:
    RowNum = 3

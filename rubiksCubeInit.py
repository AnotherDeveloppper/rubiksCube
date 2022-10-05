

from genericpath import exists
from operator import concat
from os import remove
from turtle import color
from numpy import * 

# colors of rubik cube : ( to be changed)
colors = ["White","Blue","Red","Yellow","Green","Orange","White","Blue","Red","Yellow","Green","Orange","White","Blue","Red","Yellow","Green","Orange","White","Blue","Red","Yellow","Green","Orange",]


# each piece 

class piece :
    pos = 0
    color =  []
    name = ""

    def __init__(self,name, pos,color) -> None:
        self.pos=pos
        self.color=color
        self.name=name


    def changePos(self,Newpos) -> None:
        self.pos=Newpos

    def toString(self):
        print(self.name+" with position: "+ str(self.pos)+" and color: "+' '.join(self.color))
    
    def toString2(self):
        print(' '.join(self.color))

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

# needed variables for loop
y=0 #current face color
facecounter=0   #2 colors pieces counter for each face
facecounter2=0  #3 colors pieces counter for each face
temp=0 # additional value on color to avoid adding 2 opposite face colors together
pieces = [] # list of all our pieces
colorTemp=[]    # temporary colors of each piece
threeColorsTemp = []
threeColors = []
baseColor = "" # color of the face in each loop
oppositeColor = "" # the opposite of the color in each loop
pieceCount = 1
# init all pieces 


# 1 color piece takes current color ( using variable baseColor)

# 2 colors piece takes current color + 1  of the rest 4 colors that can match ( ex : white with all except yellow)
# 3 colors piece takes current color + 2  of the rest 4 colors that can match ( ex : white with all except yellow)



for x in range (0,55) : 
    baseColor =  colors[y]
    oppositeColor = colors[y+3]

    if x==4 or (x-4)%9==0:
        # 1 color
        colorTemp.append(baseColor)

    if x== 1 or x==3 or x==5 or x==7 or (x-1)%9==0 or (x-3)%9==0 or (x-5)%9==0 or (x-7)%9==0:
        # 2 colors
        facecounter+=1
        if facecounter>= 3 :
            temp = facecounter+1
            colorTemp.append(baseColor)
            colorTemp.append(colors[y+temp])
        else : 
            colorTemp.append(baseColor)
            colorTemp.append(colors[y+facecounter])
        temp =0
    if x== 0 or x==2 or x==6 or x==8 or x%9==0 or (x-2)%9==0 or (x-6)%9==0 or (x-8)%9==0:
        # 3 colors
        threeColors = colors.copy()
        threeColorsTemp = colors.copy()
        threeColors = remove_values_from_list(threeColors,baseColor)
        threeColors = remove_values_from_list(threeColors,oppositeColor)
        colorTemp.append(baseColor)
        colorTemp.append(threeColors[0+facecounter2])
        colorTemp.append(threeColors[1+facecounter2])
        facecounter2+=1

    
    if x%9==0 and x!=0:
        y+=1
        facecounter=0
        facecounter2=0
    colorTemp.sort() #we sort all colors stored so we can compare them later to pre existing piece's colors
    
    name = 'piece_{}'.format(pieceCount) 
    exists = False
    for onePiece in pieces :
        if onePiece.color == colorTemp : 
            exists = True

    if exists == False :
        pieces.append(piece(name,pieceCount,colorTemp))
        pieceCount+=1

    colorTemp=[]
    exists= False



# show all pieces
print(" ---- pieces loaded ----")
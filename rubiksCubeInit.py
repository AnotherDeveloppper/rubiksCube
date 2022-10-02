"""
            UUU                                 0  1  2                                                     O O O
            UUU                                 3  4  5                                                     O O O
            UUU                                 6  7  8                                                     O O O
        LLL FFF RRR BBB               9  10 11  18 19 20    27 28 29    36 37 38                   G G G    W W W    B B B   Y Y Y
        LLL FFF RRR BBB               12 13 14  21 22 23    30 31 32    39 40 41                   G G G    W W W    B B B   Y Y Y
        LLL FFF RRR BBB               15 16 17  24 25 26    33 34 35    42 43 44                   G G G    W W W    B B B   Y Y Y
            DDD                                 45 46 47                                                    R R R
            DDD                                 48 49 50                                                    R R R
            DDD                                 51 52 53                                                    R R R
"""



from genericpath import exists
from operator import concat
from turtle import color


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
    

 # needed variables for loop
y=0 #current face color
facecounter=0   #2 colors pieces counter for each face
facecounter2=0  #3 colors pieces counter for each face
temp=0 # additional value on color to avoid adding 2 opposite face colors together
pieces = [] # list of all our pieces
colorTemp=[]    # temporary colors of each piece

# init all pieces 


# 1 color piece takes current color ( using variable y)
# 2 colors piece takes current color + 1  of the rest 4 colors that can match ( ex : white with all except yellow)
# 2 colors piece takes current color + 2  of the rest 4 colors that can match ( ex : white with all except yellow)

for x in range (0,54) : 
    

    if x==4 or (x-4)%9==0:
        # 1 color
        colorTemp.append(colors[y])

    if x== 1 or x==3 or x==5 or x==7 or (x-1)%9==0 or (x-3)%9==0 or (x-5)%9==0 or (x-7)%9==0:
        # 2 colors
        facecounter+=1
        if facecounter>= 3 :
            temp = facecounter+1
            colorTemp.append(colors[y])
            colorTemp.append(colors[y+temp])
        else : 
            colorTemp.append(colors[y])
            colorTemp.append(colors[y+facecounter])
        temp =0
    if x== 0 or x==2 or x==6 or x==8 or x%9==0 or (x-2)%9==0 or (x-6)%9==0 or (x-8)%9==0:
        # 3 colors
        facecounter2+=1
        if facecounter2>=2 :
            temp = facecounter2 +1
            colorTemp.append(colors[y])
            colorTemp.append(colors[y+temp])
            if temp+2 ==6 :
                colorTemp.append(colors[y+temp+2+1])
            else:
                colorTemp.append(colors[y+temp+2])
        else : 
            colorTemp.append(colors[y])
            colorTemp.append(colors[y+1])
            colorTemp.append(colors[y+2])
        temp =0
    
    if x%9==0 and x!=0:
        y+=1
        facecounter=0
        facecounter2=0
    colorTemp.sort()
    
    name = 'piece_{}'.format(x) 
    exists = False
    for onePiece in pieces :
        if onePiece.color == colorTemp : 
            exists = True

    if exists == False :
        pieces.append(piece(name,x,colorTemp))

    colorTemp=[]
    exists= False


# show all pieces
for x in pieces: 
    x.toString()

"""

for x in pieces: 
    x.toString()


        if facecounter2>=2 :
            temp = facecounter2 +1
            colorTemp.append(colors[y])
            colorTemp.append(colors[y+temp])
            if temp+2 ==6  or temp+2 == 12:
                colorTemp.append(colors[y+temp+2+1])
            else:
                colorTemp.append(colors[y+temp+2])
        else : 
            colorTemp.append(colors[y])
            colorTemp.append(colors[y+1])
            colorTemp.append(colors[y+2])
"""
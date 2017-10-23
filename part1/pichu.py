import sys

# Taking inputs from the user
plyr = str(sys.argv[1])
board = str(sys.argv[2])
time_limit = int(sys.argv[3])
state = [['.']*8 for x in xrange(8)]

# Reading board state into list of lists
for x in range(0,8):
    for y in range(0,8):
        state[x][y] = board[y+(x*8)]


#Printing board in single line string from list of lists  
def printing_board_single_line(state):
    board_string = ""
    for x in state:
        for y in x:
          board_string=board_string+y
    return board_string      

#Move Robin function gives all possible moves for Robin at coordinate (a,b) and also takes into account who is playing
# black player or white player
def move_Robin(state,a,b,player):
    if player == "w":
        R = "R"
    else:
        R ="r"
    succ_Robin = []
    for i in [x for x in xrange(-7,8) if x != 0]:
        temp1 = state[:a]+[state[a][:b]+["."]+state[a][b+1:]]+state[a+1:]
        if a+i>-1 and a+i <8  :
            if i>0 and all(state[y+a][b]=="." for y in range(1,i))and (state[a+i][b]=="."or(state[a+i][b].islower() !=state[a][b].islower())) :
              succ_Robin.append(temp1[:a+i]+[temp1[a+i][:b]+[R]+temp1[a+i][b+1:]]+temp1[a+1+i:])
            if i<0 and all(state[y+a][b]=="." for y in range(-1,i,-1)) and ((state[a+i][b].islower()!=state[a][b].islower())) :
              succ_Robin.append(temp1[:a+i]+[temp1[a+i][:b]+[R]+temp1[a+i][b+1:]]+temp1[a+1+i:])  
        if b+i>-1 and b+i<8: 
            if i>0 and all(state[a][y+b]=="." for y in range(1,i))and (state[a][b+i]=="."or(state[a][b+i].islower()!=state[a][b].islower())):
              succ_Robin.append(temp1[:a]+[temp1[a][:b+i]+[R]+temp1[a][b+i+1:]]+temp1[a+1:])
            if i<0 and all(state[a][y+b]=="." for y in range(-1,i,-1))and (state[a][b+i]=="."or(state[a][b+i].islower()!=state[a][b].islower())):  
              succ_Robin.append(temp1[:a]+[temp1[a][:b+i]+[R]+temp1[a][b+i+1:]]+temp1[a+1:])  
    return succ_Robin

#Move BlueJay function gives all possible moves for BlueJay at coordinate (a,b) and also takes into account who is playing
# black player or white player
def move_BlueJay(state,a,b,player):
    if player == "w":
        B = "B"
    else:
        B ="b"
    succ_BlueJay = []
    for i in [x for x in xrange(-7,8) if x != 0]:
        temp1 = state[:a]+[state[a][:b]+["."]+state[a][b+1:]]+state[a+1:]
        if a+i<8 and a+i>-1 and b+i<8 and b+i>-1 :
            if i>0 and all(state[a+x][b+x]=="." for x in range(1,i) )and (state[a+i][b+i]=="."or(state[a+i][b+i].islower() !=state[a][b].islower())) :
              succ_BlueJay.append(temp1[:a+i]+[temp1[a+i][:b+i]+[B]+temp1[a+i][b+i+1:]]+temp1[a+1+i:])
            if i<0 and all(state[a+x][b+x]=="." for x in range(-1,i,-1)) and (state[a+i][b+i]=="."or(state[a+i][b+i].islower()!=state[a][b].islower())) :
              succ_BlueJay.append(temp1[:a+i]+[temp1[a+i][:b+i]+[B]+temp1[a+i][b+i+1:]]+temp1[a+1+i:])  
        if a+i<8 and a+i>-1 and b-i<8 and b-i>-1 :      
            if i>0 and all(state[a+x][b-x]=="." for x in range(1,i) )and (state[a+i][b-i]=="."or(state[a+i][b-i].islower() !=state[a][b].islower())) :
              succ_BlueJay.append(temp1[:a+i]+[temp1[a+i][:b-i]+[B]+temp1[a+i][b-i+1:]]+temp1[a+1+i:])      
            if i<0  and all(state[a+x][b-x]=="." for x in range(-1,i,-1)) and (state[a+i][b-i]=="."or(state[a+i][b-i].islower()!=state[a][b].islower())) :  
              succ_BlueJay.append(temp1[:a+i]+[temp1[a+i][:b-i]+[B]+temp1[a+i][b-i+1:]]+temp1[a+1+i:])  
    return succ_BlueJay

#Move Quetzal function gives all possible moves for Quetzal at coordinate (a,b) and also takes into account who is playing
# black player or white player
def move_Quetzal(state,a,b,player):
    if player == "w":
        Q = "Q"
    else:
        Q ="q"
    succ_Quetzal = []
    for i in [x for x in xrange(-7,8) if x != 0]:
        temp1 = state[:a]+[state[a][:b]+["."]+state[a][b+1:]]+state[a+1:]
        if a+i>-1 and a+i <8  :
            if i>0 and all(state[y+a][b]=="." for y in range(1,i))and (state[a+i][b]=="."or(state[a+i][b].islower() !=state[a][b].islower())) :
              succ_Quetzal.append(temp1[:a+i]+[temp1[a+i][:b]+[Q]+temp1[a+i][b+1:]]+temp1[a+1+i:])
            if i<0 and all(state[y+a][b]=="." for y in range(-1,i,-1)) and ((state[a+i][b].islower()!=state[a][b].islower())) :
              succ_Quetzal.append(temp1[:a+i]+[temp1[a+i][:b]+[Q]+temp1[a+i][b+1:]]+temp1[a+1+i:])  
        if b+i>-1 and b+i<8: 
            if i>0 and all(state[a][y+b]=="." for y in range(1,i))and (state[a][b+i]=="."or(state[a][b+i].islower()!=state[a][b].islower())):
              succ_Quetzal.append(temp1[:a]+[temp1[a][:b+i]+[Q]+temp1[a][b+i+1:]]+temp1[a+1:])
            if i<0 and all(state[a][y+b]=="." for y in range(-1,i,-1))and (state[a][b+i]=="."or(state[a][b+i].islower()!=state[a][b].islower())):  
              succ_Quetzal.append(temp1[:a]+[temp1[a][:b+i]+[Q]+temp1[a][b+i+1:]]+temp1[a+1:])  
        
        if a+i<8 and a+i>-1 and b+i<8 and b+i>-1 :
            if i>0 and all(state[a+x][b+x]=="." for x in range(1,i) )and (state[a+i][b+i]=="."or(state[a+i][b+i].islower() !=state[a][b].islower())) :
              succ_Quetzal.append(temp1[:a+i]+[temp1[a+i][:b+i]+[Q]+temp1[a+i][b+i+1:]]+temp1[a+1+i:])
            if i<0 and all(state[a+x][b+x]=="." for x in range(-1,i,-1)) and (state[a+i][b+i]=="."or(state[a+i][b+i].islower()!=state[a][b].islower())) :
              succ_Quetzal.append(temp1[:a+i]+[temp1[a+i][:b+i]+[Q]+temp1[a+i][b+i+1:]]+temp1[a+1+i:])  
        if a+i<8 and a+i>-1 and b-i<8 and b-i>-1 :      
            if i>0 and all(state[a+x][b-x]=="." for x in range(1,i) )and (state[a+i][b-i]=="."or(state[a+i][b-i].islower() !=state[a][b].islower())) :
              succ_Quetzal.append(temp1[:a+i]+[temp1[a+i][:b-i]+[Q]+temp1[a+i][b-i+1:]]+temp1[a+1+i:])      
            if i<0  and all(state[a+x][b-x]=="." for x in range(-1,i,-1)) and (state[a+i][b-i]=="."or(state[a+i][b-i].islower()!=state[a][b].islower())) :  
              succ_Quetzal.append(temp1[:a+i]+[temp1[a+i][:b-i]+[Q]+temp1[a+i][b-i+1:]]+temp1[a+1+i:])                  
    return succ_Quetzal

#Move Nighthawk function gives all possible moves for Nighthawk at coordinate (a,b) and also takes into account who is playing
# black player or white player
def move_Nighthawk(state,a,b,player):
    if player == "w":
        N = "N"
    else:
        N ="n"
    succ_Nighthawk = []
    for i in [x for x in xrange(-1,2) if x != 0]:
        temp1 = state[:a]+[state[a][:b]+["."]+state[a][b+1:]]+state[a+1:]
        if i<0 and a+2*i<8 and a+2*i>-1 and b+i<8 and b+i>-1 and(state[a+2*i][b+i]=="." or(state[a+2*i][b+i].islower() !=state[a][b].islower())):
            succ_Nighthawk.append(temp1[:a+2*i]+[temp1[a+2*i][:b+i]+[N]+temp1[a+2*i][b+i+1:]]+temp1[a+1+2*i:])
        if i>0 and a+2*i<8 and a+2*i>-1 and b+i<8 and b+i>-1 and(state[a+2*i][b+i]=="."or(state[a+2*i][b+i].islower() !=state[a][b].islower())):
            succ_Nighthawk.append(temp1[:a+2*i]+[temp1[a+2*i][:b+i]+[N]+temp1[a+2*i][b+i+1:]]+temp1[a+1+2*i:])
        if i<0 and a+2*i<8 and a+2*i>-1 and b-i<8 and b-i>-1 and(state[a+2*i][b-i]=="." or(state[a+2*i][b-i].islower() !=state[a][b].islower())):
            succ_Nighthawk.append(temp1[:a+2*i]+[temp1[a+2*i][:b-i]+[N]+temp1[a+2*i][b-i+1:]]+temp1[a+1+2*i:])
        if i>0 and a+2*i<8 and a+2*i>-1 and b-i<8 and b-i>-1 and(state[a+2*i][b-i]=="."or(state[a+2*i][b-i].islower() !=state[a][b].islower())):
            succ_Nighthawk.append(temp1[:a+2*i]+[temp1[a+2*i][:b-i]+[N]+temp1[a+2*i][b-i+1:]]+temp1[a+1+2*i:])    
        if i<0 and a+i<8 and a+i>-1 and b+2*i<8 and b+2*i>-1 and(state[a+i][b+2*i]=="." or(state[a+i][b+2*i].islower() !=state[a][b].islower())):
            succ_Nighthawk.append(temp1[:a+i]+[temp1[a+i][:b+2*i]+[N]+temp1[a+i][b+2*i+1:]]+temp1[a+1+i:])
        if i>0 and a+i<8 and a+i>-1 and b+2*i<8 and b+2*i>-1 and(state[a+i][b+2*i]=="."or(state[a+i][b+2*i].islower() !=state[a][b].islower())):
            succ_Nighthawk.append(temp1[:a+2*i]+[temp1[a+i][:b+2*i]+[N]+temp1[a+i][b+2*i+1:]]+temp1[a+1+i:])
        if i<0 and a+i<8 and a+i>-1 and b-2*i<8 and b-2*i>-1 and(state[a+i][b-2*i]=="." or(state[a+i][b-2*i].islower() !=state[a][b].islower())):
            succ_Nighthawk.append(temp1[:a+i]+[temp1[a+i][:b-2*i]+[N]+temp1[a+i][b-2*i+1:]]+temp1[a+1+i:])
        if i>0 and a+i<8 and a+i>-1 and b-2*i<8 and b-2*i>-1 and(state[a+i][b-2*i]=="."or(state[a+i][b-2*i].islower() !=state[a][b].islower())):
            succ_Nighthawk.append(temp1[:a+i]+[temp1[a+i][:b-2*i]+[N]+temp1[a+i][b-2*i+1:]]+temp1[a+1+i:])        
    return succ_Nighthawk      

#Move Parakeet function gives all possible moves for Parakeet at coordinate (a,b) and also takes into account who is playing
# black player or white player
def move_Parakeet(state,a,b,player):
        if player == "w":
          P = "P"
        else:
          P ="p"
        succ_Parakeet = []
        succ2 = []
        temp1 = state[:a]+[state[a][:b]+["."]+state[a][b+1:]]+state[a+1:]
        if (not(state[a][b].islower()) and a ==7) or ((state[a][b].islower()) and a==0):
                succ2 = move_Quetzal(state,a,b,player)
                return succ2
        if (state[a][b].islower() ) :
            if a-1>-1 and a-1<8 and state[a-1][b]== ".":
                succ_Parakeet.append(temp1[:a-1]+[temp1[a-1][:b]+[P]+temp1[a-1][b+1:]]+temp1[a:])
            if a-1>-1 and a-1<8 and a-2>-1 and a-2<8 and state[a-1][b]=="." and state[a-2][b]=="."  and a ==6:
                succ_Parakeet.append(temp1[:a-2]+[temp1[a-2][:b]+[P]+temp1[a-2][b+1:]]+temp1[a-1:])
        if (not(state[a][b].islower()) ) : 
            if a+1>-1 and a+1<8 and state[a+1][b]== ".":
                succ_Parakeet.append(temp1[:a+1]+[temp1[a+1][:b]+[P]+temp1[a+1][b+1:]]+temp1[a+2:])
            if a+1>-1 and a+1<8 and a+2>-1 and a+2<8 and state[a+1][b]=="." and state[a+2][b]=="." and a==1:
                succ_Parakeet.append(temp1[:a+2]+[temp1[a+2][:b]+[P]+temp1[a+2][b+1:]]+temp1[a+3:])        
        if a-1>-1 and b+1>-1 and a-1<8 and b+1<8 and (state[a][b].islower()) and not(state[a-1][b+1].islower()) and (state[a-1][b+1])!="." and (state[a][b])!=".":
                succ_Parakeet.append(temp1[:a-1]+[temp1[a-1][:b+1]+[P]+temp1[a-1][b+2:]]+temp1[a:])
        if a-1>-1 and b-1>-1 and a-1<8 and b-1<8 and(state[a][b].islower()) and not(state[a-1][b-1].islower()) and (state[a-1][b-1])!="."and (state[a][b])!=".": 
                succ_Parakeet.append(temp1[:a-1]+[temp1[a-1][:b-1]+[P]+temp1[a-1][b:]]+temp1[a:])  
        if a+1>-1 and b+1>-1 and a+1<8 and b+1<8 and not(state[a][b].islower()) and (state[a+1][b+1].islower()) and (state[a+1][b+1])!="." and (state[a][b])!=".":
                succ_Parakeet.append(temp1[:a+1]+[temp1[a+1][:b+1]+[P]+temp1[a+1][b+2:]]+temp1[a+2:])
        if a+1>-1 and b-1>-1 and a+1<8 and b-1<8 and not(state[a][b].islower()) and (state[a+1][b-1].islower()) and (state[a+1][b-1])!="." and (state[a][b])!=".":
                succ_Parakeet.append(temp1[:a+1]+[temp1[a+1][:b-1]+[P]+temp1[a+1][b:]]+temp1[a+2:])          
        return succ_Parakeet 
    
#Move Kingfisher function gives all possible moves for Kingfisher at coordinate (a,b) and also takes into account who is playing
# black player or white player
def move_Kingfisher(state,a,b,player):
    if player == "w":
        K = "K"
    else:
        K ="k"
    succ_Kingfisher=[]
    temp1 = state[:a]+[state[a][:b]+["."]+state[a][b+1:]]+state[a+1:]
    if a-1>-1 and a-1<8 and b-1>-1 and b-1<8 and (state[a-1][b-1]== "." or (state[a-1][b-1]!= "." and state[a-1][b-1].islower()!= state[a][b].islower())):
        succ_Kingfisher.append(temp1[:a-1]+[temp1[a-1][:b-1]+[K]+temp1[a-1][b:]]+temp1[a:])
    if a+1>-1 and a+1<8 and b+1>-1 and b+1<8 and (state[a+1][b+1]== "." or (state[a+1][b+1]!= "." and state[a+1][b+1].islower()!= state[a][b].islower())):
        succ_Kingfisher.append(temp1[:a+1]+[temp1[a+1][:b+1]+[K]+temp1[a+1][b+2:]]+temp1[a+2:])
    if a+1>-1 and a+1<8 and b-1>-1 and b-1<8 and (state[a+1][b-1]== "." or (state[a+1][b-1]!= "." and state[a+1][b-1].islower()!= state[a][b].islower())):
        succ_Kingfisher.append(temp1[:a+1]+[temp1[a+1][:b-1]+[K]+temp1[a+1][b:]]+temp1[a+2:])    
    if a-1>-1 and a-1<8 and b+1>-1 and b+1<8 and (state[a-1][b+1]== "." or (state[a-1][b+1]!= "." and state[a-1][b+1].islower()!= state[a][b].islower())):
        succ_Kingfisher.append(temp1[:a-1]+[temp1[a-1][:b+1]+[K]+temp1[a-1][b+2:]]+temp1[a:])
    if a>-1 and a<8 and b+1>-1 and b+1<8 and (state[a][b+1]== "." or (state[a][b+1]!= "." and state[a][b+1].islower()!= state[a][b].islower())):
        succ_Kingfisher.append(temp1[:a]+[temp1[a][:b+1]+[K]+temp1[a][b+2:]]+temp1[a+1:])
    if a>-1 and a<8 and b-1>-1 and b-1<8 and (state[a][b-1]== "." or (state[a][b-1]!= "." and state[a][b-1].islower()!= state[a][b].islower())):
        succ_Kingfisher.append(temp1[:a]+[temp1[a][:b-1]+[K]+temp1[a][b:]]+temp1[a+1:])                
    if a-1>-1 and a-1<8 and b>-1 and b<8 and (state[a-1][b]== "." or (state[a-1][b]!= "." and state[a-1][b].islower()!= state[a][b].islower())):
        succ_Kingfisher.append(temp1[:a-1]+[temp1[a-1][:b]+[K]+temp1[a-1][b+1:]]+temp1[a:])                    
    if a+1>-1 and a+1<8 and b>-1 and b<8 and (state[a+1][b]== "." or (state[a+1][b]!= "." and state[a+1][b].islower()!= state[a][b].islower())):
        succ_Kingfisher.append(temp1[:a+1]+[temp1[a+1][:b]+[K]+temp1[a+1][b+1:]]+temp1[a+2:])                        
    return succ_Kingfisher

def find_position(state,t):
    position =[]
    for x in range(0,8):
        for y in range(0,8):
            if state[x][y] == t:
               position.append([x,y])
               #position.append(y)
    if len(position)>0:           
       return position
    else:
       return [[-1,-1],[-1,-1]]
   
def successors(state,player):
    if player =="w":
       R = "R"
       B = "B"
       Q = "Q"
       N = "N"
       P = "P"
       K = "K"
    else:
       R = "r"
       B = "b"
       Q = 'q'
       N = 'n'
       P = "p"
       K = "k"
    successor =[]
    
    for i in range(0,len(find_position(state,P))):
           successor = successor + ((move_Parakeet(state,find_position(state,P)[i][0],find_position(state,P)[i][1],player)))
    for i in range(0,len(find_position(state,B))):    
           successor = successor +((move_BlueJay(state,find_position(state,B)[i][0],find_position(state,B)[i][1],player)))
    for i in range(0,len(find_position(state,N))):    
           successor = successor +((move_Nighthawk(state,find_position(state,N)[i][0],find_position(state,N)[i][1],player)))
    for i in range(0,len(find_position(state,K))):    
           successor = successor +((move_Kingfisher(state,find_position(state,K)[i][0],find_position(state,K)[i][1],player)))
    for i in range(0,len(find_position(state,Q))):    
           successor = successor +((move_Quetzal(state,find_position(state,Q)[i][0],find_position(state,Q)[i][1],player)))
    for i in range(0,len(find_position(state,R))):    
           successor = successor +((move_Robin(state,find_position(state,R)[i][0],find_position(state,R)[i][1],player)))       
    return successor    

# The evaluation function written below takes into consideration two factors . One is Material score and other is mobility
#score. I got this idea from the following website  https://chessprogramming.wikispaces.com/Evaluation
# Material score is the weighted difference of number of pieces between white and black pieces. 
# Mobility score is the difference in the number of possibe moves for white and black pieces 

def evaluation(state,player):
    count_P=0
    count_p =0
    count_Q = 0
    count_q =0
    count_N =0
    count_n=0
    count_B=0
    count_b=0
    count_K = 0
    count_k=0
    count_R =0
    count_r=0
    for x in state:
        for y in x:
            if y == "P":
                count_P = count_P +1
            if y =="p":
                count_p = count_p+1
            if y == "Q" :
                count_Q = count_Q+1
            if y == "q":
                count_q =count_q+1
            if y == "K":
                count_K = count_K +1
            if y == "k":
                count_k = count_k +1
            if y == "R":
                count_R = count_R +1
            if y == "r":
                count_r =count_r +1
            if y =="B":
                count_B = count_B +1
            if y =="b":
                count_b = count_b+1
            if y =="N" :
                count_N =count_N+1
            if y == "n":
                count_n = count_n +1
                
    val = 250*(count_K-count_k)+17*(count_Q-count_q)+11*(count_B-count_b)+10*(count_R-count_r)+5*(count_N-count_n)+1*(count_P-count_p)+len(successors(state,"w"))-len(successors(state,"b"))
    return val*1 if player == "w" else val*-1         


# I have written three functions, Min-Max, Min and Max function. Min-Max will choose the maximum value state of board from
# successors of the initial board . For that the first call will go to Min function for the successors of each successor
# of the initial state of board. And that Min function will call Max function and so on until the depth reaches 7. once
# the depth reaches 7 it will call the evaluation function which will stop this loop of calls between Min and Max func
# I have implemented alpha beta pruning in the Min and Max functions 
depth = 1
def Min(state,alpha,beta):
    global depth
    depth = depth + 1
    if depth < 8:
       mini = 100000000000000
       for z in successors(state,plyr):
           score = Max(z,alpha,beta)
           if score < mini:
               mini = score
           if score<= alpha:
               return mini
           if score < beta:
               beta = score
    if depth >=8 :
       mini = 100000000000000
       for z in successors(state,plyr):
           score = evaluation(z,plyr)
           if score < mini:
               mini = score
           if score<= alpha:
               return mini
           if score < beta:
               beta = score  
    return mini    

def Max(state,alpha,beta):
    maxi = -100000000000000
    global depth
    depth = depth +1
    if depth >=8:
       for z in successors(state,plyr):
           score = evaluation(z,plyr)
           if score > maxi:
               maxi = score
           if score >= beta:
               return maxi
           
           if score > alpha :
               alpha = score
    if depth <8:
       for z in successors(state,plyr):
           score = Min(z,alpha,beta)
           if score > maxi:
               maxi = score
           if score >= beta:
               return maxi
           if score > alpha :
               alpha = score            
    return maxi

def Min_Max(state,alpha,beta):   
    final_state = []
    maxi = -100000
    for z in successors(state,plyr ):
       score  = Min(z,alpha,beta)
       if score >  maxi:        
        maxi = score
        final_state = z
    return printing_board_single_line(final_state)           

print "YO !! \n"
print Min_Max(state,-100000,100000)



# Online Python - IDE, Editor, Compiler, Interpreter
#```py
import random

    # 2 bugs
    # ---fixed----1 bug is when there are 2 aces it adds them up to 11+11 =22 instead of having 11+1 = 12 
    # ---fixed----2nd bug when there are 4 cards, the third card that is dealt is duplicated 
suits = ["♠","♣","♡","♢"]
numbers = ["1","2","3","4","5","6","7","8","9","10","11","12","13",]

winCount = 0
lossCount = 0 
drawCount = 0
    #Builds the deck of 52 cards
def reshuffle():
    for suit in suits:
        for number in numbers:
            deck.append(suit+number)


def checkforAce(player,playerTotal):
    for i in range(len(player)):
        if (player[i] == '♠1'or player[i] == '♣1' or player[i] == '♡1' or player[i] == '♢1'):
            return True
        else:
            continue
    return False
         
for i in range(10):  
    #for version of the game where there is only 1 deck
    #7 1 6 -> 7 10
    deck = []
    reshuffle()
    #"♠2","♣1","3♡","4♢"
    player = []
    house = []
    #deals 2 cards to player and house randomly
    def initialDeal(param) :
        while len(param) < 2:
            card = random.choice(deck)
            # deck.remove(card)
            param.append(card)
        return param
    player = initialDeal(player)
    house = initialDeal(house)
    #deal another card if total is less than 17
    def dealAnotherCard(param):
        card = random.choice(deck)
        # deck.remove(card)
        param.append(card)
        return param
    def convertToCorrectValue(player,hold,a):
        for i in range(0,len(hold)):
            if(hold[i] == 1 and ((a+11) <= 21)):
                hold[i] = 11
            # elif(hold[i] > 10 and player[i] == '♠1'or player[i] == '♣1' or player[i] == '♡1' or player[i] == '♢1'):
            #     continue
            elif(hold[i] == 11 and player[i] == '♠11'or player[i] == '♣11' or player[i] == '♡11' or player[i] == '♢11'):
                hold[i] = 10
            elif(hold[i] > 11):
                hold[i] = 10
            
        if(hold[0] ==11 and hold[1] == 11):
            hold[0] = 11
            hold[1] = 1
        
        return hold
        
    def total(playerValue):
        temp = 0
        for i in range(0, len(playerValue)):
            temp += playerValue[i]
        return temp
    def appendingNewCard(playerTotal):
        playerTotal.append(int((player[-1][1:])))
    def appendingNewCardH(houseTotal):
        houseTotal.append(int((house[-1][1:])))
    
    #fix when both player and house get more than 21 total for ex: hTotal:22 pTotal: 22, it should not be a draw, house should win
    def winner(pTotal,hTotal):
        global lossCount,drawCount,winCount
        if(pTotal > hTotal and pTotal <=21):
            winCount = winCount+1
            print("Player wins")
        elif(pTotal > hTotal and pTotal >21):
            print("House wins")
            lossCount = lossCount+1
        elif(hTotal > pTotal and hTotal <=21):
            lossCount = lossCount+1
            print("House wins")
        #ex Player: 18 House: 23
        elif(hTotal > pTotal and hTotal >21):
            winCount = winCount+1
            print("Player wins")
        elif(pTotal == hTotal and pTotal <= 21):
            drawCount= drawCount+1
            print("Its a draw")
        else:
            lossCount = lossCount+1
            print("House wins")
        return winCount,lossCount,drawCount    
        # if(pTotal  == hTotal):
        #     if(pTotal >21 and hTotal > 21):
        #         print("house wins")
        #         lossCount = lossCount+1
        #     print("Its a draw")
        #     drawCount = drawCount+1
        # elif(pTotal < hTotal and hTotal <= 21):
        #     print("House wins")
        #     lossCount = lossCount+1
        # elif(hTotal <  pTotal and pTotal <=21):
        #     print("Player wins")
        #     winCount = winCount+1
        # elif(pTotal > 21 and hTotal >21):
        #     print("house wins")
        #     lossCount = lossCount+1
        # return lossCount,winCount,drawCount
    # print("Cards of player:",player, "----  Cards of house:",house)
    
    #checks how many elements/cards are in player list and takes the first 2 strings
    #and puts them in playerTotal/houseTotal list
    playerTotal = []  
    for i in range(0, len(player) ):
        temp = int(player[i][1:])
        playerTotal.append(temp)
    houseTotal = []
    for i in range(0, len(house)):
        temp = int(house[i][1:])
        houseTotal.append(temp)
        
    hTotal=0
    pTotal=0
    playerTotal = convertToCorrectValue(player,playerTotal,pTotal);
    houseTotal = convertToCorrectValue(house,houseTotal,hTotal);
    
    pTotal = total(playerTotal)
    hTotal = total(houseTotal)
    def checkForEleven(playerTotal,pTotal):
        if(pTotal > 21):
            for i in range(len(playerTotal)):
                if(playerTotal[i] == 11):
                    playerTotal[i] = 1
               
    #####Policy 5 while(pTotal <15)          
    #####Policy 4 call the dealanothercard, appendingNewCard,convertToCorrectValue,pTotal once
    # dealAnotherCard(player)
    # appendingNewCard(playerTotal)
    # convertToCorrectValue(player,playerTotal,pTotal)
    # pTotal = total(playerTotal)
    #####Policy 3 get rid of the while loop
    #####Policy 2 for player
    # if(checkforAce(player,playerTotal)):      
    #     while(pTotal < 21 and checkforAce(player,playerTotal)):
    #         print("going for 21")
    #         dealAnotherCard(player)
    #         appendingNewCard(playerTotal)
    #         convertToCorrectValue(player,playerTotal,pTotal)
    #         pTotal = total(playerTotal)
    #         checkForEleven(playerTotal,pTotal)
    #         pTotal = total(playerTotal)
    # else:
    #     while(pTotal < 17):
    #         print("going for 17")
    #         dealAnotherCard(player)
    #         appendingNewCard(playerTotal)
    #         convertToCorrectValue(player,playerTotal,pTotal)
    #         pTotal = total(playerTotal)
    #         checkForEleven(playerTotal,pTotal)
    #         pTotal = total(playerTotal)
   ####Policy 1 for player
    while(pTotal < 17):
        dealAnotherCard(player)
        appendingNewCard(playerTotal)
        convertToCorrectValue(player,playerTotal,pTotal)
        pTotal = total(playerTotal)
        checkForEleven(playerTotal,pTotal)
        pTotal = total(playerTotal)
        
    #dealer takes the cards until the total is 17 or more(soft or hard)
    while(hTotal < 17):
        dealAnotherCard(house)
        appendingNewCardH(houseTotal)
        convertToCorrectValue(house,houseTotal,hTotal)
        hTotal = total(houseTotal)
        checkForEleven(houseTotal,hTotal)
        hTotal = total(houseTotal)
    
    
    print( "Player variable: ",player, ' ' , house)
    # print(checkforAce(player)) 
    print("playerTotal Variables: ",playerTotal, "   ", houseTotal)
    print("Player total is: ", pTotal, " House total is: ", hTotal)
    winner(pTotal,hTotal)
    # winner(pTotal)```
print(len(deck))
print("Losses: ",lossCount)
print("Draws: ",drawCount)
print("Wins: ",winCount)
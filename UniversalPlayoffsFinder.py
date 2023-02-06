
import math

#input win count and differential in all 16 player scores
player1 = []
player1Score = (5,18)
player1Name = "a12qsd"

player2 = []
player2Score = (5,9)
player2Name = "Palkia62"

player3 = []
player3Score = (4,6)
player3Name = "Hopeless"

player4 = []
player4Score = (4,3)
player4Name = "JimmyG"

player5 = []
player5Score = (4,2)
player5Name = "H.Y.D.R.A."

player6 = []
player6Score = (4,2)
player6Name = "Kaif"

player7 = []
player7Score = (4,0)
player7Name = "Craft"

player8 = []
player8Score = (4,-1)
player8Name = "Brotherquang"

player9 = []
player9Score = (3,-1)
player9Name = "Vengabenga"

player10 = []
player10Score = (3,-2)
player10Name = "Jjgalz"

player11 = []
player11Score = (3,-2)
player11Name = "Turk"

player12 = []
player12Score = (3,-3)
player12Name = "DaTa"

player13 = []
player13Score = (3,-5)
player13Name = "Husemannen"

player14 = []
player14Score = (3,-6)
player14Name = "Brandon"

player15 = []
player15Score = (3,-7)
player15Name = "cmr"

player16 = []
player16Score = (1,-13)
player16Name = "Shade"

#each playerX variable is a list of possible win/diffs after the week 9 game
players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12, player13, player14, player15, player16]

#each playerXScore variable is the player's score after week 8
playerScores = [player1Score, player2Score, player3Score, player4Score, player5Score, player6Score, player7Score, player8Score, player9Score, player10Score, player11Score, player12Score, player13Score, player14Score, player15Score, player16Score]

#just a list of player names
playerNames = [player1Name, player2Name, player3Name, player4Name, player5Name, player6Name, player7Name, player8Name, player9Name, player10Name, player11Name, player12Name, player13Name, player14Name, player15Name, player16Name]

#make sure that all the correct players are in the correct games
#try to put the games in order to have the highest ranked players ealier and lower ranked players later to pre-sort so less time is spent on sorting every time in the core loop
game1players = (player13, player3)
game2players = (player4, player5)
game3players = (player7, player10)
game4players = (player12, player6)
game5players = (player11, player9)
game6players = (player16, player8)
game7players = (player1, player15)
game8players = (player2, player14)

#make sure that all the correct player numbers are in the correct games
#since in this case the numbers will be used as an index make sure they are (player number - 1) since the player arrays are 0 indexed
game1playerNumbers = (12, 2)
game2playerNumbers = (3, 4)
game3playerNumbers = (6, 9)
game4playerNumbers = (11, 5)
game5playerNumbers = (10, 8)
game6playerNumbers = (15, 7)
game7playerNumbers = (0, 14)
game8playerNumbers = (1, 13)

games = [game1playerNumbers, game2playerNumbers, game3playerNumbers, game4playerNumbers, game5playerNumbers, game6playerNumbers, game7playerNumbers, game8playerNumbers]

count = 0

#populates player arrays with all possible win/diff after a game is played. Does not account for a 0-0 tie in a game because those are so unlikely
def findOutcomes():
    print("Populating potential win/diff for each player...")

    def findSingleOutcome(player, playerScore):
        diffWin = 6
        diffLoss = -1
        for x in range(0, 6):
            player.append((playerScore[0] + 1, playerScore[1] + diffWin))
            diffWin = diffWin - 1
        for x in range(0, 6):
            player.append((playerScore[0], playerScore[1] + diffLoss))
            diffLoss = diffLoss - 1

    for x in range(0, 16):
        findSingleOutcome(players[x], playerScores[x])
        print(players[x])
        
    for x in range(0,8):
        print(playerNames[games[x][0]], playerScores[games[x][0]], " vs ", playerNames[games[x][1]], playerScores[games[x][1]])
        

def main():
    findOutcomes()
    week9()


def Game1(temp, x):
    temp.append((game1playerNumbers[0], game1players[0][x]))
    temp.append((game1playerNumbers[1], game1players[1][(x * -1) - 1]))


def Game2(temp, y): 
    temp.append((game2playerNumbers[0], game2players[0][y]))
    temp.append((game2playerNumbers[1], game2players[1][(y * -1) - 1]))

def Game3(temp, z):
    temp.append((game3playerNumbers[0], game3players[0][z]))
    temp.append((game3playerNumbers[1], game3players[1][(z * -1) - 1]))

def Game4(temp, a):
    temp.append((game4playerNumbers[0], game4players[0][a]))
    temp.append((game4playerNumbers[1], game4players[1][(a * -1) - 1]))

def Game5(temp, b):
    temp.append((game5playerNumbers[0], game5players[0][b]))
    temp.append((game5playerNumbers[1], game5players[1][(b * -1) - 1]))

def Game6(temp, c):
    temp.append((game6playerNumbers[0], game6players[0][c]))
    temp.append((game6playerNumbers[1], game6players[1][(c * -1) - 1]))

def Game7(temp, d):
    temp.append((game7playerNumbers[0], game7players[0][d]))
    temp.append((game7playerNumbers[1], game7players[1][(d * -1) - 1]))

def Game8(temp, e):
    temp.append((game8playerNumbers[0], game8players[0][e]))
    temp.append((game8playerNumbers[1], game8players[1][(e * -1) - 1]))


def week9():

    #the index of a 'timesPlacedX' array or timesMadePlayoffs is the player number - 1
    #so in timesPlaced1, index 0 is how many times player1 made first place in all permutations
    #in timesPlaced4, index 7 is how many times player6 made 4th place in all permutations
    #in timesMadePlayoffs, index 10 is how many times player9 made playoffs 

    timesPlaced1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced14 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    timesPlaced16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("Doing all matchup outcome permutations...")
    #generate all week9 scenarios and put them in all
    x = 0
    y = 0
    z = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    count = 0
    while x < 12:
        temp = []
        Game1(temp, x)
        Game2(temp, y)
        Game3(temp, z)
        Game4(temp, a)
        Game5(temp, b)
        Game6(temp, c)
        Game7(temp, d)
        Game8(temp, e)
        temp.sort(key=lambda element: (element[1][0], element[1][1]), reverse=True)
        count += 1
        #temp is now one possible set of outcomes for week 9
        #it is a sorted list of tuples that look like (player number - 1, (wins, diff))

        #index into temp at a specific rank and find the player number and use that to index into the timesPlaced array 
        timesPlaced1[temp[0][0]] += 1
        timesPlaced2[temp[1][0]] += 1
        timesPlaced3[temp[2][0]] += 1
        timesPlaced4[temp[3][0]] += 1
        timesPlaced5[temp[4][0]] += 1
        timesPlaced6[temp[5][0]] += 1
        timesPlaced7[temp[6][0]] += 1
        timesPlaced8[temp[7][0]] += 1
        timesPlaced9[temp[8][0]] += 1
        timesPlaced10[temp[9][0]] += 1
        timesPlaced11[temp[10][0]] += 1
        timesPlaced12[temp[11][0]] += 1
        timesPlaced13[temp[12][0]] += 1
        timesPlaced14[temp[13][0]] += 1
        timesPlaced15[temp[14][0]] += 1
        timesPlaced16[temp[15][0]] += 1

        e += 1
        if e == 12:
            e = 0
            d += 1
            if d == 12:
                d = 0
                c += 1
                if c == 12:
                    c = 0
                    b += 1
                    if b == 12:
                        b = 0
                        a += 1
                        if a == 12:
                            a = 0
                            z += 1
                            if z == 12:
                                z = 0
                                y += 1
                                print(count)
                                if y == 12:
                                    y = 0
                                x += 1
            #just a check to see if it is running and not frozen
            # print("Game 1 new scenario")

    #Old memory intensive recursive method
    # for x in range(0,12):
    #     temp = []
    #     Game1(temp[:], x)

    # count = len(all)
    
    


    
    print("Counting all placement outcomes...")

    
    allPlacementCounts = [
        timesPlaced1, 
        timesPlaced2, 
        timesPlaced3, 
        timesPlaced4, 
        timesPlaced5, 
        timesPlaced6, 
        timesPlaced7, 
        timesPlaced8, 
        timesPlaced9, 
        timesPlaced10, 
        timesPlaced11, 
        timesPlaced12, 
        timesPlaced13, 
        timesPlaced14, 
        timesPlaced15, 
        timesPlaced16
    ]

    timesMadePlayoffs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for x  in range(0,16):
        timesPlayerXMadePlayoffs = 0
        for y in range(0,8):
            timesPlayerXMadePlayoffs += allPlacementCounts[y][x]
        timesMadePlayoffs[x] = timesPlayerXMadePlayoffs


    player1Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player2Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player3Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player4Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player5Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player6Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player7Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player8Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player9Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player10Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player11Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player12Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player13Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player14Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player15Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player16Placements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    allPlayerPlacements = [
        player1Placements, 
        player2Placements, 
        player3Placements, 
        player4Placements, 
        player5Placements, 
        player6Placements, 
        player7Placements, 
        player8Placements,
        player9Placements, 
        player10Placements, 
        player11Placements, 
        player12Placements, 
        player13Placements, 
        player14Placements, 
        player15Placements, 
        player16Placements
    ]

    for player in range(0, 16):
        for place in range(0, 16):
            allPlayerPlacements[player][place] = allPlacementCounts[place][player]

    print("Playoff Chances")

    for player in range(0,16):
        print(playerNames[player], " playoff chances: ", timesMadePlayoffs[player]/count*100, "%")

    print()
    
    for player in range(0,16):
        print(playerNames[player], " placement chances")
        print(playerNames[player], " 1st place chances: ", allPlayerPlacements[player][0]/count*100, "%")
        print(playerNames[player], " 2nd place chances: ", allPlayerPlacements[player][1]/count*100, "%")
        print(playerNames[player], " 3rd place chances: ", allPlayerPlacements[player][2]/count*100, "%")
        for place in range(3, 16):
            print(playerNames[player], " {0:1d}th place chances: ".format(place + 1), allPlayerPlacements[player][place]/count*100, "%")
        print(playerNames[player], " chance to MISS playoffs: ", (100 - (timesMadePlayoffs[player]/count*100)), "%")
        print()


   

if __name__ == "__main__":
    main()
    
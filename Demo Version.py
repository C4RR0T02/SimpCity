# Ngui Jia Le Sherlena (S10227488A) P07 CSF02

#Simp City Code

#import modules
import random
import sys
import json

#Assigning values to variables
building_list = [' HSE',' FAC',' SHP',' HWY',' BCH']
buildinglistdup = building_list.copy()

buildable_locations = ["A1", "B1", "C1", "D1",
                       "A2", "B2", "C2", "D2",
                       "A3", "B3", "C3", "D3",
                       "A4", "B4", "C4", "D4"]

building_count = {' HSE': 8,
                  ' FAC': 8,
                  ' SHP': 8,
                  ' HWY': 8,
                  ' BCH': 8}

indexrow = {'A': 0,
            'B': 1,
            'C': 2,
            'D': 3}

indexcolumn = {'1': 0,
               '2': 1,
               '3': 2,
               '4': 3}

building_score = {' HSE': [],
                  ' FAC': [],
                  ' SHP': [],
                  ' HWY': [],
                  ' BCH': []}

empty = []

map = [['    ', '    ', '    ', '    '],
       ['    ', '    ', '    ', '    '],
       ['    ', '    ', '    ', '    '],
       ['    ', '    ', '    ', '    ']
       ]

turn = 1

highscorelist = []

currentplayertotal = 0


#Menu
def init_game(buildable_locations,turn,map):
    choice = '3'
    while choice != '0' or choice != '1' or choice != '2' or choice != '3':     # Checking if input from user is valid
        choice = str(input("\n\n"
                           "Welcome, mayor of Simp City!"
                           "\n____________________________"
                           "\n1. Start new game"
                           "\n2. Load saved game"
                           "\n3. Show high scores"
                           "\n"
                           "\n0. Exit"
                           "\nYour choice? "))
        if choice == '1':
            print('Starting new game')
            init_values()
            newgame(buildable_locations,turn,map,building_count,empty)
        elif choice == '2':
            print('Loading saved game ... \n')
            loadgame()
        elif choice == '3':
            printhighscore()
        elif choice == '0':
            print("Exiting game")
            sys.exit()
        else:
            print('Choice is invalid, Please choose options 0, 1 or 2')

#Printing of map
def grid(map):
    x = 1
    column = '  ' + '+-----' * len(map[0])
    print("\n     A     B     C     D")
    for row in map:
        print(column + '+')
        print(str(x), end=' ')
        for element in row:
            print('|' + str(element) + ' ', end='')
        print('|', end='\n')
        x += 1
    print(column + '+')

#building checker: Ensure that if there is not enough building of the type, users will not be able to choose that building
def buildingchecker():
    for building in buildinglistdup:
        if building_count[building] == 0:
            buildinglistdup.remove(building)

#Generating of buildings
def building_gen():
    buildingchecker()
    buildings1 = random.choice(buildinglistdup)
    buildings2 = random.choice(buildinglistdup)
    while buildings1 == buildings2:
        # ensure that users can choose between 2 types instead of 1 type of building
        buildings2 = random.choice(buildinglistdup)
    return buildings1,buildings2

#removing given buildings
def count_building(buildings1,buildings2):
    building_count[buildings1] -= 1
    building_count[buildings2] -= 1

def init_values():
    # reset values to default when starting new game
    building_list = [' HSE', ' FAC', ' SHP', ' HWY', ' BCH']
    buildinglistdup = building_list.copy()
    buildable_locations = ["A1", "B1", "C1", "D1",
                           "A2", "B2", "C2", "D2",
                           "A3", "B3", "C3", "D3",
                           "A4", "B4", "C4", "D4"]
    building_count = {' HSE': 8,
                      ' FAC': 8,
                      ' SHP': 8,
                      ' HWY': 8,
                      ' BCH': 8}
    indexrow = {'A': 0,
                'B': 1,
                'C': 2,
                'D': 3}
    indexcolumn = {'1': 0,
                   '2': 1,
                   '3': 2,
                   '4': 3}
    building_score = {' HSE': [],
                      ' FAC': [],
                      ' SHP': [],
                      ' HWY': [],
                      ' BCH': []}
    empty = []
    map = [['    ', '    ', '    ', '    '],
           ['    ', '    ', '    ', '    '],
           ['    ', '    ', '    ', '    '],
           ['    ', '    ', '    ', '    ']
           ]
    turn = 1
    highscorelist = []
    currentplayertotal = 0

#Start game
def newgame(buildable_locations,turn,map,building_count,empty):
    while turn < 17:
        step = 6
        while step != '0' or step != '1' or step != '2' or step != '3' or step != '4' or step != '5':   #checking user input
            buildings1, buildings2 = building_gen()     #calling the buildings generated
            print('Turn ', turn)
            grid(map)                                      #Printing the map
            step = str(input("\n1. Build a{:s}"
                             "\n2. Build a{:s}"
                             "\n3. See remaining buildings"
                             "\n4. See current score"
                             "\n"
                             "\n5. Save game"
                             "\n0. Exit to main menu"
                             "\nYour choice? ".format(buildings1, buildings2)))
            if step == '1':
                build(turn, buildings1, map, buildable_locations,empty)
                count_building(buildings1, buildings2)
                turn += 1
                if turn == 17:
                    break
                else:
                    continue
            elif step == '2':
                build(turn, buildings2, map, buildable_locations,empty)
                count_building(buildings1, buildings2)
                turn += 1
                if turn == 17:
                    break
                else:
                    continue
            elif step == '3':
                remaining_build(building_count)
            elif step == '4':
                score(building_score, map)
            elif step == '5':
                savegame(buildinglistdup, buildable_locations, building_count)
            elif step == '0':
                print("Exiting to main menu")
                init_game(buildable_locations, turn, map)
            else:
                print('Choice is invalid, Input number should be between 0 to 5')
    if turn == 17:
        endgame(map)

#Remaining building (For printing)
def remaining_build(building_count):
    print('{:s} \t\t {:s}'.format('Building', 'Remaining'))
    print('{:s} \t\t {:s}'.format('--------', '---------'))
    for key, value in building_count.items():
        print('{:s} \t\t\t {:d}'.format(key, value))
    input("Press Enter to continue")

#Build - Checling format of input to prepare for building
def build(turn, building, map, buildable_locations,empty):
    buildat = str(input("Build where? "))
    buildatupper = buildat.upper()
    if len(buildatupper) < 2 or len(buildatupper) > 2:          #ensure that only 2 characters are input
        print("Please enter a valid location")
    else:
        if buildatupper[0].isalpha() == True:                   #Checking order of user input
            if buildatupper[0] == 'A' or buildatupper[0] == 'B' or buildatupper[0] == 'C' or buildatupper[0] == 'D':
                check_build(turn, empty, building, buildatupper, buildable_locations, map)
            else:
                print("Please enter a valid location")
                turn -= 1                                       #Giving back turn since it is invalid input
                build(turn, building, map, buildable_locations) #Looping
        elif buildatupper[1].isalpha() == True:                 #Checking order of user input
            reversed_building = buildatupper[::-1]              #ensuring that the input is the way the script reads it
            if reversed_building[0] == 'A' or reversed_building[0] == 'B' or reversed_building[0] == 'C' or reversed_building[0] == 'D':
                check_build(turn, empty, building, reversed_building, buildable_locations, map)
            else:
                print("Please enter a valid location")
                turn -= 1
                build(turn, building, map, buildable_locations,empty)
        else:
            print("Please enter a valid location")
            turn -= 1
            build(turn, building, map, buildable_locations,empty)

#Check build validity and build buildings
def check_build(turn, empty, building, wheretobuild, buildable_locations,map):
    if turn == 1:
        a = indexrow[wheretobuild[0]]
        b = int(indexcolumn[wheretobuild[1]])
        buildable_locations.remove(wheretobuild)        #removing current spot to ensure no building over same building
        map[b][a] = building                            #Building
        if wheretobuild == "A1":                        #updating buildable locations
            empty.append("A2")
            empty.append("B1")
        elif wheretobuild == "A2":
            empty.append("A1")
            empty.append("A3")
            empty.append("B2")
        elif wheretobuild == "A3":
            empty.append("A2")
            empty.append("A4")
            empty.append("B3")
        elif wheretobuild == "A4":
            empty.append("A3")
            empty.append("B4")
        elif wheretobuild == "B1":
            empty.append("A1")
            empty.append("C1")
            empty.append("B2")
        elif wheretobuild == "B2":
            empty.append("A2")
            empty.append("C2")
            empty.append("B1")
            empty.append("B3")
        elif wheretobuild == "B3":
            empty.append("A3")
            empty.append("C3")
            empty.append("B2")
            empty.append("B4")
        elif wheretobuild == "B4":
            empty.append("B3")
            empty.append("A4")
            empty.append("C4")
        elif wheretobuild == "C1":
            empty.append("B1")
            empty.append("D1")
            empty.append("C2")
        elif wheretobuild == "C2":
            empty.append("B2")
            empty.append("D2")
            empty.append("C1")
            empty.append("C3")
        elif wheretobuild == "C3":
            empty.append("B3")
            empty.append("D3")
            empty.append("C2")
            empty.append("C4")
        elif wheretobuild == "C4":
            empty.append("C3")
            empty.append("B4")
            empty.append("D4")
        elif wheretobuild == "D1":
            empty.append("C1")
            empty.append("D2")
        elif wheretobuild == "D2":
            empty.append("D1")
            empty.append("D3")
            empty.append("C2")
        elif wheretobuild == "D3":
            empty.append("C3")
            empty.append("D2")
            empty.append("D4")
        elif wheretobuild == "D4":
            empty.append("C4")
            empty.append("D3")
        return empty
    else:
        a = indexrow[wheretobuild[0]]
        b = int(indexcolumn[wheretobuild[1]])
        if wheretobuild in empty and wheretobuild in buildable_locations:       #ensuring no illegal building
            buildable_locations.remove(wheretobuild)                            #removing current spot to ensure no building over same building
            map[b][a] = building                                                #building
            if wheretobuild == "A1":                                            #updating buildable locations
                empty.append("A2")
                empty.append("B1")
            elif wheretobuild == "A2":
                empty.append("A1")
                empty.append("A3")
                empty.append("B2")
            elif wheretobuild == "A3":
                empty.append("A2")
                empty.append("A4")
                empty.append("B3")
            elif wheretobuild == "A4":
                empty.append("A3")
                empty.append("B4")
            elif wheretobuild == "B1":
                empty.append("A1")
                empty.append("C1")
                empty.append("B2")
            elif wheretobuild == "B2":
                empty.append("A2")
                empty.append("C2")
                empty.append("B1")
                empty.append("B3")
            elif wheretobuild == "B3":
                empty.append("A3")
                empty.append("C3")
                empty.append("B2")
                empty.append("B4")
            elif wheretobuild == "B4":
                empty.append("B3")
                empty.append("A4")
                empty.append("C4")
            elif wheretobuild == "C1":
                empty.append("B1")
                empty.append("D1")
                empty.append("C2")
            elif wheretobuild == "C2":
                empty.append("B2")
                empty.append("D2")
                empty.append("C1")
                empty.append("C3")
            elif wheretobuild == "C3":
                empty.append("B3")
                empty.append("D3")
                empty.append("C2")
                empty.append("C4")
            elif wheretobuild == "C4":
                empty.append("C3")
                empty.append("B4")
                empty.append("D4")
            elif wheretobuild == "D1":
                empty.append("C1")
                empty.append("D2")
            elif wheretobuild == "D2":
                empty.append("D1")
                empty.append("D3")
                empty.append("C2")
            elif wheretobuild == "D3":
                empty.append("C3")
                empty.append("D2")
                empty.append("D4")
            elif wheretobuild == "D4":
                empty.append("C4")
                empty.append("D3")
            return empty
        else:
            print("This is an invalid build location")
            turn -= 1
            build(turn, building, map, buildable_locations, empty)

#score
def score(building_score, map):
    faccount = 0
    x = 0
    y = 0
    building_score = {' HSE': [],
                      ' FAC': [],
                      ' SHP': [],
                      ' HWY': [],
                      ' BCH': []}
    #scoring for BCH
    for row in map:
        appendscore = 0
        if row[0] == " BCH":
            appendscore += 3
        if row[3] == " BCH":
            appendscore += 3
        if row[1] == " BCH":
            appendscore += 1
        if row[2] == " BCH":
            appendscore += 1
        building_score[" BCH"].append(appendscore)
    #scoring for FAC
    for row in map:
        for eachbuilding in row:
            if eachbuilding == " FAC":
                faccount += 1
    if faccount > 0:
        if faccount <= 4:
            numoffaccount = faccount
            while numoffaccount != 0:
                building_score[" FAC"].append(faccount)
                numoffaccount -= 1
    elif faccount > 4:
        numoffaccount = faccount - 4
        building_score[" FAC"].append(4)
        while numoffaccount != 0:
            building_score[" FAC"].append(1)
            numoffaccount -= 1
    else:
        building_score[" FAC"].append(0)
    #scoring for HSE
    for row in map:
        for each in row:
            if each == " HSE":
                axislisthse = []
                if x == 0 and y == 0:
                    axislisthse.append(map[1][0])
                    axislisthse.append(map[0][1])
                elif x == 0 and y == 1:
                    axislisthse.append(map[0][0])
                    axislisthse.append(map[0][2])
                    axislisthse.append(map[1][1])
                elif x == 0 and y == 2:
                    axislisthse.append(map[0][1])
                    axislisthse.append(map[0][3])
                    axislisthse.append(map[1][2])
                elif x == 0 and y == 3:
                    axislisthse.append(map[1][3])
                    axislisthse.append(map[0][2])
                elif x == 1 or y == 0:
                    axislisthse.append(map[0][0])
                    axislisthse.append(map[1][1])
                    axislisthse.append(map[2][0])
                elif x == 1 or y == 1:
                    axislisthse.append(map[0][1])
                    axislisthse.append(map[2][1])
                    axislisthse.append(map[1][0])
                    axislisthse.append(map[1][2])
                elif x == 1 or y == 2:
                    axislisthse.append(map[0][2])
                    axislisthse.append(map[2][2])
                    axislisthse.append(map[1][1])
                    axislisthse.append(map[1][3])
                elif x == 1 or y == 3:
                    axislisthse.append(map[0][3])
                    axislisthse.append(map[1][2])
                    axislisthse.append(map[2][3])
                elif x == 2 or y == 0:
                    axislisthse.append(map[1][0])
                    axislisthse.append(map[2][1])
                    axislisthse.append(map[3][0])
                elif x == 2 or y == 1:
                    axislisthse.append(map[1][1])
                    axislisthse.append(map[3][1])
                    axislisthse.append(map[2][0])
                    axislisthse.append(map[2][2])
                elif x == 2 or y == 2:
                    axislisthse.append(map[1][2])
                    axislisthse.append(map[3][2])
                    axislisthse.append(map[2][1])
                    axislisthse.append(map[2][3])
                elif x == 2 or y == 3:
                    axislisthse.append(map[1][3])
                    axislisthse.append(map[2][2])
                    axislisthse.append(map[2][3])
                elif x == 3 and y == 0:
                    axislisthse.append(map[2][0])
                    axislisthse.append(map[3][1])
                elif x == 3 and y == 1:
                    axislisthse.append(map[3][0])
                    axislisthse.append(map[3][2])
                    axislisthse.append(map[2][1])
                elif x == 3 and y == 2:
                    axislisthse.append(map[3][1])
                    axislisthse.append(map[3][3])
                    axislisthse.append(map[2][2])
                elif x == 3 and y == 3:
                    axislisthse.append(map[2][3])
                    axislisthse.append(map[3][2])
                tempscore = []
                totalhsescore = 0
                if " FAC" in axislisthse:
                    building_score[" HSE"].append(1)
                else:
                    for elements in axislisthse:
                        if elements == " BCH":
                            tempscore.append(2)
                        elif elements == " SHP" or elements == " HSE":
                            tempscore.append(1)
                    for score in tempscore:
                        totalhsescore += score
                    building_score[" HSE"].append(totalhsescore)
    #scoring for SHP
            if each == " SHP":
                axislistshp = []
                if x == 0 and y == 0:
                    axislistshp.append(map[1][0])
                    axislistshp.append(map[0][1])
                elif x == 0 and y == 1:
                    axislistshp.append(map[0][0])
                    axislistshp.append(map[0][2])
                    axislistshp.append(map[1][1])
                elif x == 0 and y == 2:
                    axislistshp.append(map[0][1])
                    axislistshp.append(map[0][3])
                    axislistshp.append(map[1][2])
                elif x == 0 and y == 3:
                    axislistshp.append(map[1][3])
                    axislistshp.append(map[0][2])
                elif x == 1 or y == 0:
                    axislistshp.append(map[0][0])
                    axislistshp.append(map[1][1])
                    axislistshp.append(map[2][0])
                elif x == 1 or y == 1:
                    axislistshp.append(map[0][1])
                    axislistshp.append(map[2][1])
                    axislistshp.append(map[1][0])
                    axislistshp.append(map[1][2])
                elif x == 1 or y == 2:
                    axislistshp.append(map[0][2])
                    axislistshp.append(map[2][2])
                    axislistshp.append(map[1][1])
                    axislistshp.append(map[1][3])
                elif x == 1 or y == 3:
                    axislistshp.append(map[0][3])
                    axislistshp.append(map[1][2])
                    axislistshp.append(map[2][3])
                elif x == 2 or y == 0:
                    axislistshp.append(map[1][0])
                    axislistshp.append(map[2][1])
                    axislistshp.append(map[3][0])
                elif x == 2 or y == 1:
                    axislistshp.append(map[1][1])
                    axislistshp.append(map[3][1])
                    axislistshp.append(map[2][0])
                    axislistshp.append(map[2][2])
                elif x == 2 or y == 2:
                    axislistshp.append(map[1][2])
                    axislistshp.append(map[3][2])
                    axislistshp.append(map[2][1])
                    axislistshp.append(map[2][3])
                elif x == 2 or y == 3:
                    axislistshp.append(map[1][3])
                    axislistshp.append(map[2][2])
                    axislistshp.append(map[2][3])
                elif x == 3 and y == 0:
                    axislistshp.append(map[2][0])
                    axislistshp.append(map[3][1])
                elif x == 3 and y == 1:
                    axislistshp.append(map[3][0])
                    axislistshp.append(map[3][2])
                    axislistshp.append(map[2][1])
                elif x == 3 and y == 2:
                    axislistshp.append(map[3][1])
                    axislistshp.append(map[3][3])
                    axislistshp.append(map[2][2])
                elif x == 3 and y == 3:
                    axislistshp.append(map[2][3])
                    axislistshp.append(map[3][2])
                uniquelist = []
                for uniquebuilding in axislistshp:
                    if uniquebuilding not in uniquelist:
                        uniquelist.append(uniquebuilding)
                building_score[" SHP"].append(len(uniquelist))
            y += 1
        x += 1
    # scoring for HWY
    for row in map:
        index = 0
        if row[0] == " HWY":
            if row[1] == " HWY":
                if row[2] == " HWY":
                    if row[3] == " HWY":
                        building_score[" HWY"].append(4)
                        building_score[" HWY"].append(4)
                        building_score[" HWY"].append(4)
                        building_score[" HWY"].append(4)
                    else:
                        building_score[" HWY"].append(3)
                        building_score[" HWY"].append(3)
                        building_score[" HWY"].append(3)
                else:
                    building_score[" HWY"].append(2)
                    building_score[" HWY"].append(2)
            else:
                building_score[" HWY"].append(1)
        elif row[1] == " HWY":
            if row[2] == " HWY":
                if row[3] == " HWY":
                    building_score[" HWY"].append(3)
                    building_score[" HWY"].append(3)
                    building_score[" HWY"].append(3)
                else:
                    building_score[" HWY"].append(2)
                    building_score[" HWY"].append(2)
            else:
                building_score[" HWY"].append(1)
        elif row[2] == " HWY":
            if row[3] == " HWY":
                building_score[" HWY"].append(2)
                building_score[" HWY"].append(2)
            else:
                building_score[" HWY"].append(1)
        elif row[3] == " HWY":
            building_score[" HWY"].append(1)
    #Prepare for score calculations
    bchscore = 0
    facscore = 0
    hsescore = 0
    shpscore = 0
    hwyscore = 0
    for elements in building_score[" BCH"]:
        bchscore += elements
    for elements in building_score[" FAC"]:
        facscore += elements
    for elements in building_score[" HSE"]:
        hsescore += elements
    for elements in building_score[" SHP"]:
        shpscore += elements
    for elements in building_score[" HWY"]:
        hwyscore += elements
    global currentplayertotal
    currentplayertotal = bchscore + facscore + hsescore + shpscore + hwyscore
    #printing scores
    print('\nBCH:', end=' ')
    index = 0
    for score in building_score[" BCH"]:
        if index < len(building_score[" BCH"]) - 1:
            print(str(score), end=' + ')
        else:
            print(str(score), end=' ')
        index += 1
    print("= " + str(bchscore), end='\n')
    print('FAC:', end=' ')
    index = 0
    for score in building_score[" FAC"]:
        if index < len(building_score[" FAC"]) - 1:
            print(str(score), end=' + ')
        else:
            print(str(score), end=' ')
        index += 1
    print("= " + str(facscore), end='\n')
    print('HSE:', end=' ')
    index = 0
    for score in building_score[" HSE"]:
        if index < len(building_score[" HSE"]) - 1:
            print(str(score), end=' + ')
        else:
            print(str(score), end=' ')
        index += 1
    print("= " + str(hsescore), end='\n')
    print('SHP:', end=' ')
    index = 0
    for score in building_score[" SHP"]:
        if index < len(building_score[" SHP"]) - 1:
            print(str(score), end=' + ')
        else:
            print(str(score), end=' ')
        index += 1
    print("= " + str(shpscore), end='\n')
    print('HWY:', end=' ')
    index = 0
    for score in building_score[" HWY"]:
        if index < len(building_score[" HWY"]) - 1:
            print(str(score), end=' + ')
        else:
            print(str(score), end=' ')
        index += 1
    print("= " + str(hwyscore), end='\n')
    print ("Total Score: {:d}".format(currentplayertotal))

#game end
def endgame(map):
    print("\nFinal layout of Simp City:")
    grid(map)
    score(building_score, map)
    highscore(currentplayertotal)
    init_game(buildable_locations, turn, map)

#save highscore
def highscore(currentplayertotal):
    pos = 1
    inhighscore = False
    file = open("leaderboard.json", "r")
    load_data = json.load(file)
    highscorelist = load_data
    for points in highscorelist:
        if len(highscorelist) < 10:
            inhighscore = True
        elif currentplayertotal >= points[1]:
            inhighscore = True
        else:
            pos += 1
    file.close()
    if inhighscore == True:
        username = str(input("Please enter your name (max 20 chars): "))
        while len(username) != 20:
            username = username + str(" ")
        print("Congratulations! You made the high score board at position {:d}!".format(pos))
        templist = [username, currentplayertotal]
        highscorelist.insert(pos -1,templist)
    file = open("leaderboard.json", "w+")
    file.write(json.dumps(highscorelist))
    file.close()
    printhighscore()

#Print highscore
def printhighscore():
    poslist = [" 1."," 2."," 3."," 4."," 5."," 6."," 7."," 8."," 9.","10."]
    players = 0
    file = open("leaderboard.json", "r")
    load_data = json.load(file)
    highscorelist = load_data
    print ("\n--------- HIGH SCORES ---------")
    print ("Pos Player\t\t\t\t  Score")
    print ("--- ------\t\t\t\t  -----")
    if len(highscorelist) < 10:
        while players < len(highscorelist):
            print ("{:s} {:s}\t{:>d}".format(poslist[players], highscorelist[players][0], highscorelist[players][1]))
            players += 1
    else:
        while players < len(poslist):
            print ("{:s} {:s}\t{:>d}".format(poslist[players], highscorelist[players][0], highscorelist[players][1]))
            players += 1
    print ("-------------------------------")
    file.close()

#save game
def savegame(buildinglistdup, buildable_locations, building_count):
    print ("Saving game")
    savedict = {"buildinglist": buildinglistdup,
                "buildable_locations": buildable_locations,
                "building_count": building_count,
                "map": map,
                "empty": empty}
    file = open("savegame.json", "w+")
    file.write(json.dumps(savedict))
    file.close()

#load game
def loadgame():
    file = open("savegame.json", "r")
    load_data = json.load(file)
    buildinglistdup = load_data.get("buildinglist")
    buildable_locations = load_data.get("buildable_locations")
    building_count = load_data.get("building_count")
    map2 = load_data.get("map")
    empty = load_data.get("empty")
    file.close()
    turn = 17 - len(buildable_locations)
    newgame(buildable_locations, turn, map2, building_count, empty)

#game
init_game(buildable_locations, turn, map)
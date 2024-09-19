print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


direction = input("You reach the island, do you go towards the jungle (J) or towards the mountains (M)?\n")
if direction == "M":
  print("You approach two caves, one has a danger symbol, and the other seems abandoned.")
  cave = input("Do you go into the abandoned cave (AC) or the cave with the danger symbol (DS)?")
  if cave == "AC":
    print("You enter the cave")
    chest = input("You see a blue, yellow, and red chest. Which chest do you open to find the treasure? (B), (Y), (R).\n")
    if chest == "B":
      print("Acid spews out from the chest and blinds you.\n <<<GAME OVER>>>")
    elif chest == "R":
      print("You find the treasure of the island, $100! Congrats!!!")
    elif chest == "Y":
      print("A Thousand Spiders crawl on you from within the chest, poisoning you.\n <<<GAME OVER>>>")
    else:
      print("You chose wrong... Choose B, R, or Y next time... <<<GAME OVER>>>")
  else:
    print("YOU SHOUILD OF LISTENED TO THE WARNING\n <<<GAME OVER>>>")
elif direction == "J":
  print("You get mauled by gorrilas, <<<GAME OVER>>>.\n")
else:
  print("You must choose either J (Jungle) or M (Mountains)")


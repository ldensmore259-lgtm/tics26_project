import time
################################
def clock_countdown():
    #if game_start == True:
        clock = 300
        for i in range(300):
            clock -=1
            time.sleep(1)
            print (clock) 
##################################
def game_start():
    # Opening dialouge
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(.25)
    print("You sit up in the cryopod. Red emergency lights strobe across the frost-covered glass." "")
    time.sleep(.25)
    print("A soft female voice repeats from every speaker:")
    time.sleep(.25)
    print("“Don’t trust the countdown. Don’t trust the countdown.”")
    time.sleep(.25)
    print("A glowing panel on the wall shows:")
    time.sleep(.25)
    print("LIFE SUPPORT: 04:58")
    time.sleep(.25)
    print("The corridor outside is dark except for distant flickering lights.")
    time.sleep(.25)
    print("Your personal log is blank. You don’t remember your name.")
    time.sleep(.25)
    print("What do you do?")
    time.sleep(.25)
    print("-------------------------------------------------")
    time.sleep(.25)
    print("1, Open the door and head for the bridge")    
    time.sleep(.25)
    print("2, Stay and try to access the cryopod’s logs")
    time.sleep(.25)
    print("3, Head for the emergency airlock")
    time.sleep(.25)
    answer_1 = input("Type 1, 2, or 3 to choose your action: ")
##################################

print("Hello!, welcome to my game. Please give me 100 percent or I will be sad :( You see that, Thats gonna be me if I dont get a 100 percent")
start=input("Type start to start, or anything else to be yelled at")
if start == "start":
    game_start()
    clock_countdown()
    else:
        print("WROOOOOOOOOOOOOOOOOOOOOOOONG THATS NOT START AND I SAID TYPE START SO NOW STOP THEN START THE PROGRAM AGAIN THEN TYPE START OR ELSE I WILL BE SAD AND YOU DONT WANT ME TO BE SAD DO YOU? I DONT THINK SO SO TYPE START NOW")
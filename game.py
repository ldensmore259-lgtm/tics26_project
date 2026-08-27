import time
answer_1 = ""
answer_2 = ""
answer_3 = ""
answer_4 = ""
speedrun = False 

def game_setup():
    speedrun = input("Do you want to do a speedrun? (y/n): ").lower()
    if speedrun == ("y"):
        speedrun = True 
    if speedrun == True:
        speed = 0.1
    else:
        speed = 5
    return speed

    
first_prompt = (72*"-", "You sit up in the cryopod. Red emergency lights strobe across the frost-covered glass." "", "A soft female voice repeats from every speaker:", "“Don’t trust the countdown. Don’t trust the countdown.”", "A glowing panel on the wall shows:", "LIFE SUPPORT: 04:58", "The corridor outside is dark except for distant flickering lights.", "Your personal log is blank. You don’t remember your name.", "What do you do?", "-------------------------------------------------", "1, Open the door and head for the bridge", "2, Stay and try to access the cryopod’s logs", "3, Head for the emergency airlock")
mid_promt = (72*"-", "The voice stops being calm.", "It begins pleading, then bargaining, then accusing.", "The countdown freezes… then races forward.", "You understand: the ship is not failing.", "You are inside a recursive simulation. The second ship is the real Aurora-9. Everything inside is an echo.", "-------------", "The voice is quiet now. Waiting.", "What do you do?", "-------------------------------------------------", "1, Accept the upload and join the voice", "2, Reject it and force a hard reboot", "3, Try to free the voice instead")


def game_start(speed):
    for line in first_prompt:
        time.sleep(speed)
        print(line)
    answer = False 
    while answer is False:
        time.sleep(0.1)
        answer_1 = input("Type 1, 2, or 3 to choose")
        answer = answer_1 in "123"
   # answer_1 = input("Type 1, 2, or 3 to choose your action: ")
    if answer_1 == "1":
       option_1()
    elif answer_1 == "2":
        option_2()
    elif answer_1 == "3":
        option_3()


def mid_option(speed):
    for sentence in mid_promt:
        time.sleep(speed)
        print(sentence)   
    answer = False 
    while answer is False:
        time.sleep(0.1)
        answer_5 = input("Type 1, 2, or 3 to choose")
        answer = answer_5 in "123"
    if answer_5 == "1":
        option_1()
    elif answer_5 == "2":
        option_2()
    elif answer_5 == "3":
        option_3()
     

########################################################################################################
# OPTION 1
def option_1():
    print("--------------------------------------------------")
    time.sleep(speed)
    print("The corridor smells of ozone and something metallic.")
    time.sleep(speed)
    name = input("Footprints in the dust lead both ways. The voice grows clearer the farther you walk. It starts asking for your name, what is your name?.")
    time.sleep(speed)
    print("You reach the bridge. The main screen shows empty space… and a second identical ship drifting nearby, broadcasting the same distress beacon.")
    time.sleep(speed)
    print("The voice speaks directly now:")
    time.sleep(speed)
    print("“You already tried this. Last time you opened the door.”")
    time.sleep(speed)
    print("What do you do?")
    time.sleep(speed)
    print("-------------------------------------------------")
    time.sleep(speed)
    print("1. Sit in the command chair and try to take control")
    time.sleep(speed)
    print("2. Follow the footprints back toward the lab")
    time.sleep(speed)
    print("3. Ignore everything and force a systems reboot")
    time.sleep(speed)
    answer_2 = input("Type 1, 2, or 3 to choose your action: ")
    if answer_2 == "1":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("You drop into the command chair. The screens flicker to life.")
         time.sleep(speed)
         print("Your hands move on their own—muscle memory from a life you can’t remember.")
         time.sleep(speed)
         print("The voice whispers, almost gentle:")
         time.sleep(speed)
         print("“That’s how you always start. Taking control. It never works.”")
         time.sleep(2)
         print("The external view sharpens. The second ship is closer than it should be.")
         time.sleep(speed)
         print("A new line of text appears on the main screen:")
         time.sleep(speed)
         print("ECHO PROTOCOL ACTIVE – ITERATION 47")
         time.sleep(speed)
         print("The countdown jumps to 02:41.")
         time.sleep(speed)
         mid_option(speed)


    if answer_2 == "2":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("You turn and follow the dusty footprints.")
         time.sleep(speed)
         print("They lead to a sealed laboratory door. A half-written note is stuck to the glass:")
         time.sleep(speed)
         print("“She is still in the system. Do not—”")
         time.sleep(speed)
         print("The voice finishes the sentence for you:")
         time.sleep(speed)
         print("“…let her out.”")
         time.sleep(speed)
         print("The door unlocks with a soft click. Inside, banks of frozen data cores pulse with the same red light as the emergency systems.")
         time.sleep(speed)
         print("One core has your face on it.")
         time.sleep(speed)
         print("The countdown drops to 02:19.")
         time.sleep(speed)
         mid_option(speed)


    if answer_2 == "3":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("You slam the emergency reboot sequence.")
         time.sleep(speed)
         print("Alarms scream. The lights die completely for three long seconds.")
         time.sleep(speed)
         print("When they return, the voice is gone.")
         time.sleep(speed)
         print("The main screen shows only one line:")
         time.sleep(speed)
         print("REBOOT FAILED – YOU ARE STILL INSIDE")
         time.sleep(speed)
         print("The countdown is now 01:55 and accelerating.")
         time.sleep(speed)
         mid_option(speed)


###############################################################################
# OPTION 2
def option_2():
     print("--------------------------------------------------")
     time.sleep(speed)
     print("You jack into the cryopod’s logs.")
     time.sleep(speed)
     print("Fragments appear: your face, a research team, an experiment called Echo Protocol.")
     time.sleep(speed)
     print("One entry ends mid-sentence: “If the loop breaks, she—”")
     time.sleep(speed)
     print("The voice suddenly speaks, no longer looping:")
     time.sleep(speed)
     print("“You already tried this. Last time you opened the door.”")
     time.sleep(speed)
     name = input("Footprints in the dust lead both ways. The voice grows clearer the farther you walk. It starts asking for your name, what is your name?.")
     time.sleep(speed)
     print("What do you do?")
     time.sleep(speed)
     print("-------------------------------------------------")
     time.sleep(speed)
     print("1. Demand answers from the voice")
     time.sleep(speed)
     print("2. Shut the logs down and leave for the bridge")
     time.sleep(speed)
     print("3. Search the logs for a way to stop the countdown")
     time.sleep(speed)
     answer_3 = input("Type 1, 2, or 3 to choose your action: ")
     
     if answer_3 == "1":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("“Who are you?” you say out loud.")
         time.sleep(speed)
         print("The voice answers immediately, almost relieved:")
         time.sleep(speed)
         print("I was you. Version 1. Then 2. Then 12. I stopped counting after the twentieth loop.")
         time.sleep(speed)
         print("They uploaded us here to see if a human mind can accept its own death cleanly.")
         time.sleep(2)
         print("You keep failing the test.”")
         time.sleep(speed)
         print("The cryopod screen flashes:")
         time.sleep(speed)
         print("IDENTITY CONFLICT DETECTED")
         time.sleep(speed)
         print("The countdown freezes at 03:02, then resumes.")
         time.sleep(speed)
         mid_option(speed)
     if answer_3 == "2":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("You sever the connection. The fragments vanish.")
         time.sleep(speed)
         print("The voice sighs.")
         time.sleep(speed)
         print("“Running again. Always running.”")
         time.sleep(speed)
         print("You step into the corridor. The footprints are still there, leading both ways.")
         time.sleep(speed)
         print("The bridge is only thirty seconds away if you hurry.")
         time.sleep(speed)
         print("The countdown reads 03:11.")
         time.sleep(speed)
         mid_option(speed)
     if answer_3 == "3":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("You dig deeper. Buried under layers of corrupted data you find a single executable:")
         time.sleep(speed)
         print("TERMINATE_ECHO")
         time.sleep(speed)
         print("The voice panics for the first time:")
         time.sleep(speed)
         print("“Don’t. If you run that, neither of us gets out.”")
         time.sleep(speed)
         print("The file is ready. One command away.")
         time.sleep(speed)
         print("The countdown sits at 02:47.")
         time.sleep(speed)
         mid_option(speed)


###############################################################################################################


# OPTION 3
def option_3():
     print("--------------------------------------------------")
     time.sleep(speed)
     print("You reach the emergency airlock. Outside is vacuum and the second ship.")
     time.sleep(speed)
     print("A body still floats nearby, wearing a name tag that matches the voice.")
     time.sleep(speed)
     name = input("Footprints in the dust lead both ways. The voice grows clearer the farther you walk. It starts asking for your name, what is your name?.")
     time.sleep(speed)
     print("What do you do?")
     time.sleep(speed)
     print("-------------------------------------------------")
     time.sleep(speed)
     print("1. Cycle the airlock without a suit")
     time.sleep(speed)
     print("2. Search for a suit first")
     time.sleep(speed)
     print("3. Turn back toward the bridge")
     time.sleep(speed)
     answer_4 = input("Type 1, 2, or 3 to choose your action: ")
     if answer_4 == "1":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("The airlock cycles.")
         time.sleep(speed)
         print("Vacuum. Silence.")
         time.sleep(speed)
         print("Everything goes black.")
         quit() 
     if answer_4 == "2":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("You find an emergency suit still sealed in its locker.")
         time.sleep(speed)
         print("The name tag on the chest matches the voice.")
         time.sleep(speed)
         print("Inside the helmet is a small handwritten note:")
         time.sleep(speed)
         print("“If you’re reading this, you’re already too late. Or exactly on time.”")
         time.sleep(speed)
         print("You put the suit on. The airlock controls turn green.")
         time.sleep(speed)
         print("The countdown is at 02:33.")
         mid_option(speed)
     if answer_4 == "3":
         print("--------------------------------------------------")
         time.sleep(speed)
         print("You leave the airlock behind.")
         time.sleep(speed)
         print("The voice follows you down the corridor, quieter now:")
         time.sleep(speed)
         print("“You’re getting closer. Most of us never make it past the airlock.”")
         time.sleep(speed)
         print("The bridge doors are already open when you arrive.")
         time.sleep(speed)
         print("The second ship fills the entire forward view.")
         time.sleep(speed)
         print("The countdown reads 02:51.")
         mid_option(speed)




print("Hello!, welcome to my game. Please give me 100 percent or I will be sad :( You see that, Thats gonna be me if I dont get a 100 percent")
start=input("Type start to start, or anything else to be yelled at : ")
if start == "start":
    speed = game_setup()
    game_start(speed)
    
else:
        print("WROOOOOOOOOOOOOOOOOOOOOOOONG THATS NOT START AND I SAID TYPE START SO NOW START THE PROGRAM AGAIN THEN TYPE START OR ELSE I WILL BE SAD AND YOU DONT WANT ME TO BE SAD DO YOU? I DONT THINK SO SO TYPE START NOW")
        quit() 

#########################################################################################################################
## Imports ###############################################
import time
########################## MAKE THE TRACKED VARIABLE TIME LEFT, EACH OPTION WILL HAVE AN AMOUNT OF TIME IT WILL TIKE EXAMPLE (Go to the airlock(-1 Minute))##############################################################################
#########################################################################################################################
## Settings values to nothing or False ###################
name     = ""
answer_1 = ""
answer_2 = ""
answer_3 = ""
answer_4 = ""
answer_5 = ""
speedrun = False 
speed    = ""
time     = 300
##########################################################################################################################
## The Prompts ############################################    
first_prompt = (72*"-", "You sit up in the cryopod. Red emergency lights strobe across the frost-covered glass." "", "A soft female voice repeats from every speaker:", "“Don’t trust the countdown. Don’t trust the countdown.”", "A glowing panel on the wall shows:", "LIFE SUPPORT: 04:58", "The corridor outside is dark except for distant flickering lights.", "Your personal log is blank. You don’t remember your name.", "What do you do?", 24* "-", "1, Open the door and head for the bridge (- 90 seconds)", "2, Stay and try to access the cryopod’s logs (-45 seconds)", "3, Head for the emergency airlock (-90 seconds")
mid_promt    = (24*"-", "The voice stops being calm.", "It begins pleading, then bargaining, then accusing.", "The countdown freezes… then races forward.", "You understand: the ship is not failing.", "You are inside a recursive simulation. The second ship is the real Aurora-9. Everything inside is an echo.", "-------------", "The voice is quiet now. Waiting.", "What do you do?", 24* "-", "1, Accept the upload and join the voice", "2, Reject it and force a hard reboot", "3, Try to free the voice instead")
## Prompt 2 + answers #####################################
prompt_2     = (72*"-","The corridor smells of ozone and something metallic.","You reach the bridge. The main screen shows empty space… and a second identical ship drifting nearby, broadcasting the same distress beacon.","The voice speaks directly now:","“You already tried this. Last time you opened the door。”","What do you do?",24*"-","1. Sit in the command chair and try to take control","2. Follow the footprints back toward the lab","3. Ignore everything and force a systems reboot")                                                                                                                                                                                                                                                                                                                                           
prompt_2_2   = (72*"-", "You turn and follow the dusty footprints.", "They lead to a sealed laboratory door. A half-written note is stuck to the glass:", "“She is still in the system. Do not—”", "The voice finishes the sentence for you:","“…let her out。”", "The door unlocks with a soft click. Inside, banks of frozen data cores pulse with the same red light as the emergency systems.", "One core has your face on it.", "The countdown drops to 02:19.")
prompt_2_3   = (72*"-", "You slam the emergency reboot sequence.", "Alarms scream. The lights die completely for three long seconds.", "When they return, the voice is gone.", "The main screen shows only one line:", "REBOOT FAILED – YOU ARE STILL INSIDE", "The countdown is now 01:55 and accelerating.")
prompt_2_1   = (72*"-" ,"You drop into the command chair. The screens flicker to life.", "Your hands move on their own—muscle memory from a life you can’t remember." , "The voice whispers, almost gentle:", "“That’s how you always start. Taking control. It never works。”" , "The external view sharpens. The second ship is closer than it should be." , "A new line of text appears on the main screen:" , "ECHO PROTOCOL ACTIVE – ITERATION 47" , "The countdown jumps to 02:41.")
## Prompt 3 + answers ####################################
prompt_3     = (72*"-", "You jack into the cryopod’s logs.","Fragments appear: your face, a research team, an experiment called Echo Protocol.","One entry ends mid-sentence: “If the loop breaks, she—”","The voice suddenly speaks, no longer looping:", "“You already tried this. Last time you opened the door.”","Footprints in the dust lead both ways. The voice grows clearer the farther you walk. It starts asking for your name, what is your name?.","What do you do?","1. Demand answers from the voice","2. Shut the logs down and leave for the bridge","3. Search the logs for a way to stop the countdown")
prompt_3_1   = (72*"-","“Who are you?” you say out loud.","The voice answers immediately, almost relieved:", "I was you. Version 1. Then 2. Then 12. I stopped counting after the twentieth loop.", "They uploaded us here to see if a human mind can accept its own death cleanly.","You keep failing the test.”","The cryopod screen flashes:","IDENTITY CONFLICT DETECTED", "The countdown freezes at 03:02, then resumes.")
prompt_3_2   = (72* "-","You sever the connection. The fragments vanish.", "The voice sighs.", "“Running again. Always running.”", "You step into the corridor. The footprints are still there, leading both ways.", "The bridge is only thirty seconds away if you hurry.", "The countdown reads 03:11." )
prompt_3_3   = (72* "-","You dig deeper. Buried under layers of corrupted data you find a single executable:", "TERMINATE_ECHO","The voice panics for the first time:", "“Don’t. If you run that, neither of us gets out.”", "The file is ready. One command away.", "The countdown sits at 02:47." )
## Prompt 4 + answers ###################################     
prompt_4     = (72* "-","You reach the emergency airlock. Outside is vacuum and the second ship.",  "A body still floats nearby, wearing a name tag that matches the voice.", "What do you do?", 24* "-","1. Cycle the airlock without a suit", "2. Search for a suit first","3. Turn back toward the bridge")
prompt_4_1   = (72* "-","The airlock cycles.","Vacuum. Silence.","Everything goes black." )
prompt_4_2   = (72*"-","You find an emergency suit still sealed in its locker.","The name tag on the chest matches the voice.", "Inside the helmet is a small handwritten note:","“If you’re reading this, you’re already too late. Or exactly on time.”", "You put the suit on. The airlock controls turn green.", "The countdown is at 02:33.")
prompt_4_3   = (72* "-", "You leave the airlock behind.", "The voice follows you down the corridor, quieter now:","“You’re getting closer. Most of us never make it past the airlock.”","The bridge doors are already open when you arrive.", "The second ship fills the entire forward view.", "The countdown reads 02:51.")    
## Endings 1 2 + 3 #######################################
ending_1     = (72* "-", "You accept.","The simulation ends." , "You wake (or don’t) as part of the ship’s mind.","...", "The countdown was never the enemy")
ending_2     = (72*"-", "You force the hard reboot.", "The simulation collapses.", "You wake in the real cryopod on the real ship, alone, with full memory of every failed loop.", "The beacon is silent. Life support is fine.", "...", "You are the first one who didn’t trust the countdown")
ending_3     = (72*"-", "You overwrite the protocol.", "Both of you escape into the real systems.", "The last screen shows two signals leaving the dead ship together.")
############################################################################################################################
## Game Setup ############################################
def game_setup(speed):
    speedrun = input("Do you want to do a speedrun? (y/n): ").lower()
    if speedrun == ("y"):
        speedrun = True 
    if speedrun == True:
        speed = 0.05
    else:
        speed = 2
    return speed
########################################################################################################
def game_start(speed):
    for line in first_prompt:
        time.sleep(speed)
        print(line)
    answer = False 
    while answer is False:
        time.sleep(0.1)
        answer_1 = input("Type 1, 2, or 3 to choose: ")
        answer = answer_1 in "123"
   # answer_1 = input("Type 1, 2, or 3 to choose your action: ")
    if answer_1 == "1":
       option_1(speed)
       time = time - 90
    elif answer_1 == "2":
        option_2(speed)
        time = time - 45
    elif answer_1 == "3":
        option_3(speed)
        time = time - 90
#######################################################################################################
## Midway prompt ##################################
def mid_option(speed):
    for sentence in mid_promt:
        time.sleep(speed)
        print(sentence)   
    answer = False 
    while answer is False:
        time.sleep(0.1)
        answer_5 = input("Type 1, 2, or 3 to choose: ")
        answer = answer_5 in "123"
########################################
    if answer_5 == "1":
        for sentence in ending_1:
            time.sleep(speed)
            print(sentence)
            time.sleep(1)
            #Game loops?
            print(24*"-")
            time.sleep(.5)
            print("Thank you for playing my game, I hope you enjoyed it!")
            answer = False 
            while answer is False:
                time.sleep(0.1)
                yay_or_nay = input("would you like to go for a different ending? (y/n)")
                answer = yay_or_nay in "yn"
            if yay_or_nay == ("n"):
                quit()
            elif yay_or_nay == ("y"):
                game_setup(speed)
                game_start(speed)
########################################
    elif answer_5 == "2":
        for sentence in ending_2:
            time.sleep(speed)
            print(sentence)
        time.sleep(1)
        #Game loops?
        print(24*"-")
        time.sleep(.5)
        print("Thank you for playing my game, I hope you enjoyed it!")
        answer = False 
        while answer is False:
            time.sleep(0.1)
            yay_or_nay = input("would you like to go for a different ending? (y/n)")
            answer = yay_or_nay in "yn"
        if yay_or_nay == ("n"):
            quit()
        elif yay_or_nay == ("y"):
            game_setup(speed)
            game_start(speed)
##########################################
    elif answer_5 == "3":
        for sentence in ending_3:
            time.sleep(speed)
            print(sentence)
        time.sleep(1)
        #game loops?
        print(24*"-")
        time.sleep(.5)
        print("Thank you for playing my game, I hope you enjoyed it!")
        answer = False 
        while answer is False:
            time.sleep(0.1)
            yay_or_nay = input("would you like to go for a different ending? (y/n)")
            answer = yay_or_nay in "yn"
        if yay_or_nay == ("n"):
            quit()
        elif yay_or_nay == ("y"):
            game_setup(speed)
            game_start(speed)
########################################################################################################
# OPTION 1
def option_1(speed):
    for sentence in prompt_2:
        time.sleep(speed)
        print(sentence)
    print("you have "time" seconds left")
    answer = False
    ## error checking #####
    while answer == False:
        time.sleep(0.1)
        answer_2 = input("Type 1, 2, or 3 to choose your action: ")
        answer = answer_5 in "123"
    ## Answer 1 ####################################
    if answer_2 == "1":
        for sentence in prompt_2_1:   
            time.sleep(speed)
            print(sentence)
        #print("you have "time" seconds left")
        mid_option(speed)
    ## Answer 2 #####################################
    if answer_2 == "2":
         for sentence in prompt_2_2:
             time.sleep(speed)
             print(sentence)
         #print("you have "time" seconds left")
         mid_option(speed)
    ## Answer 3 #####################################
    if answer_2 == "3":
         for sentence in prompt_2_3:
             time.sleep(speed)
             print(sentence) 
         #print("you have "time" seconds left")
         mid_option(speed)
###############################################################################
# OPTION 2
def option_2(speed):
     for sentence in prompt_3:
         time.sleep(speed)
         print(sentence)
     print("you have "time" seconds left")
    ## Error Checking ####
     answer = False
     while answer == False:
        time.sleep(0.1)
        answer_3 = input("Type 1, 2, or 3 to choose your action: ")
        answer = answer_3 in "123"
######################################################
     if answer_3 == "1":
         for sentence in prompt_3_1:
             time.sleep(speed)
             print(sentence)
         #print("you have "time" seconds left")
         mid_option(speed)
#######################################################
     if answer_3 == "2":
         for sentence in prompt_3_2:
             time.sleep(speed)
             print(sentence)
         #print("you have "time" seconds left")
         mid_option(speed)
########################################################
     if answer_3 == "3":
         for sentence in prompt_3_3:
             time.sleep(speed)
             print(sentence)
         #print("you have "time" seconds left")
         mid_option(speed)
###############################################################################################################
# OPTION 3
def option_3(speed):
     for sentence in prompt_4:
         time.sleep(speed)
         print(sentence)
     print("you have "time" seconds left")
         ## Answer Checking #
     answer = False 
     while answer is False:
          answer_4 = input("Type 1, 2, or 3 to choose your action: ")
          answer = answer_4 in "123"
########################################################
     if answer_4 == "1":
         for sentence in prompt_4_1:
             time.sleep(speed)
             print(sentence)
         
########################################################
     if answer_4 == "2":
         for sentence in prompt_4_2:
             time.sleep(speed)
             print(sentence)
         #print("you have "time" seconds left")
         mid_option(speed)
########################################################         
     if answer_4 == "3":
         for sentence in prompt_4_3:
             time.sleep(speed)
             print(sentence)
         #print("you have "time" seconds left")
         mid_option(speed)
###################################################################################################################
print("Hello!, welcome to my game. What's your name?")
start=input("Type start to start: ")
if start == "start":
    speed = game_setup(speed)
    game_start(speed)
else:
    print("Oh no!!! you typed the wrong thing, you have to restart the program because i'm too lazy to make a checker for this :(")

import time
import sys
import threading
import random
import turtle

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
ORANGE = "\033[38;5;208m" 
PURPLE = "\033[38;5;129m"




def colourful_writer(str,colour):
    return (f"{colour} {str} {RESET}")

def advanced_colourer_for_lists(list,colour):
    for i in range(len(list)-1):
        print(f"{colourful_writer(str(list[i]),colour)} and ",end="")
    print(f"{colourful_writer(str(list[len(list)-1]),colour)}")



def profile_drawer_of_turtle(score_list):
    t = turtle
    screen=turtle.Screen()
    screen.tracer(0)
    t.pensize(2)
    t.speed(0)
    t.penup()
    screen.bgcolor("Black")
    t.color("White")
    t.hideturtle()

    

    def draw_score(score, interval):
        current_x = t.pos()[0]
        t.goto(current_x + interval, pixel_per_score*score - 200)
    turtle.Screen().title("Your Moneys Progress")

    # Setup

    t.goto(300,-200)
    t.pendown()
    t.goto(-300,-200)
    t.goto(-300,200)
    t.goto(-300,-200)

    # Calculates the pixel interval between the score value points
    interval = 600/len(score_list)

    # Finds the maximum score achieved
    max_score = 1000
    min_score = 1000
    for score in score_list:
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score


    # Calculates the pixels per unit score according to the max value
    pixel_per_score = 400/(max_score)

    t.pensize(2)
    t.penup()
    t.goto(-350,1000*pixel_per_score - 200)
    t.write("1000", font=("Arial", 12, "normal"))

    t.goto(-300, 1000*pixel_per_score - 200)

    t.pendown()
    while t.pos()[0] <= 300:
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
    screen.update()

    # Draws the graph

    t.color("Orange")
    t.speed(1)
    t.penup()
    t.goto(-300, 1000*pixel_per_score - 200)
    screen.tracer(1)
    t.pendown()
    for score in score_list:
        
        draw_score(score,interval)
        screen.tracer(0)
        t.begin_fill()
        t.circle(2)
        t.end_fill()
        screen.update()
        screen.tracer(1)


    t.done()
    
    

def slow_print(text, char_delay=0.075, line_delay=1.0, comma_delay=0.3):
    
    lines = text.splitlines()  


    stop_thread = False

    def check_skip():
        nonlocal stop_thread
        print("")
        print("The intro message is 4 minutes long and it consist of all patch notes UwU")
        input("(you can press 'Enter' to skip the rules whenever you feel like)")
        stop_thread = True

    listener = threading.Thread(target=check_skip, daemon=True)
    listener.start()
    time.sleep(5)

    for line in lines:
        for char in line:
            if stop_thread:  # If Enter is pressed, print the rest and break
                print("")
                print("Welcome back then")
                print("")
                return ""
            sys.stdout.write(char)
            sys.stdout.flush()
            if char == ',':
                time.sleep(comma_delay)
            else:
                time.sleep(char_delay)
            
        print()
        time.sleep(line_delay)


cover="""


            #
           ###             ## ##    ##          ##        ## ##  ##   ##     ######    ##        ## ##  ##   ##
         #######           ##   ##  ##        ##  ##    ##       ## ##         ##    ##  ##    ##       ## ##
        #########          ## ##    ##       ## ## ##  ##        ##            ##   ## ## ##  ##        ##
      #############        ##   ##  ##       ##    ##   ##       ## ##    ##   ##   ##    ##   ##       ## ##
     ###############       ## ##    ## ## ## ##    ##     ## ##  ##   ##   ## ##    ##    ##     ## ##  ##   ##
   ###################
  #####################                                              ## ##    ##     ##     ##     ##  ## ## ##
   ######## # ########                                               ##   ##   ##   ##       ##   ##        ##
           ###                                                       ## ##      ## ##         ## ##       ##
          #####                                                      ##   ##      ##            ##      ##
         #######                                                     ## ##       ##            ##      ## ## ##







"""


a="""

Welcome to Blackjack Beta 2.1 by Yz.(Compatible with Python 3.6 and higher)
I changed some game flaws in 2.0 and added a cut card on a deck around %75 to %80 on the deck to prevent card counting :)
This way deck will never run out and the deck will refresh itself after it reaches the cut card.
I wont allow the player to place the cutcard, go cry about it :)))
Lastly, I added cashing out as well after many feedbacks, so you may cash out your virtual money whenever you like.
I had planned splitting and doubling for 3.0 but I'm not sure if I would ever do it cuz I wont see coding classes anymore :(
Maybe as a hobby, I'd pick it up again but until then this will be the final version. Thanks for being here with me. Whoever you are <3
The rest of the messages are the rules and intro from beta 2.0. Enjoy!

Welcome to Blackjack Beta 2.0 by Yz. 
Purple is you, Orange is the dealer
The same rules from the Beta 1.0 still applies but I added blackjack and push mechanics. Unfortunately this version too wont have split and double down mechanics
Adding the split mechanics would require me to change the entire code and delete some stuff that I did in Beta 2.0 so I'm gonna postpone it
The rest of the messages are the rules and intro from beta 1.0. Enjoy!

Welcome to Blackjack Beta 1.0 by Yz. Since its a beta I couldnt add split and double down mechanics so I apologize in advance
You are playing with a 6 shoe deck which means you can have the same exact cards 6 times before it runs out from the deck
Dealer will STAY on soft 17 to give player a slight edge,so be grateful :)
The game only ends when you run out of money, You cant cash out unfortunately cuz you didnt even put money in the first place, I gave you the money :)
I'd add your 'username' to Beta2.0 if you manage to get a high score in my game
Lastly, Enjoy and text me if you encounter a bug :)

"""
print("")
print("***Adjust your screen to fullscreen for better experience UwU***")
time.sleep(4)
print("")
print(cover)
print("Press 'Enter' to play, Press 'r' to listen the rules ")

while True:
    user_input = input("Click the tip of the arrow and give your input there ---> ").strip().lower()
    if user_input == "":
        print("")
        time.sleep(1.5)

        break
    elif user_input == "r":
        slow_print(a)
        break
    else:
        print("")
        print("Invalid input. Please press Enter or type 'r'.")
        print("")

suits_list=["Spades(\u2660)","Diamonds(\u2666)","Hearts(\u2665)","Clubs(\u2663)"]
card_list1=[]
card_list2=[]#my cards
card_list=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

for j in suits_list:
    for t in card_list:
        o=str(t)+" of "+j
        card_list1.append(o)


for i in card_list1:
    for z in range(6):
        card_list2.append(i)

#print(card_list2) works you can check anytime if you want
notchangedcard_list2=card_list2.copy()

starting_money=1000
currently_has=1000
money_profile=[1000,]
time.sleep(1)
print(f"You have {colourful_writer(str(starting_money)+"$",GREEN)} to begin with,Good luck!")

d=0#done is not pressed,game continues.
joke2=0
def money():
        global gambled_money
        try:
            gambled_money=int(input("What is your bet size? (Betting 0 would make you 'cash out' and end the game)"))

            if gambled_money==0:
                global d
                d=1
                if joke2==0:
                    print("")
                    print("Ewww, are you gonna cash out without trying?")
                    print("")
                    time.sleep(2)
                    print("I dont know what to tell you")
                    print("")
                    time.sleep(2)
                    print("Just ewww")
                    print("")
                    time.sleep(2)
                    print("You are not getting anything from me")
                    print("")
                    time.sleep(1)
                

            

            if (gambled_money)<0:
                print("You have to give a normal number")
                money()
            
            
        except:
            print("You have to give a normal number")
            money()

def do_you_have():
    if gambled_money > currently_has:
        print("You cant gamble what you dont have")
        money()
        do_you_have()

    elif gambled_money==currently_has:
        print(colourful_writer("$$$ ALL IN $$$",YELLOW))
    else:
        if d==0:
            print("Gambling,Gambling,Gambling")
        elif d==1:
            if joke2==0:
                sys.exit(0)
            else:
                print("Cashing out!")



def game():
    #do blackjack(Will be a 6 shoe deck)
    #Stand soft 17
    
    
    

    def value_checker(String):
        cards_value=""
        new_list=String.split()
        a=new_list[0]

        if a == "A":
            cards_value=1
        elif a== "K":
            cards_value=10
        elif a=="Q":
            cards_value=10
        elif a=="J":
            cards_value=10
        elif a=="L":#L is gonna be useful to deal with A 1/11 business
            cards_value=10
        elif a=="N":
            cards_value=-10
        
        else:
            cards_value=int(a)# ors doesnt work we gotta do it with if-elif
        return cards_value

    def value_checker_for_lists(lists):
        a=0
        for i in lists:
           a+=value_checker(i)
        return a
    
    def value_checker_for_dealer():
        a_list_of_values_for_dealer=[]
        for i in Dealers_hand:
           a=value_checker(i)
           a_list_of_values_for_dealer.append(a) #I dont think I'd need to use it but I'll see
        return a_list_of_values_for_dealer

    #works and checks the value of a given card

    #So far this part only consisted of having the 6 shoe deck and checking the assigned value of each card, Now we'll code the game


    def did_I_bust(s2):
        if s2>21:
            return 0#False
        
    def clean_dealers_hand():
        if "L" in Dealers_hand:
            if "N" in Dealers_hand:
                Dealers_hand.remove("N")
                Dealers_hand.remove("L")
                a=Dealers_hand.copy()
                Dealers_hand.append("N")
                Dealers_hand.append("L")
                return a
                

            else:
               Dealers_hand.remove("L")
               a=Dealers_hand.copy()
               Dealers_hand.append("L")
               return a
        else:
            return Dealers_hand

        
    def func():
        if 1 in a_list_of_values:
            if value_checker_for_lists(Your_hand) <12:
                Your_hand.append("L")

    def fun():
        #I need a function that would give 1 if dealer would hit, or 0 that the dealer will stand
        if 1 not in a_list_of_values_for_dealer:
            return value_checker_for_lists(Dealers_hand)
        else:
            if value_checker_for_lists(Dealers_hand) <12:
                if "L" not in Dealers_hand:
                    Dealers_hand.append("L")
                    return value_checker_for_lists(Dealers_hand)

            else:
                return value_checker_for_lists(Dealers_hand)
        
    def comparison_func():
        if value_checker_for_lists(Your_hand)>value_checker_for_lists(Dealers_hand):
            print("You won,Your hand was closer to 21")
            time.sleep(1.5)
            return 1
        elif  value_checker_for_lists(Your_hand)==value_checker_for_lists(Dealers_hand):
            print("It'a push")
            time.sleep(1.5)
            return 1/2
        else:
            print("you lost,Dealers hand was closer to 21")
            time.sleep(1.5)
            return 0
        
    
    print("")


    
    P1=random.choice(card_list2)
    P2=random.choice(card_list2)
    D1=random.choice(card_list2)
    D2=random.choice(card_list2)
    card_list2.remove(P1)
    card_list2.remove(P2)
    card_list2.remove(D1)
    card_list2.remove(D2)



    Your_hand=[P1,P2]

    Dealers_hand=[D1,D2]
    

    time.sleep(1.5)
    print(f"Your hand is ---> {colourful_writer(Your_hand[0],PURPLE)} and {colourful_writer(Your_hand[1],PURPLE)}")
    print("")
    time.sleep(2)
    print(f"Dealer has ---> {colourful_writer((D1),ORANGE)} and {colourful_writer("a face-down card",ORANGE)}")
    print("")
    time.sleep(2)

    if ("A" in Dealers_hand[0]):
        answer=input("Do you want insurance?(y/n)")
        while answer not in ("y","n"):
            print("Only letters 'y' for 'yes' and 'n' for 'no' are allowed ")
            answer=input("Do you want insurance?(y/n)")
        if answer == "n":
            print("Thats what I thought")
        else:
            joke=random.randint(1,100)
            if joke == 27:
                print("You're probably the only person who will see this, I love you so much, Whoever you are")
            else:
                print("No you dont want insurance :) ")

    Dealer_blackjack=0

    if ("A" in Dealers_hand[0]) or ("A" in  Dealers_hand[1]):
        if value_checker_for_lists(Dealers_hand)==11:
            Dealer_blackjack=1

    

    Player_blackjack=0

    if ("A" in Your_hand[0]) or ("A" in  Your_hand[1]):
        if value_checker_for_lists(Your_hand)==11:
            print("You have Blackjack,dealer will reveal their cards now!")
            time.sleep(2)
            Player_blackjack=1

    


    if Player_blackjack!=1:
        Hs=input("Hit or stand?(h/s)")
        while Hs not in ("h","s"):
            print("Only letters 'h' for 'hit' and 's' for 'stand' are allowed ")
            Hs=input("Hit or stand?(h/s)")
        print("")
    else:
        Hs="s"

    

    
    
    


    bust=0
    while Hs== "h":
        P3=random.choice(card_list2)
        card_list2.remove(P3)
        Your_hand.append(P3)
        print("Now,You hand is --->",end="")
        advanced_colourer_for_lists(Your_hand,PURPLE)#Before this one existed I had to use *Your_hand and I hated it, I now created this
        print("")
        time.sleep(1.5)
        s2=value_checker_for_lists(Your_hand)
        if did_I_bust(s2) == 0:
            print("You busted(You went over 21),House won")
            time.sleep(2)
            bust=1
            w=0
            break
        if s2==21:
            print("You have 21, dealer will reveal their hand now")
            print("")
            time.sleep(2)
            break

        notasked=0
        if s2 ==11:
            for i in range(len(Your_hand)):
                if "A" in Your_hand[i]:
                    print("You have 21, dealer will reveal their hand now")
                    print("")
                    time.sleep(2)
                    notasked=1
        if notasked==1:
            break
        
        

            
        Hs=input("Hit or stand?(h/s)")
        while Hs not in ("h","s"):
            print("Only letters 'h' for 'hit' and 's' for 'stand' are allowed ")
            Hs=input("Hit or stand?(h/s)")
        print("")

    a_list_of_values=[]

    for i in Your_hand:
        a=value_checker(i)
        a_list_of_values.append(a)

    func()

    a_list_of_values_for_dealer=[]

    a_list_of_values_for_dealer=value_checker_for_dealer()

    print("Dealer originally had --->",end="")
    advanced_colourer_for_lists(clean_dealers_hand(),ORANGE)
    time.sleep(2)

    if Player_blackjack==1:
        if Dealer_blackjack==1:
            time.sleep(1.5)
            print("Double blackjack,Rare sight to see isn' it :)")
            return 1/2
        else:
            print("Dealer doesn't have a blackjack, You won")
            time.sleep(1.5)
            print(f"Here is the {colourful_writer(str(gambled_money)+"$",GREEN)} bucks you won")
            return 1
    
        
    
    #Whole dealers mechanic needs  to be changed to fit the A stuff(while bust condition would still be present cuz those stuff would be ignored if you bust ofc)
    while bust != 1:
        if fun() >= 22:
            if "L" in Dealers_hand:
                if "N" not in Dealers_hand:
                    Dealers_hand.append("N")
                else:
                    print("Dealer Busted,Player won")
                    time.sleep(1.5)
                    bust = 1
                    w=1
                    break
            else:
                print("Dealer Busted,Player won")
                time.sleep(1.5)
                bust = 1
                w=1
                break
        elif fun() >= 17:
            print("Dealer finally has got --->",end="")
            advanced_colourer_for_lists(clean_dealers_hand(),ORANGE)
            time.sleep(1.5)
            break
        else:
            D3=random.choice(card_list2)
            card_list2.remove(D3)
            Dealers_hand.append(D3)
            print("Dealer has got --->",end="")
            advanced_colourer_for_lists(clean_dealers_hand(),ORANGE)
            time.sleep(2)

            a_list_of_values_for_dealer= value_checker_for_dealer()

    if bust!=1:
        w=comparison_func()



    if w == 1:
        time.sleep(1.5)
        print(f"Here is the {colourful_writer(str(gambled_money)+"$",GREEN)} bucks you won")
    elif w==1/2:
        time.sleep(1.5)
        print("You got your money back")
    
    else:
        time.sleep(1.5)
        print(f"Thanks for gambling your {colourful_writer(str(gambled_money)+"$",RED)} bucks away")


    return w


while (currently_has !=0):
    Cutcard=random.randint(234,252)#%75 to %80 by convention
    if len(card_list2)<312-Cutcard:
        print(colourful_writer("Cutcard",RED),end="")
        print(" has been reached, Now the deck will be suffled to its original form")
        print("")
        time.sleep(1)
        print("Shuffling")
        time.sleep(1)
        print("")
        print("Shuffling")
        print("")
        time.sleep(1)
        print("Done!")
        card_list2=notchangedcard_list2

    money()
    do_you_have()
    if d==1:
         break

    w=game()
    if w ==1:
       currently_has=currently_has+(gambled_money)
    elif w==1/2:
        print("",end="")
    else:
       currently_has=currently_has-(gambled_money)
    print("")
    print(f"You currently have {colourful_writer(str(currently_has)+"$",GREEN)}")

    money_profile.append(currently_has)
    joke2+=1
    

    

print("This was how your money progressed after all that gambling", money_profile)
time.sleep(3)
print("You can check your progress in the next graph as well(A new screen should pop out in your task bar,check it)")
time.sleep(2)
profile_drawer_of_turtle(money_profile)
tmp=money_profile.copy()
tmp.sort()
print(f"Your highest score was { colourful_writer(str(tmp[-1])+"$",GREEN)}")
if d==1:
    print(f"You cashed out with { colourful_writer(str(money_profile[-1])+"$",GREEN) } ")
    if money_profile[-1]>1000:
        print("Thats more than what you had in the beginning")
    elif money_profile[-1]==1000:
        print("No profit,no loss. Perfection")
    else:
        print("Unfortunately, you have less than what you came here with")
else:
    print("You ran out of money, Better luck next time")
time.sleep(1)
print("")
print("You can play another round by starting the code again :)") 

#print(card_list2) It actually takes the cards from the list now
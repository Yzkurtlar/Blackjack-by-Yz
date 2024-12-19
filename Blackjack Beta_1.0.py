import time
import sys
import threading

def slow_print(text, char_delay=0.075, line_delay=1.0, comma_delay=0.3):
    
    lines = text.splitlines()  


    stop_thread = False

    def check_skip():
        nonlocal stop_thread
        input("Press Enter to skip if you have already listened the rules once...\n")
        stop_thread = True

    listener = threading.Thread(target=check_skip, daemon=True)
    listener.start()
    time.sleep(4)

    for line in lines:
        for char in line:
            if stop_thread:  # If Enter is pressed, print the rest and break
                print("")
                print("Welcome back then")
                return ""
            sys.stdout.write(char)
            sys.stdout.flush()
            if char == ',':
                time.sleep(comma_delay)
            else:
                time.sleep(char_delay)
            
        print()
        time.sleep(line_delay)

a="""
Welcome to Blackjack Beta 1.0 by Yz. Since its a beta I couldnt add split and double down mechanics so I apologize in advance
You are playing with a 6 shoe deck which means you can have the same exact cards 6 times before it runs out from the deck
Dealer will STAY in soft 17 to give player a slight edge,so be grateful :)
The game only ends when you run out of money, You cant cash out unfortunately :)
I'd add your 'username' to Beta2.0 if you manage to get aa high score in my game
Lastly, Enjoy and text me if you encounter a bug :)
"""
slow_print(a)

suits_list=["Spades","Diamonds","Hearts","Clubs"]
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

starting_money=1000
currently_has=1000

print("You have "+ str(starting_money)+"$ to begin with")

def money():
        global gambled_money
        try:
            gambled_money=int(input("How much value you wanna gamble?"))
            if gambled_money<=0:
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
        print("ALL IN")
    else:
         print("Gambling,Gambling,Gambling")



def game():
    #do blackjack(Will be a 6 shoe deck)
    #Stand soft 17
    import random
    
    

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
            return 1
        else:
            print("you lost,Dealers hand was closer to 21")
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
    print("Your hand is --->",Your_hand[0],"and", Your_hand[1])
    print("")
    print("Dealer has "+D1+" and a face-down card")
    print("")
    Hs=input("Hit or stand?(h/s)")
    while Hs not in ("h","s"):
        print("Only letters 'h' and 's' are allowed ")
        Hs=input("Hit or stand?(h/s)")
    print("")


    bust=0
    while Hs== "h":
        P3=random.choice(card_list2)
        card_list2.remove(P3)
        Your_hand.append(P3)
        print("Now,You hand is --->",end="")
        print(*Your_hand,sep=" and ")
         # I'm glad that I learnt this with elif
        s2=value_checker_for_lists(Your_hand)
        s=value_checker_for_lists(Dealers_hand)
        if did_I_bust(s2) == 0:
            print("You busted(You went over 21),House won")
            bust=1
            w=0
            break
            
        Hs=input("Hit or stand?(h/s)")
        while Hs not in ("h","s"):
            print("Only letters 'h' and 's' are allowed ")
            Hs=input("Hit or stand?(h/s)")
        print("")

    a_list_of_values=[]

    for i in Your_hand:
        a=value_checker(i)
        a_list_of_values.append(a)

    func()

    a_list_of_values_for_dealer=[]

    a_list_of_values_for_dealer=value_checker_for_dealer()

    p=0
    print("Dealer originally had ",end="")
    print(*clean_dealers_hand(),sep=" and ")
    #Whole dealers mechanic needs  to be changed to fit the A stuff(while bust condition would still be present cuz those stuff would be ignored if you bust ofc)
    while bust != 1:
        if fun() >= 22:
            if "L" in Dealers_hand:
                if "N" not in Dealers_hand:
                    Dealers_hand.append("N")
                else:
                    print("House Busted,Player won")
                    bust = 1
                    w=1
                    break
            else:
                print("House Busted,Player won")
                bust = 1
                w=1
                break
        elif fun() >= 17:
            print("Dealer finally has got ",end="")
            print(*clean_dealers_hand(),sep=" and ")
            break
        else:
            D3=random.choice(card_list2)
            card_list2.remove(D3)
            Dealers_hand.append(D3)
            print("Dealer has got ",end="")
            print(*clean_dealers_hand(),sep=" and ")

            a_list_of_values_for_dealer= value_checker_for_dealer()

    if bust!=1:
        w=comparison_func()



    if w == 1:
        print("")
        print("Here is the "+ str((gambled_money)) + " bucks you won")
    else:
        print("")
        print("Thanks for gambling your "+str(gambled_money)+" bucks away")


    return w


while currently_has !=0:
    money()
    do_you_have()
    w=game()
    if w ==1:
       currently_has=currently_has+(gambled_money)
    else:
       currently_has=currently_has-(gambled_money)
    print("You currently have "+str(currently_has)+"$")

    
print("You ran out of money, Better luck next time")

#print(card_list2) It actually takes the cards from the list now
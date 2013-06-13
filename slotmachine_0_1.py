# Source File Name: slotmachine.py
# Author's Name: Rubyta Herwinda
# Date Last Modified: Friday June 7, 2013
""" 
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module

  Version: 0.1 - * Created Back end functions for the slot machine program Reels, pullthehandle, and
                 is_number (a validation function).
                 * Text output provides debugging information to check if the Slot Machine program does
                 what it's supposed to do.
                 * Used research from the internet to set the Reels function to simulate basic slot reels
"""

# import statements
import random
from Tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import sys

class SlotMachine():
    def __init__(self):
        base = Tk()
        base.title = ("Disney Slot Machine")
        self.canvas = Canvas(base, width=1000, height=800)
        self.canvas.grid(column=0, row=0)
        #spin button
        button = Button(root, text="Spin", width=20, command = self.spin)
        button.grid(column=0, row=25)
        #bet button
        button1 = Button(root, text="Bet", width=20, command = self.spin)
        button.grid(column=1, row=25)
        #reset button
        button2 = Button(root, text="Reset", width=20, command = self.spin)
        button.grid(column=2, row=25)
        #quit button
        button = Button(root, text="Quit", width=20, command = self.spin)
        button.grid(column=3, row=25)
        #label for player money
        Currentmoney = StringVar(None)
        DollarEntry = Entry(base, textvariable=Currentmoney)
        DollarEntry.pack()
        #label for jackpot
        Currentjackpot = StringVar(None)
        JackpotEntry = Entry(base, textvariable=Currentjackpot)
        JackpotEntry.pack()
        #label for bet
        Currentbet = StringVar(None)
        BetEntry = Entry(base, textvariable=Currentbet)
        BetEntry.pack()
        
        self.alive = True
        base.protocol("WM_DELETE_WINDOW", self.die)
        base.mainloop()

        def Reels():
            
            """define the wheels image"""
            img = Image.open("slot2.jpeg")
            wheelwidth = img.size[0]
            wheelheight = img.size[1]
            showsize = 500
            speed = 3
            bx = 250 #coordinate x of the box
            by = 250 #coordinate y of the box
            numberofspin = 50
            cycle_period = 3
            
            """define the image inside the wheel"""
            disney_img1 = ImageTk.PhotoImage(mickey.jpeg)
            disney_img2 = ImageTk.PhotoImage(minnie.jpg)
            disney_img3 = ImageTk.PhotoImage(daisy.jpg)
            disney_img4 = ImageTk.PhotoImage(donald.jpg)
            disney_img5 = ImageTk.PhotoImage(goofy.jpg)
            disney_img6 = ImageTk.PhotoImage(pluto.jpg)
            disney_img7 = ImageTk.PhotoImage(clarabelle.jpg)
            disney_img8 = ImageTk.PhotoImage(pete.jpg)
            img1id = self.canvas.create_image(bx, by + showsize, image=disney_img1)
            img2id = self.canvas.create_image(bx, by + showsize + wheelheight, image=disney_img2)
            img3id = self.canvas.create_image(bx, by + showsize + wheelheight, image=disney_img3)
            img4id = self.canvas.create_image(bx, by + showsize + wheelheight, image=disney_img4)
            img5id = self.canvas.create_image(bx, by + showsize + wheelheight, image=disney_img5)
            img6id = self.canvas.create_image(bx, by + showsize + wheelheight, image=disney_img6)
            img7id = self.canvas.create_image(bx, by + showsize + wheelheight, image=disney_img7)
            img8id = self.canvas.create_image(bx, by + showsize + wheelheight, image=disney_img8)
            
            mickey = self.canvas.show(img1id)
            minnie = self.canvas.show(img2id)
            daisy = self.canvas.show(img3id)
            donald = self.canvas.show(img4id)
            goofy = self.canvas.show(img5id)
            pluto = self.canvas.show(img6id)
            clarabelle = self.canvas.show(img7id)
            pete = self.canvas.show(img8id)
            
            """ When this function is called it determines the Bet_Line results. e.g. Bar - Orange - Banana """
        
            # [0]Fruit, [1]Fruit, [2]Fruit
            Bet_Line = [" "," "," "]
            Outcome = [0,0,0]
    
        # Spin those reels
            for spin in range(3):
                Outcome[spin] = random.randrange(1,65,1)
            # Spin those Reels!
                if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
                    Bet_Line[spin] = mickey
                if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
                    Bet_Line[spin] = minnie
                if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
                    Bet_Line[spin] = daisy
                if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
                    Bet_Line[spin] = donald
                if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
                    Bet_Line[spin] = goofy
                if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
                    Bet_Line[spin] = pluto
                if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
                    Bet_Line[spin] = clarabelle 
                if Outcome[spin] == 64:                         # 1.56%  Chance
                    Bet_Line[spin] = pete
    
                return Bet_Line

    def is_number(Bet):
        """ This function Checks if the Bet entered by the user is a valid number """
        try:
            int(Bet)
            return True
        except ValueError:
            print("Please enter a valid number or Q to quit")
        return False

    def pullthehandle(Bet, Player_Money, Jack_Pot):
        """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
        Player_Money -= Bet
        Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
        win = False
        Disney_Reel = Reels()
        Disney = Disney_Reel[0] + " - " + Disney_Reel[1] + " - " + Disney_Reel[2]
    
        # Match 3
        if Disney_Reel.count(mickey) == 3:
            winnings,win = Bet*20,True
        elif Disney_Reel.count(minnie) == 3:
            winnings,win = Bet*30,True
        elif Disney_Reel.count(daisy) == 3:
            winnings,win = Bet*40,True
        elif Disney_Reel.count(donald) == 3:
            winnings,win = Bet*100,True
        elif Disney_Reel.count(goofy) == 3:
            winnings,win = Bet*200,True
        elif Disney_Reel.count(pluto) == 3:
            winnings,win = Bet*300,True
        elif Disney_Reel.count(Pete) == 3:
            print("Lucky Seven!!!")
            winnings,win = Bet*1000,True
        # Match 2
        elif Disney_Reel.count("Blank") == 0:
            if Disney_Reel.count(mickey) == 2:
                winnings,win = Bet*2,True
            if Disney_Reel.count(minnie) == 2:
                winnings,win = Bet*2,True
            elif Disney_Reel.count(daisy) == 2:
                winnings,win = Bet*3,True
            elif Disney_Reel.count(donald) == 2:
                winnings,win = Bet*4,True
            elif Disney_Reel.count(goofy) == 2:
                winnings,win = Bet*5,True
            elif Disney_Reel.count(clarabelle) == 2:
                winnings,win = Bet*10,True
            elif Disney_Reel.count(pete) == 2:
                winnings,win = Bet*20,True
    
            # Match Lucky Seven
            elif Disney_Reel.count(pete) == 1:
                winnings, win = Bet*10,True
            
            else:
                winnings, win = Bet*2,True
        if win:    
            print(Disney + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
            Player_Money += int(winnings)
    
            # Jackpot 1 in 450 chance of winning
            jackpot_try = random.randrange(1,51,1)
            jackpot_win = random.randrange(1,51,1)
            if  jackpot_try  == jackpot_win:
                print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
                Jack_Pot = 500
            elif jackpot_try != jackpot_win:
                print ("You did not win the Jackpot this time. \nPlease try again ! \n")
        # No win
        else:
            print(Disney + "\nPlease try again. \n")
    
        return Player_Money, Jack_Pot, win

    def main():
        """ The Main function that runs the game loop """
        # Initial Values
        Player_Money = 1000
        Jack_Pot = 500
        Turn = 1
        Bet = 0
        Prev_Bet=0
        win_number = 0
        loss_number = 0
    
        # Flag to initiate the game loop
        KeepGoing = True
    
        while KeepGoing == True:
            win = 0
            # Give the player some money if he goes broke
            if Player_Money <1:
                input("You have no more money. Here is $500 \nPress Enter\n")
                Player_Money = 500
        
                # User Input
            Prompt = raw_input(" Place Your Bet ! \n Jackpot $ " + str(Jack_Pot) + "\n Money $ " + str(Player_Money) + "\n Q = quit \n")
            if Prompt  == "q" or Prompt  == "Q":
                KeepGoing = False
                break
        
            if Prompt == "" and Turn >1:
                Bet = Prev_Bet
                print("Using Previous Bet")
                if Bet > Player_Money:
                    print("Sorry, you only have $" + str(Player_Money) + " \n")
                elif Bet <= Player_Money:
                    Turn +=1
                    Prev_Bet = Bet
                    Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
            elif is_number(Prompt ):
                Bet = int(Prompt )
                # not enough money
                if Bet > Player_Money:
                    print("Sorry, you only have $" + str(Player_Money) + " \n")
                
                # Let's Play
                elif Bet <= Player_Money:
                    Turn +=1
                    Prev_Bet = Bet
                    Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
                # determine win/loss ratio for debugging purposes
                if win:
                    win_number += 1
                else:
                    loss_number += 1
                    win_ratio = "{:.2%}".format(win_number / Turn)
                    print("Wins: " + str(win_number) + "\nLosses: " + str(loss_number) + "\nWin Ratio: " + win_ratio + "\n")           
                
    
        #The End
        print("- Program Terminated -")
    
    if __name__ == "__main__": main()

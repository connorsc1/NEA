# importing necessary libraries 

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image, ImageTk
import json
import random

# main app

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = Font(family='Secular One')

        # creating the container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # adding navigation
        self.frames = {}
        for F in (opening, login, signup, mainmenu, settings, game):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("opening")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class opening(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame
        self.configure(background="#333333")

        # icon inside opening screen
        self.icon_text = tk.Label(self, text='21', font=("Secular One", 200),
                                  bg="#333333", fg="#FFFFFF")
        self.icon_text.pack(pady=20)

        # log in button
        self.login_btn = tk.PhotoImage(file='assets/buttons/login.png')
        ttk.login = tk.Button(self, image=self.login_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=lambda: controller.show_frame("login"))
        ttk.login.pack()

        # sign up button
        self.signup_btn = tk.PhotoImage(file='assets/buttons/signup.png')
        ttk.signup = tk.Button(self, image=self.signup_btn, bg="#333333", activebackground="#333333",
                               borderwidth=0, command=lambda: controller.show_frame("signup"))
        ttk.signup.pack(pady=10)

        # quit button
        self.quit_btn = tk.PhotoImage(file='assets/buttons/quit.png')
        ttk.quitb = tk.Button(self, image=self.quit_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=quit)
        ttk.quitb.pack()


class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame
        self.configure(background="#333333")

        # invisible label
        ilabel = tk.Label(self, text="", bg="#333333")
        ilabel.pack(side="top", fill="x", pady=120)

        login_text = Label(self, text='Log in', font=("Secular One", 50),
                           bg="#333333", fg="#FFFFFF")
        login_text.pack(pady=20)

        # input fields
        def on_entry_click_username(event):
            if username_entry.cget('fg') == 'grey':
                # delete all the text in the entry
                username_entry.delete(0, "end")
                username_entry.insert(0, '')
                username_entry.config(fg='black')

        def on_focusout_username(event):
            if username_entry.get() == '':
                username_entry.insert(0, 'Username')
                username_entry.config(fg='grey')

        username_entry = Entry(
            self, width=17, bg="#D9D9D9", font=("Secular One", 28))
        username_entry.insert(0, 'Username')
        username_entry.bind('<FocusIn>', on_entry_click_username)
        username_entry.bind('<FocusOut>', on_focusout_username)
        username_entry.config(fg='grey')
        username_entry.pack()

        def on_entry_click_password(event):
            password_entry.config(show='*')
            if password_entry.cget('fg') == 'grey':
                password_entry.delete(0, "end")
                password_entry.insert(0, '')
                password_entry.config(fg='black')

        def on_focusout_password(event):
            if password_entry.get() == '':
                password_entry.insert(0, 'Password')
                password_entry.config(fg='grey', show='')

        password_entry = Entry(
            self, width=17, bg="#D9D9D9", font=("Secular One", 28))
        password_entry.insert(0, 'Password')
        password_entry.bind('<FocusIn>', on_entry_click_password)
        password_entry.bind('<FocusOut>', on_focusout_password)
        password_entry.config(fg='grey')
        password_entry.pack(pady=10)

        # user authentication
        incorrect = Label(self, text='', font=("Secular One", 20),
                          bg="#333333", fg="red")

        def log_in():
            if username_entry.get() != "Username":
                with open("info.txt") as f:
                    data = f.read()
                info = json.loads(data)
                usern = username_entry.get()
                passw = password_entry.get()
                incorrect.config(text='')
                if usern.lower() in info and info[usern.lower()] == passw:
                    # make it go to the main menu
                    controller.show_frame("mainmenu")
                else:
                    incorrect.config(text='Incorrect, try again')
                    incorrect.pack(pady=20)
            else:
                incorrect.config(text='No Input')
                incorrect.pack(pady=20)

        # enter button
        self.enter_btn = tk.PhotoImage(file='assets/buttons/enter.png')
        ttk.enter = tk.Button(self, image=self.enter_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=log_in).pack()

        # back button
        self.back_btn = tk.PhotoImage(file='assets/buttons/back.png')
        ttk.back = tk.Button(self, image=self.back_btn, bg="#333333", activebackground="#333333",
                             borderwidth=0, command=lambda: controller.show_frame("opening"))
        ttk.back.pack(anchor="w", side="bottom")


class signup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame
        self.configure(background="#333333")

        # invisible label
        ilabel = tk.Label(self, text="", bg="#333333")
        ilabel.pack(side="top", fill="x", pady=120)

        signup_text = Label(self, text='Sign up', font=("Secular One", 50),
                            bg="#333333", fg="#FFFFFF")
        signup_text.pack(pady=20)

        # input fields
        def on_entry_click_username(event):
            if username_entry.cget('fg') == 'grey':
                username_entry.delete(0, "end")
                username_entry.insert(0, '')
                username_entry.config(fg='black')

        def on_focusout_username(event):
            if username_entry.get() == '':
                username_entry.insert(0, 'Username')
                username_entry.config(fg='grey')

        username_entry = Entry(
            self, width=17, bg="#D9D9D9", font=("Secular One", 28))
        username_entry.insert(0, 'Username')
        username_entry.bind('<FocusIn>', on_entry_click_username)
        username_entry.bind('<FocusOut>', on_focusout_username)
        username_entry.config(fg='grey')
        username_entry.pack()
        def on_entry_click_password(event):
            password_entry.config(show='*')
            if password_entry.cget('fg') == 'grey':
                # delete all the text in the entry
                password_entry.delete(0, "end")
                password_entry.insert(0, '')
                password_entry.config(fg='black')

        def on_focusout_password(event):
            if password_entry.get() == '':
                password_entry.insert(0, 'Password')
                password_entry.config(fg='grey', show='')

        password_entry = Entry(
            self, width=17, bg="#D9D9D9", font=("Secular One", 28))
        password_entry.insert(0, 'Password')
        password_entry.bind('<FocusIn>', on_entry_click_password)
        password_entry.bind('<FocusOut>', on_focusout_password)
        password_entry.config(fg='grey')
        password_entry.pack(pady=10)

        # user auth
        incorrect = Label(self, text='', font=("Secular One", 20),
                          bg="#333333", fg="red")

        def sign_up():
            if username_entry.get() != "Username":
                with open("info.txt") as f:
                    data = f.read()
                info = json.loads(data)
                usern = username_entry.get()
                passw = password_entry.get()
                incorrect.config(text='')
                if usern.lower() in info:
                    incorrect.config(text='Username is taken, try again')
                    incorrect.pack(pady=20)
                else:
                    f = open("info.txt", "r+")
                    lines = f.readlines()
                    f.seek(0)
                    f.truncate()
                    f.writelines(lines[:-1])
                    f.write(f',"{usern.lower()}" : "{passw}"\n')
                    f.write("}")
                    controller.show_frame("login")
            else:
                incorrect.config(text='No Input')
                incorrect.pack(pady=20)

        # submit button
        self.submit_btn = tk.PhotoImage(file='assets/buttons/submit.png')
        ttk.enter = tk.Button(self, image=self.submit_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=sign_up)
        ttk.enter.pack()

        # back button
        self.back_btn = tk.PhotoImage(file='assets/buttons/back.png')
        ttk.back = tk.Button(self, image=self.back_btn, bg="#333333", activebackground="#333333",
                             borderwidth=0, command=lambda: controller.show_frame("opening"))
        ttk.back.pack(anchor="w", side="bottom")


class mainmenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame
        self.configure(background="#333333")

        # invisible label
        ilabel = tk.Label(self, text="", bg="#333333")
        ilabel.pack(side="top", fill="x", pady=200)

        # play button
        self.play_btn = tk.PhotoImage(file='assets/buttons/play.png')
        ttk.play = tk.Button(self, image=self.play_btn, bg="#333333", activebackground="#333333",
                             borderwidth=0, command=lambda: controller.show_frame("game"))
        ttk.play.pack()

        # settings button
        self.settings_btn = tk.PhotoImage(file='assets/buttons/settings.png')
        ttk.settings = tk.Button(self, image=self.settings_btn, bg="#333333", activebackground="#333333",
                                 borderwidth=0, command=lambda: controller.show_frame("settings"))
        ttk.settings.pack(pady=10)

        # quit button
        self.quit_btn = tk.PhotoImage(file='assets/buttons/quit2.png')
        ttk.quitb = tk.Button(self, image=self.quit_btn, bg="#333333", activebackground="#333333",
                              borderwidth=0, command=quit)
        ttk.quitb.pack()


class settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame
        self.configure(background="#333333")

        # maybe use global variables to tell the game what settings a user has used
        # if they have solo they are alone
        # if they have chosen hard they use more decks
        # if they choose easy its just one deck
        # if they choose multi then there could be 7 players?


class game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame
        self.configure(background="#35654d")
        self.configure(pady=20)

        # dealer frame
        dealer_frame = tk.LabelFrame(
            self, text='Dealer', bd=0, bg='#35654d', fg='#FFFFFF')
        dealer_frame.pack(ipadx=20)
       
        # player frame
        player_frame = LabelFrame(
            self, text='Player', bd=0, bg='#35654d', fg='#FFFFFF')
        player_frame.pack(ipadx=20)

        # cards in dealer frame
        dealer_label_1 = Label(dealer_frame, text='', bd=0, bg='#35654d')
        dealer_label_1.grid(row=0, column=0, padx=20, pady=20)

        dealer_label_2 = Label(dealer_frame, text='', bd=0, bg='#35654d')
        dealer_label_2.grid(row=0, column=1, padx=20, pady=20)

        dealer_label_3 = Label(dealer_frame, text='', bd=0, bg='#35654d')
        dealer_label_3.grid(row=0, column=2, padx=20, pady=20)

        dealer_label_4 = Label(dealer_frame, text='', bd=0, bg='#35654d')
        dealer_label_4.grid(row=0, column=3, padx=20, pady=20)

        dealer_label_5 = Label(dealer_frame, text='', bd=0, bg='#35654d')
        dealer_label_5.grid(row=0, column=4, padx=20, pady=20)

        # cards in player frame
        player_label_1 = Label(player_frame, text='', bd=0, bg='#35654d')
        player_label_1.grid(row=1, column=0, padx=20, pady=20)

        player_label_2 = Label(player_frame, text='', bd=0, bg='#35654d')
        player_label_2.grid(row=1, column=1, padx=20, pady=20)

        player_label_3 = Label(player_frame, text='', bd=0, bg='#35654d')
        player_label_3.grid(row=1, column=2, padx=20, pady=20)

        player_label_4 = Label(player_frame, text='', bd=0, bg='#35654d')
        player_label_4.grid(row=1, column=3, padx=20, pady=20)

        player_label_5 = Label(player_frame, text='', bd=0, bg='#35654d')
        player_label_5.grid(row=1, column=4, padx=20, pady=20)


        # testing for blackjack after shuffle
        def blackjack_test(player):
            global player_total, dealer_total, player_score
            # keep track of total score of player / dealer
            player_total = 0
            dealer_total = 0

            if not first:
                if player == "dealer":
                    if len(dealer_score) == 2:
                        if dealer_score[0] + dealer_score[1] == 21:
                            # update the status
                            blackjack_status["dealer"] = "yes"

                            # messagebox.showinfo('Blackjack', 'Dealer Wins!')
                            # disable the butons for players
                            # cardb.config(state='disabled')
                            # standb.config(state='disabled')

                    else: 
                        # loop through dealer score list and add up cards
                        for score in dealer_score: 
                            # add score
                            dealer_total += score
                        if dealer_total == 21:
                            blackjack_status["dealer"] = "yes"
                        
                        elif dealer_total > 21:
                            # check if ace needs to be converted
                            for card_num, card in enumerate(dealer_score):
                                if card == 11:
                                    dealer_score[card_num] = 1

                                    # Clear dealer total and recalc with ace being 1
                                    dealer_total = 0
                                    for score in dealer_score:
                                        # Add score
                                        dealer_total += score
                                    
                                    # check for over 21 after ace is converted
                                    if dealer_total > 21:
                                        blackjack_status["dealer"] = "bust"
                            else:
                                if dealer_total == 21:
                                    blackjack_status["dealer"] = "yes"
                                if dealer_total > 21:
                                    blackjack_status["dealer"] = "bust"

                if player == "player":
                    if len(player_score) == 2:
                        if player_score[0] + player_score[1] == 21:
                            # update the status
                            blackjack_status["player"] = "yes"

                            # messagebox.showinfo('Blackjack', 'You have won!')
                            # disable the buttons for players
                            # cardb.config(state='disabled')
                            # standb.config(state='disabled')
                    else: 
                        # loop through player score list and add up cards
                        for score in player_score: 
                            # add score
                            player_total += score

                        if player_total == 21:
                            blackjack_status["player"] = "yes"
                        
                        elif player_total > 21:
                            # check if ace needs to be converted
                            for card_num, card in enumerate(player_score):
                                if card == 11:
                                    player_score[card_num] = 1

                                    # Clear player total and recalc with ace being 1
                                    player_total = 0
                                    for score in player_score:
                                        # Add score
                                        player_total += score
                                    
                                    # check for over 21 after ace is converted
                                    if player_total > 21:
                                        blackjack_status["player"] = "bust"
                            else:
                                if player_total == 21:
                                    blackjack_status["player"] = "yes"
                                if player_total > 21:
                                    blackjack_status["player"] = "bust"
                
                if len(dealer_score) == 2 and len(player_score) == 2:
                    # check for tie
                    if blackjack_status["dealer"] == "yes" and blackjack_status["player"] == "yes":
                        messagebox.showinfo('Push', 'Its a tie!')
                        # disable the butons for players
                        cardb.config(state='disabled')
                        standb.config(state='disabled')
                    
                    # check for dealer win
                    elif blackjack_status["dealer"] == "yes":
                        messagebox.showinfo('Blackjack', 'Dealer Wins!')
                        # disable the butons for players
                        cardb.config(state='disabled')
                        standb.config(state='disabled')
                    
                    # check for player win
                    elif blackjack_status["player"] == "yes":
                        messagebox.showinfo('Blackjack', 'You have won!')
                        # disable the buttons for players
                        cardb.config(state='disabled')
                        standb.config(state='disabled')
                
                # checking for 21 after hit me (more than 2 cards)
                else:
                    # check for tie
                    if blackjack_status["dealer"] == "yes" and blackjack_status["player"] == "yes":
                        messagebox.showinfo('Push', 'Its a tie!')
                        # disable the butons for players
                        cardb.config(state='disabled')
                        standb.config(state='disabled')
                    
                    # check for dealer win
                    elif blackjack_status["dealer"] == "yes":
                        messagebox.showinfo('Blackjack', 'Dealer Wins!')
                        # disable the butons for players
                        cardb.config(state='disabled')
                        standb.config(state='disabled')
                    
                    # check for player win
                    elif blackjack_status["player"] == "yes":
                        messagebox.showinfo('Blackjack', 'You have won!')
                        # disable the buttons for players
                        cardb.config(state='disabled')
                        standb.config(state='disabled')
                
                # check for player bust
                if blackjack_status["player"] == "bust":
                    messagebox.showinfo('Player bust', f'You lose - {player_total}')
                    # disable the buttons for players
                    cardb.config(state='disabled')
                    standb.config(state='disabled')
            else:
                pass

        # resize card images
        def resize(card):
            # open the image
            our_card_img = Image.open(card)

            # Resizing it
            our_card_resized_image = our_card_img.resize((150, 218))

            # output card
            global our_card_image
            our_card_image = ImageTk.PhotoImage(our_card_resized_image)
            return our_card_image

        # shuffle function
        def shuffle():
            # used to check if the dealer and player have won, if they both win it is a tie
            global blackjack_status, player_total, dealer_total
            blackjack_status = {"dealer":"no", "player":"no"}
            
            # keep track of total score of player / dealer
            player_total = 0
            dealer_total = 0

            # Enable buttons from disbaling on blackjack
            cardb.config(state='normal')
            standb.config(state='normal')

            # Clear old cards from previous games
            dealer_label_1.config(image='')
            dealer_label_2.config(image='')
            dealer_label_3.config(image='')
            dealer_label_4.config(image='')
            dealer_label_5.config(image='')

            player_label_1.config(image='')
            player_label_2.config(image='')
            player_label_3.config(image='')
            player_label_4.config(image='')
            player_label_5.config(image='')

            suits = ['diamonds', 'clubs', 'hearts', 'spades']
            values = range(1, 14)
            # 1 is ace, 11 = jack, 12 = queen, 13 = king

            # defining empty deck
            global deck
            deck = []

            # creating full deck
            for suit in suits:
                for value in values:
                    deck.append(f'{value}_of_{suit}')

            # creating players
            global player, dealer, dealer_spot, player_spot, dealer_score, player_score
            dealer = []
            player = []
            dealer_spot = 0
            player_spot = 0
            dealer_score = []
            player_score = []

            # Shuffle 2 cards for dealer and player

            player_hit()
            dealer_hit()
            player_hit()
            dealer_hit()

        def dealer_hit():
            global dealer_spot
            global player_total, dealer_total, player_score, dealer_score

            if dealer_spot <= 5:
                try:
                    # get dealer card
                    dealer_card = random.choice(deck)
                    deck.remove(dealer_card)
                    # append card to dealer list
                    dealer.append(dealer_card)
                    # append card to score list and convert values to real blackjack values
                    numberofdealercard = int(dealer_card.split("_", 1)[0]) # Find the number of the card
                    if numberofdealercard == 1: # Changing Ace to 11
                        dealer_score.append(11)
                    elif numberofdealercard == 11 or numberofdealercard == 12 or numberofdealercard == 13: #Changing jack, queen and king to value 10 (like in blackjack)
                        dealer_score.append(10)
                    else:
                        dealer_score.append(numberofdealercard)


                    # show card on screen
                    global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5

                    if dealer_spot == 0:
                        # Resize card
                        dealer_image1 = resize(f'assets/cards/{dealer_card}.png')
                        # Output card
                        dealer_label_1.config(image=dealer_image1)
                        #print(f'{len(deck)} cards left')
                        # Increment dealer spot counter
                        dealer_spot += 1
                    elif dealer_spot == 1:
                        # Resize card
                        dealer_image2 = resize(f'assets/cards/{dealer_card}.png')
                        # Output card
                        dealer_label_2.config(image=dealer_image2)
                        # Increment dealer spot counter
                        dealer_spot += 1
                    elif dealer_spot == 2:
                        # Resize card
                        dealer_image3 = resize(f'assets/cards/{dealer_card}.png')
                        # Output card
                        dealer_label_3.config(image=dealer_image3)
                        # Increment dealer spot counter
                        dealer_spot += 1
                    elif dealer_spot == 3:
                        # Resize card
                        dealer_image4 = resize(f'assets/cards/{dealer_card}.png')
                        # Output card
                        dealer_label_4.config(image=dealer_image4)
                        # Increment dealer spot counter
                        dealer_spot += 1
                    elif dealer_spot == 4:
                        # Resize card
                        dealer_image5 = resize(f'assets/cards/{dealer_card}.png')
                        # Output card
                        dealer_label_5.config(image=dealer_image5)
                        # Increment dealer spot counter
                        dealer_spot += 1
                        
                        # See if they have 5 cards
                        player_total = 0
                        dealer_total = 0

                        # get dealer score
                        for score in dealer_score:
                            dealer_total += score

                        # get player score
                        for score in player_score:
                            player_total += score

                        # Check to see if <= 21
                        if dealer_total <= 21:
                            # dealer wins
                            # disable buttons
                            cardb.config(state="disabled")
                            standb.config(state="disabled")
                            messagebox.showinfo("Five card trick", "Dealer wins")
                except:
                    print("No cards in deck")

                # Check for blackjack after dealing out cards 
                blackjack_test("dealer")

        def player_hit():
            global player_spot
            global player_total, dealer_total, player_score, dealer_score

            if player_spot <= 5:
                try:
                    # get player card
                    player_card = random.choice(deck)
                    deck.remove(player_card)
                    # append card to player list
                    dealer.append(player_card)
                    # append card to score list and convert values to real blackjack values
                    numberofplayercard = int(player_card.split("_", 1)[0]) # Find the number of the card
                    if numberofplayercard == 1: # Changing Ace to 11
                        player_score.append(11)
                    elif numberofplayercard == 11 or numberofplayercard == 12 or numberofplayercard == 13: #Changing jack, queen and king to value 10 (like in blackjack)
                        player_score.append(10)
                    else:
                        player_score.append(numberofplayercard)

                    # show card on screen
                    global player_image1, player_image2, player_image3, player_image4, player_image5

                    if player_spot == 0:
                        # Resize card
                        player_image1 = resize(f'assets/cards/{player_card}.png')
                        # Output card
                        player_label_1.config(image=player_image1)
                        #print(f'{len(deck)} cards left')
                        # Increment player spot counter
                        player_spot += 1
                    elif player_spot == 1:
                        # Resize card
                        player_image2 = resize(f'assets/cards/{player_card}.png')
                        # Output card
                        player_label_2.config(image=player_image2)
                        # Increment player spot counter
                        player_spot += 1
                    elif player_spot == 2:
                        # Resize card
                        player_image3 = resize(f'assets/cards/{player_card}.png')
                        # Output card
                        player_label_3.config(image=player_image3)
                        # Increment player spot counter
                        player_spot += 1
                    elif player_spot == 3:
                        # Resize card
                        player_image4 = resize(f'assets/cards/{player_card}.png')
                        # Output card
                        player_label_4.config(image=player_image4)
                        # Increment player spot counter
                        player_spot += 1
                    elif player_spot == 4:
                        # Resize card
                        player_image5 = resize(f'assets/cards/{player_card}.png')
                        # Output card
                        player_label_5.config(image=player_image5)
                        # Increment player spot counter
                        player_spot += 1
                        
                        # See if they have 5 cards
                        player_total = 0
                        dealer_total = 0

                        # get dealer score
                        for score in dealer_score:
                            dealer_total += score

                        # get player score
                        for score in player_score:
                            player_total += score

                        # Check to see if <= 21
                        if player_total <= 21:
                            # player wins
                            # disable buttons
                            cardb.config(state="disabled")
                            standb.config(state="disabled")
                            messagebox.showinfo("Five card trick", "Player wins")
                except:
                    print("No cards in deck")

                # Check for blackjack after dealing out cards 
                blackjack_test("player")

        # deal cards out to player / dealer
        # def deal_cards():
        #     try:
        #         # get dealers card
        #         card = random.choice(deck)
        #         deck.remove(card)
        #         dealer.append(card)

        #         # show card on screen
        #         global dealer_image
        #         dealer_image = resize(f'assets/cards/{card}.png')
        #         dealer_label.config(image=dealer_image)

        #         # get players card
        #         card = random.choice(deck)
        #         deck.remove(card)
        #         player.append(card)

        #         # show card on screen
        #         global player_image
        #         player_image = resize(f'assets/cards/{card}.png')
        #         player_label.config(image=player_image)

        #         print(f'{len(deck)} cards left')
        #     except:
        #         pass

        # shuffle / deal buttons

        def stand():
            global player_total, dealer_total, player_score
            # keep track of total score of player / dealer
            player_total = 0
            dealer_total = 0

            # get dealers score
            for score in dealer_score:
                # add up score
                dealer_total += score

            # get players score
            for score in player_score:
                # add up score
                player_total += score

            # freeze buttons
            cardb.config(state="disabled")
            standb.config(state="disabled")

            # see if dealer has 17 or above
            if dealer_total >= 17:
                # check if bust
                if dealer_total > 21:
                    # bust
                    messagebox.showinfo('Dealer bust', f'You have won! dealer - {dealer_total}')
                elif dealer_total == player_total:
                    # tie
                    messagebox.showinfo('Push', 'Its a tie!')
                elif dealer_total > player_total:
                    # dealer wins
                    messagebox.showinfo('Blackjack', 'Dealer wins!')
                else:
                    # player wins
                    messagebox.showinfo('Blackjack', 'You have won!')
            else:
                # give dealer a card
                dealer_hit()
                # recalculate
                stand()

        button_frame = Frame(self, bg='#35654d')
        button_frame.pack(pady=20)

        shuffleb = tk.Button(button_frame, text='Shuffle', command=shuffle)
        shuffleb.grid(row=0, column=0)

        cardb = tk.Button(button_frame, text='Hit me', command=player_hit)
        cardb.grid(row=0, column=1, padx=10)

        standb = tk.Button(button_frame, text='Stand', command=stand)
        standb.grid(row=0, column=2)

        # shuffle the deck once
        first = TRUE
        shuffle()
        first = FALSE

class blank(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # configuring the frame
        self.configure(background="#333333")


if __name__ == "__main__":

    # configuring the app
    app = App()
    app.title('BlackJack Card Game NEA')
    app.iconbitmap('assets/icon.ico')
    app.geometry("900x500")
    app.state('zoomed')
    app.configure(background="#333333")

    # open the main app
    app.mainloop()

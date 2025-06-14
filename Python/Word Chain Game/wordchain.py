import tkinter as tk
import random

def operateComputerMode(frame):
    pass
def checkWord(frame):
    pass

def setDifficulty(difficulty):
    if difficulty == 'Easy':
        timer = 180
    elif difficulty == 'Medium':
        timer = 120
    elif difficulty == 'Hard':
        timer = 60
    return timer

def operateTimerMode(frame, difficulty):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    displayTimerAndScore(frame, difficulty)

    frame.pack(expand=True, fill='both')


def countDownTimer(timer_label, timer, frame):
    if timer > 0:
        minutesRemaining = timer // 60
        secondsRemaining = timer % 60
        timer_label.config(text=f'Time Left: {minutesRemaining:01d}:{secondsRemaining:02d}', font=statusFont)
        timer -= 1
        window.after(1000, lambda: countDownTimer(timer_label, timer, frame))
    else:
        timeUpWindow = tk.Toplevel(window)
        timeUpWindow.title("Time's Up")
        timeUpWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
        timeUpLabel = tk.Label(timeUpWindow, text='Time is up', font=informationFont)
        

def displayTimerAndScore(frame, difficulty):
    chosenTimer = setDifficulty(difficulty)
    timerLabel = tk.Label(frame, text=f'Time Left: {chosenTimer} seconds', font=statusFont)
    scoreLabel = tk.Label(frame, text=f'Score: {score}', font=statusFont)
    scoreLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    timerLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    countDownTimer(timerLabel, chosenTimer, frame)

def displayHighScores(frame):
    pass
def displayDifficultyLevels(frame, mode):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    chooseYourModeLabel = tk.Label(frame, text='Choose Your Mode', font=titleFont)
    if mode == 'timer':
        easyModeButton = tk.Button(frame, text='Easy', command=lambda: operateTimerMode(frame, 'Easy'), font=buttonFont)
        mediumModeButton = tk.Button(frame, text='Medium', command=lambda: operateTimerMode(frame, 'Medium'), font=buttonFont)
        hardModeButton = tk.Button(frame, text='Hard', command=lambda: operateTimerMode(frame, 'Hard'), font=buttonFont)
    else:
        easyModeButton = tk.Button(frame, text='Easy', command=lambda: operateComputerMode(frame, 'Easy'), font=buttonFont)
        mediumModeButton = tk.Button(frame, text='Medium', command=lambda: operateComputerMode(frame, 'Medium'), font=buttonFont)
        hardModeButton = tk.Button(frame, text='Hard', command=lambda: operateComputerMode(frame, 'Hard'), font=buttonFont)
    backButton = tk.Button(frame, text='<-', command=lambda: displayMainMenu(frame), font=buttonFont)
    chooseYourModeLabel.pack()
    easyModeButton.pack(pady=10)
    mediumModeButton.pack(pady=10)
    hardModeButton.pack(pady=10)
    backButton.pack(pady=20)
    frame.pack(expand=True, fill='both')

def displayMainMenuWidgets(index, widgets, frame):
    if index < len(widgets):
        widget, pack_options = widgets[index]
        widget.pack(**pack_options)
        frame.after(1250, lambda: displayMainMenuWidgets(index + 1, widgets, frame))

def displayMainMenu(frame):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    wordChainGameLabel = tk.Label(frame, text='Word Chain Game', font=titleFont)
    chooseYourModeLabel = tk.Label(frame, text='Choose Your Mode!', font=buttonFont)
    timerModeButton = tk.Button(frame, text='Timer Mode', command=lambda: displayDifficultyLevels(frame, 'timer'), font=buttonFont)
    computerModeButton = tk.Button(frame, text='Computer Mode', command=lambda: displayDifficultyLevels(frame, 'computer'), font=buttonFont)
    howToPlayButton = tk.Button(frame, text='How To Play?', command=lambda: displayInstructionsOnHowToPlay(frame), font=buttonFont)
    quitButton = tk.Button(frame, text='Quit', command=window.destroy, font=buttonFont)
    mainMenuWidgets = [(wordChainGameLabel, {}), (chooseYourModeLabel, {'pady': 20}), (timerModeButton, {'pady': 10}),
    (computerModeButton, {'pady': 10}), (howToPlayButton, {'pady': 10}), (quitButton, {'pady': 20})]
    frame.pack(expand=True, fill='both')
    index = 0
    global userAnimatesMainMenu
    if userAnimatesMainMenu:
        displayMainMenuWidgets(index, mainMenuWidgets, frame)
        userAnimatesMainMenu = False
    else:
        for widget, pack_options in mainMenuWidgets:
            widget.pack(**pack_options)

def displayInstructionsOnHowToPlay(frame):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    howToPlayLabel = tk.Label(frame, text='How To Play', font=titleFont)
    instructionsLabel = tk.Label(frame, text='''
    • Words must begin with the last letter of the previous word after the first word is entered
    • Each word MUST contain at least 3 letters
    • Repeating words is strictly forbidden
    • Please enter valid words that you would find in a dictionary
    
    Example: call -> lock -> keen -> none -> egg
                                 
    Mode Information:
                                 
    Timer Mode:
                                 
    • Race against the clock to make as many words as possible
    • Score points based on word length and speed
                    
    Computer Mode:
                                 
    • Take turns with the computer; computer guesses a word, you guess a word, and so on
    • First player who can't respond in time loses
    ''', font=informationFont, justify='left')
    backButton = tk.Button(frame, text='<-', command=lambda: displayMainMenu(frame), font=buttonFont)
    howToPlayLabel.pack(pady=20)
    instructionsLabel.pack(pady=30)
    backButton.pack(pady=20)
    frame.pack(expand=True, fill='both')    
window = tk.Tk()
window.minsize(800, 600)
window.resizable(True, True)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
userAnimatesMainMenu = True
window.title('Word Chain Game')
titleFont = ('Georgia', 37, 'bold') 
buttonFont = ('Georgia', 20)
informationFont = ('Georgia', 20)
statusFont = ('Georgia', 10)
score = 0
highScores = []
windowFrame = tk.Frame(window)
displayMainMenu(windowFrame)
window.mainloop()
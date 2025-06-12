import tkinter as tk
import random

def operateComputerGame(frame):
    pass
def checkWord(frame):
    pass

def countDownTimer(frame):
    pass

def displayTimerAndScore(frame):
    pass
def displayHighScores(frame):
    pass
def displayDifficultyLevels(frame, mode):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    chooseYourModeLabel = tk.Label(frame, text='Choose Your Mode', font=titleFont)
    if mode == 'timer':
        easyModeButton = tk.Button(frame, text='Easy', command=lambda: displayTimerAndScore(frame), font=buttonFont)
        mediumModeButton = tk.Button(frame, text='Medium', command=lambda: displayTimerAndScore(frame), font=buttonFont)
        hardModeButton = tk.Button(frame, text='Hard', command=lambda: displayTimerAndScore(frame), font=buttonFont)
    else:
        easyModeButton = tk.Button(frame, text='Easy', command=lambda: operateComputerGame(frame), font=buttonFont)
        mediumModeButton = tk.Button(frame, text='Medium', command=lambda: operateComputerGame(frame), font=buttonFont)
        hardModeButton = tk.Button(frame, text='Hard', command=lambda: operateComputerGame(frame), font=buttonFont)
    backButton = tk.Button(frame, text='<-', command=lambda: displayMainMenu(frame), font=buttonFont)
    chooseYourModeLabel.pack()
    easyModeButton.pack(pady=10)
    mediumModeButton.pack(pady=10)
    hardModeButton.pack(pady=10)
    backButton.pack(pady=20)
    frame.pack(expand=True, fill='both')


def displayMainMenu(frame):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    wordChainGameLabel = tk.Label(frame, text='Word Chain Game', font=titleFont)
    chooseYourModeLabel = tk.Label(frame, text='Choose Your Mode!', font=buttonFont)
    timerModeButton = tk.Button(frame, text='Timer Mode', command=lambda: displayDifficultyLevels(frame, 'timer'), font=buttonFont)
    computerModeButton = tk.Button(frame, text='Computer Mode', command=lambda: displayDifficultyLevels(frame, 'computer'), font=buttonFont)
    howToPlayButton = tk.Button(frame, text='? How To Play', command=lambda: displayInstructionsOnHowToPlay(frame), font=buttonFont)
    quitButton = tk.Button(frame, text='Quit', command=window.destroy, font=buttonFont)
    wordChainGameLabel.pack()
    chooseYourModeLabel.pack(pady=20)
    timerModeButton.pack(pady=10)
    computerModeButton.pack(pady=10)
    howToPlayButton.pack(pady=10)
    quitButton.pack(pady=20)
    frame.pack(expand=True, fill='both')

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
                                 
    • Take turns with the computer; computer guesses a word, you guess a word, and so on.
    • First player who can't respond in time loses
    
    Definition Mode:
                                 
    • 
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
window.title('Word Chain Game')
titleFont = ('Georgia', 37, 'bold') 
buttonFont = ('Georgia', 20)
informationFont = ('Georgia', 20)
windowFrame = tk.Frame(window)
displayMainMenu(windowFrame)
window.mainloop()
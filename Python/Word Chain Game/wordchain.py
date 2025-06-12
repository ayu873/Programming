import tkinter as tk
import random

def checkWord(frame):
    pass

def countDownTimer(frame):
    pass

def displayTimer(frame):
    pass
def displayHighScores(frame):
    pass

def displayMainMenu(frame):
    wordChainGameLabel = tk.Label(frame, text='Word Chain Game', font=titleFont)

def displayInstructionsOnHowToPlay():
    pass


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
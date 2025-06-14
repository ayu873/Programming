import nltk
from nltk.corpus import brown
from nltk.corpus import words
import tkinter as tk
import random

def displayMainWindow(frame):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    welcomeLabel = tk.Label(frame, text='Welcome To Wordle!', font=titleFont)
    coinsLabel = tk.Label(frame, text=f'{coins} coins', font=statusFont)
    hintsLabel = tk.Label(frame, text=f'{hints} hints', font=statusFont)
    startLabel = tk.Label(frame, text='Click on any option below to get started! :)', font=buttonFont)
    playButton = tk.Button(frame, text='Play!', width=5, command=lambda: displayDifficulties(frame), font=buttonFont)
    shopButton = tk.Button(frame, text='Shop', width=5, command=lambda: operateShop(frame), font=buttonFont)
    helpButton = tk.Button(frame, text='Help', width=5, command=lambda: displayInstructions(frame), font=buttonFont)
    quitButton = tk.Button(frame, text='Quit', width=5, command=window.destroy, font=buttonFont)
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    welcomeLabel.pack(pady=(35, 0))
    startLabel.pack()
    playButton.pack()
    shopButton.pack()
    helpButton.pack()
    quitButton.pack()  
    frame.pack(expand=True, fill='both')

def checkEntries(entries, frame):
    global currentGuess
    indexOfRandomWord = 0
    listOfGuessedWord = []
    for i in entries:
        letter = i.get().lower()
        listOfGuessedWord.append(letter)
        if letter == randomWord[indexOfRandomWord]:
            i.config(bg='green')
        elif letter in randomWord and letter != randomWord[indexOfRandomWord]:
            i.config(bg='yellow')
        else:
            i.config(bg='gray')
        indexOfRandomWord += 1
    currentGuess += 1
    joinedGuessedWord = ''.join(listOfGuessedWord)

    if joinedGuessedWord == randomWord:
        global guesses
        guesses = currentGuess
        guessWindow = tk.Toplevel(window)
        guessWindow.title('You Guessed It')
        guessWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
        greatJobLabel = tk.Label(guessWindow, text='Great Job!', font=informationFont)
        guessWordLabel = tk.Label(guessWindow, text=f'You guessed the word in {currentGuess} tries', font=informationFont)
        wouldYouLikeToPlayAgainLabel = tk.Label(guessWindow, text='Would you like to play again?', font=informationFont)
        yesButton = tk.Button(guessWindow, text='Yes', command=lambda: [guessWindow.destroy(), displayDifficulties(frame)], font=buttonFont)
        noButton = tk.Button(guessWindow, text='No', command=window.destroy, font=buttonFont)
        greatJobLabel.pack()
        guessWordLabel.pack()
        wouldYouLikeToPlayAgainLabel.pack()
        yesButton.pack(side='left')
        noButton.pack(side='left')
        return
    
    if currentGuess < guesses:
        window.after(1000, lambda: displayEntries(frameForWindow))
    elif currentGuess == guesses:
        usedUpGuessesWindow = tk.Toplevel(window)
        usedUpGuessesWindow.title('You Used Up All Your Guesses')
        usedUpGuessesWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
        ohNoLabel = tk.Label(usedUpGuessesWindow, text='Oh No!', font=informationFont)
        usedUpGuessesLabel = tk.Label(usedUpGuessesWindow, text='You have used up all your guesses!', font=informationFont)
        wordLabel = tk.Label(usedUpGuessesWindow, text=f'The word was {randomWord}', font=informationFont)
        wouldYouLikeToPlayAgainLabel = tk.Label(usedUpGuessesWindow, text='Would you like to play again?', font=informationFont)
        yesButton = tk.Button(usedUpGuessesWindow, text='Yes', command=lambda: [usedUpGuessesWindow.destroy(), displayDifficulties(frame)], font=buttonFont)
        noButton = tk.Button(usedUpGuessesWindow, text='No', command=window.destroy, font=buttonFont)
        ohNoLabel.pack()
        usedUpGuessesLabel.pack()
        wordLabel.pack()
        wouldYouLikeToPlayAgainLabel.pack()
        yesButton.pack(side='left')
        noButton.pack(side='left')

def countDownTheTimer(labelForTimer, timer, frame):
    if timer > 0 and currentGuess < guesses:
        minutesRemaining = timer // 60
        secondsRemaining = timer % 60
        labelForTimer.config(text=f'Time Left: {minutesRemaining:01d}:{secondsRemaining:02d}', font=statusFont)
        timer -= 1
        window.after(1000, lambda: countDownTheTimer(labelForTimer, timer, frame))
    elif timer <= 0 and currentGuess < guesses:
        timeIsUpWindow = tk.Toplevel(window)
        timeIsUpWindow.title("Time's Up")
        timeIsUpWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
        timeIsUpLabel = tk.Label(timeIsUpWindow, text="Time's up!", font=informationFont)
        wordLabel = tk.Label(timeIsUpWindow, text=f'The word was {randomWord}', font=informationFont)
        playAgainLabel = tk.Label(timeIsUpWindow, text='Would you like to play again?', font=informationFont)
        yesButton = tk.Button(timeIsUpWindow, text='Yes', command=lambda: [timeIsUpWindow.destroy(), displayDifficulties(frame)], font=buttonFont)
        noButton = tk.Button(timeIsUpWindow, text='No', command=window.destroy, font=buttonFont)
        timeIsUpLabel.pack()
        wordLabel.pack()
        playAgainLabel.pack()
        yesButton.pack(side='left')
        noButton.pack(side='left')

def createTimer(frame, level):
    if level == 'Easy':
        timer = 60
    elif level == 'Medium':
        timer = 45
    elif level == 'Hard':
        timer = 30
    timerLabel = tk.Label(frame, text=f'Time Left: {timer} seconds', font=statusFont)
    timerLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=34)
    countDownTheTimer(timerLabel, timer, frame)

def revealConsonant():
    consonants = 'bcdfghjklmnpqrstvwxyz'
    for i in randomWord:
        if i in consonants:
            consonantWindow = tk.Toplevel(window)
            consonantWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
            consonantHintLabel = tk.Label(consonantWindow, text='Consonant Hint', font=informationFont)
            consonantLabel = tk.Label(consonantWindow, text=f'The consonant {i} is in the word', font=informationFont)
            okButton = tk.Button(consonantWindow, text='OK', width=5, command=consonantWindow.destroy, font=buttonFont)
            consonantHintLabel.pack()
            consonantLabel.pack()
            okButton.pack()
            return

def revealVowel():
    vowels = 'aeiou'
    vowelWindow = tk.Toplevel(window)
    vowelWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
    vowelHintLabel = tk.Label(vowelWindow, text='Vowel Hint', font=titleFont)
    okButton = tk.Button(vowelWindow, text='OK', width=5, command=vowelWindow.destroy, font=buttonFont)
    for i in randomWord:
        if i in vowels:
            vowelLabel = tk.Label(vowelWindow, text=f'The vowel {i} is in the word', font=informationFont)
            vowelHintLabel.pack()
            vowelLabel.pack()
            okButton.pack()
            return
    noVowelsLabel = tk.Label(vowelWindow, text='There are no vowels', font=informationFont)
    vowelHintLabel.pack()
    noVowelsLabel.pack()
    okButton.pack()
    return
        
def revealLettersThatRepeat():
    global hintsRemaining
    repeatedLetterWindow = tk.Toplevel(window)
    repeatedLetterWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
    repeatedLetterHintLabel = tk.Label(repeatedLetterWindow, text='Repeated Letter Hint', font=titleFont)
    okButton = tk.Button(repeatedLetterWindow, text='OK', width=5, command=repeatedLetterWindow.destroy, font=buttonFont)
    hintsRemaining -= 1
    for i in randomWord:
        if randomWord.count(i) > 1:
            repeatedLetterLabel = tk.Label(repeatedLetterWindow, text=f'The letter {i} is repeated', font=informationFont)
            repeatedLetterHintLabel.pack()
            repeatedLetterLabel.pack()
        else:
            noRepeatedLettersLabel = tk.Label(repeatedLetterWindow, text='There are no repeated letters', font=informationFont)
            repeatedLetterHintLabel.pack()
            noRepeatedLettersLabel.pack()
        okButton.pack()
        return

def displayHints(difficulty_level):
    hintWindow = tk.Toplevel(window)
    hintWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
    randomHints = [revealConsonant, revealVowel, revealLettersThatRepeat]
    global hintsRemaining
    if difficulty_level == 'Easy':
        hintsRemaining = 3
    elif difficulty_level == 'Medium':
        hintsRemaining = 2
    elif difficulty_level == 'Hard':
        hintsRemaining = 1
    hintsRemainingLabel = tk.Label(hintWindow, text=f'Hints Remaining: {hintsRemaining}', font=informationFont)
    for i in range(1, len(randomHints) + 1):
        selectedHint = random.choice(randomHints)
        print(selectedHint)
        hint = tk.Button(hintWindow, text=f'Hint {i}', width=5, command=selectedHint, font=buttonFont)
        randomHints.remove(selectedHint)
        hintsRemainingLabel.pack()
        hint.pack()

def displayHintButton(frame, difficultyLevel):
    hintsButton = tk.Button(frame, text='Hints', width=6, command=lambda: displayHints(difficultyLevel), font=buttonFont)
    hintsButton.place(relx=1, rely=0, anchor='ne', x=-5, y=51)
    
def moveToNextEntry(event, entries, frame):
    if not event.char.isalpha():
        return 'break'
    currentEntry = event.widget
    currentIndex = entries.index(currentEntry)
    currentEntry.delete(0, tk.END)
    currentEntry.insert(0, event.char.lower())
    if currentIndex == len(entries) - 1:
        checkEntries(entries, frame)
    else:
        nextEntry = entries[currentIndex + 1]
        nextEntry.focus()
    return 'break'

def displayEntries(frame): 
    entryFrame = tk.Frame(frame)
    listOfEntries = []
    for i in range(len(randomWord)):
        entry = tk.Entry(entryFrame, width=2, justify='center', font=informationFont)
        entry.pack(side='left', padx=5, pady=5)
        listOfEntries.append(entry)
    for i in range(len(listOfEntries)):
        listOfEntries[i].bind('<KeyPress>', lambda event, entries=listOfEntries, frame=frame: moveToNextEntry(event, entries, frame))
    listOfEntries[0].focus()
    entryFrame.pack()
    frame.pack(expand=True, fill='both')

def operateGame(frame, level_of_difficulty):
    global currentGuess, guesses, currentDifficulty
    currentGuess = 0
    currentDifficulty = level_of_difficulty
    if currentDifficulty == 'Easy':
        guesses = 5
    elif currentDifficulty == 'Medium':
        guesses = 4
    elif currentDifficulty == 'Hard':
        guesses = 3
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    coinsLabel = tk.Label(frame, text=f'{coins} coins', font=statusFont)
    hintsLabel = tk.Label(frame, text=f'{hints} hints', font=statusFont)
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    createTimer(frame, level_of_difficulty)
    displayHintButton(frame, level_of_difficulty)
    displayEntries(frame)
    
def getUserInput(frame):
    global userSelectedOption
    selectedDifficulty = userSelectedOption.get()
    operateGame(frame, selectedDifficulty)

def displayDifficulties(frame):
    global userSelectedOption
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    coinsLabel = tk.Label(frame, text=f'{coins} coins', font=statusFont)
    hintsLabel = tk.Label(frame, text=f'{hints} hints', font=statusFont)
    userSelectedOption = tk.StringVar(value=' ')
    global randomWord
    randomWord = random.choice(wordList)
    print(randomWord)
    chooseDifficultyLabel = tk.Label(frame, text='Choose your difficulty level:', font=informationFont)
    easyOption = tk.Radiobutton(frame, text='Easy', variable=userSelectedOption, value='Easy', selectcolor="white", font=informationFont)
    mediumOption = tk.Radiobutton(frame, text='Medium', variable=userSelectedOption, value='Medium', selectcolor="white", font=informationFont)
    hardOption = tk.Radiobutton(frame, text='Hard', variable=userSelectedOption, value='Hard', selectcolor="white", font=informationFont)
    okButton = tk.Button(frame, text='OK', width=5, command=lambda: getUserInput(frame), font=buttonFont)
    backButton = tk.Button(frame, text='Back', width=5, command=lambda: displayMainWindow(frame), font=buttonFont)          
    quitButton = tk.Button(frame, text='Quit', width=5, command=window.destroy, font=buttonFont)
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    chooseDifficultyLabel.pack()
    easyOption.pack()
    mediumOption.pack()
    hardOption.pack()
    okButton.pack()
    backButton.pack()
    quitButton.pack()
    frame.pack(expand=True, fill='both')

def buy(cost):
    global coinsLabel, hintsLabel, hints, coins
    if coins < cost:
        errorWindow = tk.Toplevel(window)
        errorWindow.title('Error Message')
        errorLabel = tk.Label(errorWindow, text='Not Enough Coins!')
        okButton = tk.Button(errorWindow, text='OK', command=errorWindow.destroy)
        errorLabel.pack()
        okButton.pack()
        return
    if cost == 50:
        hints += 1
    elif cost == 100:
        hints += 2
    elif cost == 150:
        hints += 5
    elif cost == 250:
        hints += 7
    elif cost == 500:
        hints += 10
    coins -= cost

    coinsLabel.config(text=f'{coins} coins')
    hintsLabel.config(text=f'{hints} hints')
    
def operateShop(frame):
    global coinsLabel, hintsLabel
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    coinsLabel = tk.Label(frame, text=f'{coins} coins')
    hintsLabel = tk.Label(frame, text=f'{hints} hints')
    oneHintFrame = tk.Frame(frame)
    oneHintLabel = tk.Label(oneHintFrame, text='1 hint')
    fiftyCoinButton = tk.Button(oneHintFrame, text='50 coins', width=6, command=lambda: buy(50))
    twoHintFrame = tk.Frame(frame)
    twoHintsLabel = tk.Label(twoHintFrame, text='2 hints')
    hundredCoinButton = tk.Button(twoHintFrame, text='100 coins', width=7, command=lambda: buy(100))
    fiveHintFrame = tk.Frame(frame)
    fiveHintsLabel = tk.Label(fiveHintFrame, text='5 hints')
    oneHundredFiftyCoinLabel = tk.Button(fiveHintFrame, text='150 coins', width=7, command=lambda: buy(150))
    sevenHintFrame = tk.Frame(frame)
    sevenHintsLabel = tk.Label(sevenHintFrame, text='7 hints')
    twoHundredFiftyCoinButton = tk.Button(sevenHintFrame, text='250 coins', width=7, command=lambda: buy(250))
    tenHintFrame = tk.Frame(frame)
    tenHintsLabel = tk.Label(tenHintFrame, text='10 hints')
    fiveHundredCoinButton = tk.Button(tenHintFrame, text='500 coins', width=7, command=lambda: buy(500))
    backButton = tk.Button(frame, text='Back', width=5, command=lambda: displayMainWindow(frame))          
    quitButton = tk.Button(frame, text='Quit', width=5, command=window.destroy)
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    oneHintLabel.pack(side='left')
    fiftyCoinButton.pack(side='left')
    oneHintFrame.pack()
    twoHintsLabel.pack(side='left')
    hundredCoinButton.pack(side='left')
    twoHintFrame.pack()
    fiveHintsLabel.pack(side='left')
    oneHundredFiftyCoinLabel.pack(side='left')
    fiveHintFrame.pack()
    sevenHintsLabel.pack(side='left')
    twoHundredFiftyCoinButton.pack(side='left')
    sevenHintFrame.pack()
    tenHintsLabel.pack(side='left')
    fiveHundredCoinButton.pack(side='left')
    tenHintFrame.pack()
    backButton.pack()
    quitButton.pack()
    frame.pack(expand=True, fill='both')
    
def displayInstructions(frame):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    titleLabel = tk.Label(frame, text='How To Play', font=titleFont)
    coinsLabel = tk.Label(frame, text=f'{coins} coins', font=statusFont)
    hintsLabel = tk.Label(frame, text=f'{hints} hints', font=statusFont)
    guessLabel = tk.Label(frame, text='• Try to guess the word in 3, 4, or 5 tries', font=informationFont)
    validLabel = tk.Label(frame, text='• Each entry MUST contain a letter', font=informationFont)
    useHintsLabel = tk.Label(frame, text="• Use hints if you'd like to help you guess the word", font=informationFont)
    timerCountsDownLabel = tk.Label(frame, text='• The timer counts down while you play', font=informationFont)
    colorGuideLabel = tk.Label(frame, text='Color Guide:', font=informationFont)
    greenLabel = tk.Label(frame, text='🟩 Green - the letter is in the correct spot', font=informationFont, fg='#538d4e')
    yellowLabel = tk.Label(frame, text='🟨 Yellow - the letter is in the word but in the wrong spot', font=informationFont, fg="#f7d94f")
    grayLabel = tk.Label(frame, text='⬜ Gray - the letter is not in the word', font=informationFont, fg='#3a3a3c')
    backButton = tk.Button(frame, text='Back', width=5, command=lambda: displayMainWindow(frame), font=buttonFont)
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    titleLabel.pack(pady=(35, 30))
    guessLabel.pack(pady=3)
    validLabel.pack(pady=3)
    useHintsLabel.pack(pady=3)
    timerCountsDownLabel.pack(pady=3)
    colorGuideLabel.pack(pady=(20, 10))
    greenLabel.pack(pady=3)
    yellowLabel.pack(pady=3)
    grayLabel.pack(pady=3)
    backButton.pack(pady=30)
    frame.pack(expand=True, fill='both')

wordList = []
wordFrequency = nltk.FreqDist(brown.words())
for word in words.words():
    if 3 <= len(word) <= 7 and word.isalpha():
        if word.lower() in wordFrequency and wordFrequency[word.lower()] > 10:
            wordList.append(word.lower())
titleFont = ('Georgia', 37, 'bold') 
buttonFont = ('Georgia', 20)
statusFont = ('Georgia', 10)
informationFont = ('Georgia', 20)
randomWord = None
window = tk.Tk()
window.minsize(800, 600)
window.resizable(True, True)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.title('Wordle')
frameForWindow = tk.Frame(master=window)
coins = 1000
hints = 0
displayMainWindow(frameForWindow)
window.mainloop()
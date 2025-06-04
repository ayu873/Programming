from nltk.corpus import wordnet
import tkinter as tk
import random

def displayMainWindow(frame):
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    welcomeLabel = tk.Label(frame, text='Welcome To Wordle!')
    coinsLabel = tk.Label(frame, text=f'{coins} coins')
    hintsLabel = tk.Label(frame, text=f'{hints} hints')
    startLabel = tk.Label(frame, text='Click on any option below to get started! :)')
    playButton = tk.Button(frame, text='Play!', width=5, command=lambda: displayDifficulties(frame))
    shopButton = tk.Button(frame, text='Shop', width=5, command=lambda: operateShop(frame))
    helpButton = tk.Button(frame, text='Help', width=5, command=lambda: displayInstructions(frame))
    quitButton = tk.Button(frame, text='Quit', width=5, command=window.destroy)
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    welcomeLabel.pack(pady=(35, 0))
    startLabel.pack()
    playButton.pack()
    shopButton.pack()
    helpButton.pack()
    quitButton.pack()  
    frame.pack(expand=True, fill='both')

def checkEntries(entries, frame, entry):
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
        if len(letter) != 1 or not letter.isalpha():
            errorWindow = tk.Toplevel(window)
            errorWindow.title('Error Message')
            warningLabel = tk.Label(errorWindow, text='Warning:')
            oneLetterOnlyLabel = tk.Label(errorWindow, text='One of your entries contains more than one letter or is empty')
            tryAgainLabel = tk.Label(errorWindow, text='Please try again')
            warningLabel.pack()
            oneLetterOnlyLabel.pack()
            tryAgainLabel.pack()
            errorWindow.after(2000, errorWindow.destroy)
            for entry in entries:
                entry.delete(0, tk.END)
                entry.config(bg='white')
            return
        indexOfRandomWord += 1
    currentGuess += 1
    joinedGuessedWord = ''.join(listOfGuessedWord)
    if joinedGuessedWord == randomWord:
        guessWindow = tk.Toplevel(window)
        guessWindow.title('You Guessed It')
        guessWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
        greatJobLabel = tk.Label(guessWindow, text='Great Job!')
        guessWordLabel = tk.Label(guessWindow, text=f'You guessed the word in {currentGuess} tries')
        wouldYouLikeToPlayAgainLabel = tk.Label(guessWindow, text='Would you like to play again?')
        yesButton = tk.Button(guessWindow, text='Yes', command=lambda: [displayDifficulties(frame), guessWindow.destroy])
        noButton = tk.Button(guessWindow, text='No', command=window.destroy)
        greatJobLabel.pack()
        guessWordLabel.pack()
        wouldYouLikeToPlayAgainLabel.pack()
        yesButton.pack(side='left')
        noButton.pack(side='left')
    if currentGuess < guesses:
        window.after(1000, lambda: displayEntries(frameForWindow, currentDifficulty))
    elif currentGuess == guesses:
        usedUpGuessesWindow = tk.Toplevel(window)
        usedUpGuessesWindow.title('You Used Up All Your Guesses')
        usedUpGuessesWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
        ohNoLabel = tk.Label(usedUpGuessesWindow, text='Oh No!')
        usedUpGuessesLabel = tk.Label(usedUpGuessesWindow, text='You have used up all your guesses!')
        wordLabel = tk.Label(usedUpGuessesWindow, text=f'The word was {randomWord}')
        wouldYouLikeToPlayAgainLabel = tk.Label(usedUpGuessesWindow, text='Would you like to play again?')
        yesButton = tk.Button(usedUpGuessesWindow, text='Yes', command=lambda: [displayDifficulties(frame), usedUpGuessesWindow.destroy])
        noButton = tk.Button(usedUpGuessesWindow, text='No', command=window.destroy)
        ohNoLabel.pack()
        usedUpGuessesLabel.pack()
        wordLabel.pack()
        wouldYouLikeToPlayAgainLabel.pack()
        yesButton.pack(side='left')
        noButton.pack(side='left')
        
        


def displayRememberToPressEnterWindow():
    rememberToPressEnterWindow = tk.Toplevel(window)
    rememberToPressEnterWindow.title('Press Enter')
    rememberToPressEnterLabel = tk.Label(rememberToPressEnterWindow, text='Remember to press ENTER after you have filled in ALL of the entries')
    rememberToPressEnterLabel.pack()
    rememberToPressEnterWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
    rememberToPressEnterWindow.after(2000, rememberToPressEnterWindow.destroy)

def countDownTheTimer(labelForTimer, timer, frame):
    if timer > 0:
        minutesRemaining = timer // 60
        secondsRemaining = timer % 60
        labelForTimer.config(text=f'Time Left: {minutesRemaining:01d}:{secondsRemaining:02d}')
        timer -= 1
        window.after(1000, lambda: countDownTheTimer(labelForTimer, timer, frame))
    else:
        timeIsUpWindow = tk.Toplevel(window)
        timeIsUpWindow.title("Time's Up")
        timeIsUpWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
        timeIsUpLabel = tk.Label(timeIsUpWindow, text="Time's up!")
        wordLabel = tk.Label(timeIsUpWindow, text=f'The word was {randomWord}')
        playAgainLabel = tk.Label(timeIsUpWindow, text='Would you like to play again?')
        yesButton = tk.Button(timeIsUpWindow, text='Yes', command=lambda: [timeIsUpWindow.destroy(), displayDifficulties(frame)])
        noButton = tk.Button(timeIsUpWindow, text='No', command=window.destroy)
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
    timerLabel = tk.Label(frame, text=f'Time Left: {timer} seconds')
    timerLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=34)
    countDownTheTimer(timerLabel, timer, frame)

def revealConsonant():
    consonants = 'bcdfghjklmnpqrstvwxyz'
    for i in randomWord:
        if i in consonants:
            consonantWindow = tk.Toplevel(window)
            consonantWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
            consonantHintLabel = tk.Label(consonantWindow, text='Consonant Hint')
            consonantLabel = tk.Label(consonantWindow, text=f'The consonant {i} is in the word')
            okButton = tk.Button(consonantWindow, text='OK', width=5, command=consonantWindow.destroy)
            consonantHintLabel.pack()
            consonantLabel.pack()
            okButton.pack()
            return

def revealVowel():
    vowels = 'aeiou'
    vowelWindow = tk.Toplevel(window)
    vowelWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
    vowelHintLabel = tk.Label(vowelWindow, text='Vowel Hint')
    okButton = tk.Button(vowelWindow, text='OK', width=5, command=vowelWindow.destroy)
    for i in randomWord:
        if i in vowels:
            vowelLabel = tk.Label(vowelWindow, text=f'The vowel {i} is in the word')
            vowelHintLabel.pack()
            vowelLabel.pack()
            okButton.pack()
            return
    noVowelsLabel = tk.Label(vowelWindow, text='There are no vowels')
    vowelHintLabel.pack()
    noVowelsLabel.pack()
    okButton.pack()
    return
        
def revealLettersThatRepeat():
    global hintsRemaining
    repeatedLetterWindow = tk.Toplevel(window)
    repeatedLetterWindow.geometry("+%d+%d" % (window.winfo_rootx() + 50, window.winfo_rooty() + 50))
    repeatedLetterHintLabel = tk.Label(repeatedLetterWindow, text='Repeated Letter Hint')
    okButton = tk.Button(repeatedLetterWindow, text='OK', width=5, command=repeatedLetterWindow.destroy)
    hintsRemaining -= 1
    for i in randomWord:
        if randomWord.count(i) > 1:
            repeatedLetterLabel = tk.Label(repeatedLetterWindow, text=f'The letter {i} is repeated')
            repeatedLetterHintLabel.pack()
            repeatedLetterLabel.pack()
        else:
            noRepeatedLettersLabel = tk.Label(repeatedLetterWindow, text='There are no repeated letters')
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
    hintsRemainingLabel = tk.Label(hintWindow, text=f'Hints Remaining: {hintsRemaining}')
    for i in range(1, len(randomHints) + 1):
        selectedHint = random.choice(randomHints)
        print(selectedHint)
        hint = tk.Button(hintWindow, text=f'Hint {i}', width=5, command=selectedHint)
        randomHints.remove(selectedHint)
        hintsRemainingLabel.pack()
        hint.pack()

def displayHintButton(frame, difficultyLevel):
    hintsButton = tk.Button(frame, text='Hints', width=6, command=lambda: displayHints(difficultyLevel))
    hintsButton.place(relx=1, rely=0, anchor='ne', x=-5, y=51)
    
def displayEntries(frame, levelOfDifficulty): 
    entryFrame = tk.Frame(frame)
    listOfEntries = []
    for i in range(len(randomWord)):
        entry = tk.Entry(entryFrame, width=2, justify='center')
        entry.pack(side='left', padx=5, pady=5)
        listOfEntries.append(entry)
        entry.bind('<Return>', lambda event: checkEntries(listOfEntries, frame, entry))
        entryFrame.pack()
    frame.pack(expand=True, fill='both')

def operateGame(frame, level_of_difficulty):
    global currentGuess, guesses, currentDifficulty
    currentGuess = 0
    currentDifficulty = level_of_difficulty
    if level_of_difficulty == 'Easy':
        guesses = 5
    elif level_of_difficulty == 'Medium':
        guesses = 4
    elif level_of_difficulty == 'Hard':
        guesses = 3
    displayRememberToPressEnterWindow()
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    coinsLabel = tk.Label(frame, text=f'{coins} coins')
    hintsLabel = tk.Label(frame, text=f'{hints} hints')
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    window.after(2000, lambda: [createTimer(frame, level_of_difficulty), displayHintButton(frame, level_of_difficulty)])
    displayEntries(frame, level_of_difficulty)
    
def confirmDifficulty(difficulty):
    print(len(randomWord))
    frameForWindow.pack_forget()
    for widget in frameForWindow.winfo_children():
        widget.destroy()
    coinsLabel = tk.Label(frameForWindow, text=f'{coins} coins')
    hintsLabel = tk.Label(frameForWindow, text=f'{hints} hints')
    difficultyLabel = tk.Label(frameForWindow, text=f'You have chosen to go {difficulty}. Proceed?')
    proceedButton = tk.Button(frameForWindow, text='Proceed', width=6, command=lambda: operateGame(frameForWindow, difficulty))
    backButton = tk.Button(frameForWindow, text='Back', width=5, command=lambda: displayDifficulties(frameForWindow))      
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    difficultyLabel.pack()
    proceedButton.pack()
    backButton.pack()
    frameForWindow.pack(expand=True, fill='both')
    
def getUserInput():
    global userSelectedOption
    selectedDifficulty = userSelectedOption.get()
    confirmDifficulty(selectedDifficulty)

def displayDifficulties(frame):
    global userSelectedOption
    frame.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    coinsLabel = tk.Label(frame, text=f'{coins} coins')
    hintsLabel = tk.Label(frame, text=f'{hints} hints')
    userSelectedOption = tk.StringVar(value=' ')
    chooseDifficultyLabel = tk.Label(frame, text='Choose your difficulty level:')
    easyOption = tk.Radiobutton(frame, text='Easy', variable=userSelectedOption, value='Easy', selectcolor="white")
    mediumOption = tk.Radiobutton(frame, text='Medium', variable=userSelectedOption, value='Medium', selectcolor="white")
    hardOption = tk.Radiobutton(frame, text='Hard', variable=userSelectedOption, value='Hard', selectcolor="white")
    okButton = tk.Button(frame, text='OK', width=5, command=getUserInput)
    backButton = tk.Button(frame, text='Back', width=5, command=lambda: displayMainWindow(frame))          
    quitButton = tk.Button(frame, text='Quit', width=5, command=window.destroy)
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
    coinsLabel = tk.Label(frame, text=f'{coins} coins')
    hintsLabel = tk.Label(frame, text=f'{hints} hints')
    guessLabel = tk.Label(frame, text='Try to guess the word in 5 tries')
    validLabel = tk.Label(frame, text='Each entry MUST contain a letter')
    greenImage = tk.PhotoImage(file=r"c:\Users\ayaaz\Downloads\green.png")
    greenImage = greenImage.subsample(30, 30)
    greenLabel = tk.Label(frame, image=greenImage, text=' = If one of your entries are green, that means ' \
    'the letter is in the word and in the right spot', compound='left')
    greenLabel.image = greenImage
    yellowImage = tk.PhotoImage(file=r"c:\Users\ayaaz\Downloads\yellow.png")
    yellowImage = yellowImage.subsample(20, 20)
    yellowLabel = tk.Label(frame, image=yellowImage, text=' = If one of your entries are yellow, that means ' \
    'the letter is in the word but in the wrong spot', compound='left')
    yellowLabel.image = yellowImage
    grayImage = tk.PhotoImage(file=r"c:\Users\ayaaz\Downloads\gray.png")
    grayImage = grayImage.subsample(20, 20)
    grayLabel = tk.Label(frame, image=grayImage, text=' = If one of your entries are gray, that means ' \
    'the letter is not in the word at all', compound='left')
    pressEnterLabel = tk.Label(frame, text="Don't forget to press ENTER after you have filled in ALL of the entries")
    grayLabel.image = grayImage
    backButton = tk.Button(frame, text='Back', width=5, command=lambda: displayMainWindow(frame))
    quitButton = tk.Button(frame, text='Quit', width=5, command=window.destroy)
    coinsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=0)
    hintsLabel.place(relx=1, rely=0, anchor='ne', x=-5, y=17)
    guessLabel.pack(pady=(30, 0))
    validLabel.pack()
    greenLabel.pack()
    yellowLabel.pack()
    grayLabel.pack()
    pressEnterLabel.pack()
    backButton.pack()
    quitButton.pack(in_=frame)
    frame.pack()

wordList = []

for word in wordnet.words():
    if word.isalpha():
        wordList.append(word.lower())

randomWord = random.choice(wordList)
window = tk.Tk()
window.geometry('500x500')
window.title('Wordle')
print(randomWord)
frameForWindow = tk.Frame(master=window)
coins = 1000
hints = 0
displayMainWindow(frameForWindow)
window.mainloop()
import nltk
from nltk.corpus import brown
from nltk.corpus import words
import random
from flask import Flask, jsonify, request, render_template

# --- Word list generation (from your original code) ---
# It's good practice to do this once when the server starts.
print("Initializing word list...")
wordList = []
# Ensure NLTK data is downloaded. In a real server, you'd do this in a setup script.
try:
    brown_words = brown.words()
    english_words = words.words()
except LookupError:
    print("NLTK data not found. Downloading...")
    nltk.download('brown')
    nltk.download('words')
    brown_words = brown.words()
    english_words = words.words()

wordFrequency = nltk.FreqDist(brown_words)
for word in english_words:
    # We'll use 5-letter words for a consistent game board
    if len(word) == 5 and word.isalpha():
        if word.lower() in wordFrequency and wordFrequency[word.lower()] > 10:
            wordList.append(word.lower())
print(f"Word list initialized with {len(wordList)} words.")

# --- Flask App Setup ---
app = Flask(__name__)

# This dictionary will store the secret word for the current game.
# Note: This simple approach only supports one game at a time for all users.
game_state = {
    'random_word': ''
}

@app.route('/')
def home():
    """Serves the main HTML file which contains all our game's UI and logic."""
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """Chooses a new word and sends its length to the frontend."""
    # The frontend doesn't need difficulty info, but we receive it anyway.
    # difficulty = request.get_json().get('difficulty')
    
    game_state['random_word'] = random.choice(wordList)
    # For debugging purposes, we print the word on the server console
    print(f"New game started. Word is: {game_state['random_word']}") 
    
    # We only need to tell the frontend the length of the word to build the grid.
    return jsonify({'word_length': len(game_state['random_word'])})

@app.route('/check_guess', methods=['POST'])
def check_guess_route():
    """Checks the user's guess against the random word."""
    data = request.get_json()
    guessed_word = data.get('guess', '').lower()
    
    random_word = game_state['random_word']
    
    if not random_word:
        return jsonify({'error': 'Game not started'}), 400
        
    if len(guessed_word) != len(random_word):
        return jsonify({'error': 'Invalid guess length'}), 400

    results = []
    # Use a copy of the random word to handle duplicate letters correctly
    word_copy = list(random_word)

    # First pass for correct (green) letters
    for i in range(len(random_word)):
        if guessed_word[i] == random_word[i]:
            results.append('green')
            word_copy[i] = None # Mark this letter as used
        else:
            results.append('') # Placeholder

    # Second pass for present but wrong spot (yellow) letters
    for i in range(len(random_word)):
        if results[i] == '': # If not already marked green
            if guessed_word[i] in word_copy:
                results[i] = 'yellow'
                # Mark the first occurrence of this letter in the copy as used
                word_copy[word_copy.index(guessed_word[i])] = None
            else:
                results[i] = 'gray'
            
    is_correct = (guessed_word == random_word)
    
    response = {'results': results, 'is_correct': is_correct}
    if not is_correct and data.get('is_last_guess', False):
        response['answer'] = random_word

    return jsonify(response)

if __name__ == '__main__':
    # The 'host' parameter makes the server accessible from other devices on your network
    app.run(debug=True, host='0.0.0.0')


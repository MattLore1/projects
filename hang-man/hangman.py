import random

words = ['wizard', 'turtle', 'queen', 'checkmate', 'discworld', 'dragon', 'luggage', 'tower', 'sword', 'carrot', 'granny', 'moist', 'dwarves']

# List of hangman stages, 7 to 0 attempts left
hangman_stages = [
    """  _______
  |/    |      
  |            
  |            
  |            
  |_________   
 /|\       |   
/ | \      |   
6 Guesses Left!""",
    """  _______
  |/    |      
  |     O      
  |            
  |            
  |_________   
 /|\       |   
/ | \      |   
5 Guesses Left!""",
    """  _______
  |/    |      
  |     O      
  |     |      
  |            
  |_________   
 /|\       |   
/ | \      |   
4 Guesses Left!""",
    """  _______
  |/    |      
  |     O      
  |    /|      
  |            
  |_________   
 /|\       |   
/ | \      |   
3 Guesses Left!""",
    """  _______
  |/    |      
  |     O      
  |    /|\     
  |            
  |_________   
 /|\       |   
/ | \      |   
2 Guesses Left!""",
    """  _______
  |/    |      
  |     O      
  |    /|\     
  |    /       
  |_________   
 /|\       |   
/ | \      |   
1 Guess Left!""",
    """  _______
  |/    |      
  |     O      
  |    /|\     
  |    / \    
  |_________   
 /|\       |   
/ | \      |   
Game Over!""",
]

# Start game
chosen_word = random.choice(words)
word_display = ["_" for _ in chosen_word]
wrong_guesses = 0
max_attempts = len(hangman_stages) - 1

#Main game loop, was first made with a series of if statements. Learned how to use an array to display the hangman stages to make it cleaner.
print("Welcome to Hangman!")
while wrong_guesses < max_attempts and "_" in word_display:
    print("\nCurrent word: " + " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print(hangman_stages[wrong_guesses])

if "_" not in word_display:
    print(f"\nCongratulations! You guessed the word: {''.join(word_display)} 🎉")
else:
    print(f"\nThe word was: {chosen_word}. Better luck next time!")
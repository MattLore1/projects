#sets computer's moves
computer = ["Rock", "Paper", "Scissors"]
            
def round_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or (player == "Scissors" and computer == "Paper") or (player == "Paper" and computer == "Rock"):
        return "You win the round!"
    else:
        return "You lost the round!" 

player_score = 0
computer_score = 0

def win_count(player, computer, player_score, computer_score):
    result = round_winner(player, computer)
    if result == "You win the round!":
        player_score += 1
    elif result == "You lost the round!":
        computer_score += 1
    return player_score, computer_score

#Sets the rules of the game
print("ITS ROCK PAPER SCISSORS TIME BABY! \n   The rules:\n     -Best of 3 wins!\n     -Rock crushes Scissors,\n     -Scissors cuts Paper, \n     -Paper covers Rock.")
import random

while player_score < 3 and computer_score < 3:
    player = input("\nYour choice (Rock, Paper, Scissors): ").title()
    comp = random.choice(computer)
    print(f"The computer choose: {comp}")
    result = round_winner(player, comp)
    print(result)
    player_score, computer_score = win_count(player, comp, player_score, computer_score)
    print(f"Score - You: {player_score}, Computer: {computer_score}")

if player_score == 3:
    print("You've won the match!\n")
elif computer_score == 3:
    print("You've lost the match!\n")
import cowsay
import random
import os
import sys

def get_choices():
  cowsay.cow("Welcome to Rock, Paper, Scissors!")
  player_choice = input("\nEnter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  cow_choice = f"You chose {player.lower()}, Computer chose {computer}"
  if player == computer:
    os.system('clear')
    cowsay.cow(cow_choice)
    return("It's a tie!")
  elif player.casefold() == "rock":
    if computer == "scissors":
      os.system('clear')
      cowsay.cow(cow_choice)
      return("Rock smashes scissors! You win!")
    else:
      os.system('clear')
      cowsay.cow(cow_choice)
      return("Paper covers rock! You lose.")
  elif player.casefold() == "paper":
    if computer == "rock":
      os.system('clear')
      cowsay.cow(cow_choice)
      return("Paper covers rock! You win!")
    else:
      os.system('clear')
      cowsay.cow(cow_choice)
      return("Scissors cuts paper! You lose.")
  elif player.casefold() == "scissors":
    if computer == "paper":
      os.system('clear')
      cowsay.cow(cow_choice)
      return("Scissors cuts paper! You win!")
    else:
      os.system('clear')
      cowsay.cow(cow_choice)
      return("Rock smashes scissors! You lose.")


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

replay = input("\nWould you like to play again? (Yes/No) ")
if replay.casefold() == "no":
  os.system('clear')
  cowsay.cow("Thanks for playing!")
elif replay.casefold() == "yes":
  os.system('clear')
  os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
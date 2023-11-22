# Step 1
import random
from easymode import word_list as e_list
from hardmode import word_list as h_list
from art import logo, stages

# Select a random word and save to variable
def select_mode():
  print(logo)
  game_mode = input('Select e for easy mode or h for hard mode: ')
  if game_mode == 'e':
    return e_list
  elif game_mode == 'h':
    return h_list
  else:
    print('Not a valid input')

mode = select_mode()

def game(mode):
  selected_word = random.choice(mode)
  lives = 6
  # Allow user input for a letter and lowercase the letter
  placeholder = ['_'] * len(selected_word)

  while '_' in placeholder:
    guessed_letter = input('Guess a letter: ').lower()
    for i in range(len(selected_word)):
      if selected_word[i] == guessed_letter:
        placeholder[i] = guessed_letter
    if guessed_letter not in selected_word:
      lives -= 1
      if lives == 0:
          print(stages[lives])
          print('You Lose')       
          break
    print(stages[lives])
    print(placeholder)
    if '_' not in placeholder:
        print('You win')

game(mode)

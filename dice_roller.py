#! /usr/bin/python3

def main():

  import random
  dice_rolls = int(input('How many dice would you like to roll?\n'))
  dice_sides = int(input('How many sided die?\n'))
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_sides)
    dice_sum = dice_sum + roll
    if roll == 1:
      print(f'You rolled a {roll}! Critical Failure')
    elif roll == dice_sides:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
  print(f'A total of {dice_sum}')
if __name__== "__main__":
  main()

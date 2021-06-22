from art import logo, vs
from game_data import data
import random
from replit import clear()
def format_data(account):
  """Format the account data into printable format"""
  account_name = account["name"]
  account_descript = account["description"]
  account_country = account["country"]  
  return f"{account_name} a {account_descript} from {account_country}"

print(logo)
score = 0
account_b = random.choice(data)
game_continue = True

while game_continue:
  # Making account at position B become the next account at position A
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)


  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  #who has more followers 
  account_follower_a = account_a["follower_count"]
  account_follower_b = account_b["follower_count"]

  guess = input("Who has more followers. Type 'A'or 'B': ").lower()
  def check_answer(guess,account_follower_a, account_follower_b):
    """take the user guess and follower count and return if they got it right"""
    if account_follower_a > account_follower_b:
      return guess == "a"
    else:
      return guess == "b"


  is_correct = check_answer(guess, account_follower_a, account_follower_b)
  clear()
  print(logo)

  if is_correct:
    score += 1
    print(f"You right. Your current score is: {score}")
  else:
    game_continue = False
    print(f"Sorry, that's wrong. Your final score is {score}")




#follower count



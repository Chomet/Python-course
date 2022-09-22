from art import logo, vs
from game_data import data
##from replit import clear
import random

score = 0
current = random.choice(data)
print(logo)
while True:
  print(f"Compare A: {current['name']}, {current['description']} from {current['country']}")
  print(vs)
  while True:
    current2 = random.choice(data)
    if current2["name"] != current["name"]:
      break
  print(f"Against B: {current2['name']}, {current2['description']} from {current2['country']}")
  choice = input("Who has more followers: A or B: ").upper()
  if choice == "A":
    if current["follower_count"] >= current2["follower_count"]:
      ##clear()
      print(logo)
      current = current2
      score += 1
    else:
      ##clear()
      print(logo)
      print(f"Defeat! You final score is {score}")
      break
  elif choice == "B":
    if current["follower_count"] <= current2["follower_count"]:
      current = current2
      ##clear()
      print(logo)
      score += 1
    else:
      ##clear()
      print(logo)
      print(f"Defeat! You final score is {score}")
      break
  else:
    ##clear()
    print(logo)
    print(f"Unknown choice! You final score is {score}")
    break
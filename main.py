import random

user_input = input("Hello, how are you? If you want to stop talking, type \"quit\": ")

good_answers = ["good","great","well","fine","okay","yes","ok"]
bad_answers = ["bad","not good","terrible","no"]

responses = ["Nice!","Cool!"]

def good_or_bad(answer,good,bad):
  if answer in good_answers:
    print(good)
  elif answer in bad_answers:
    print(bad)
  else:
    print("I'm not sure what to say to that")

if user_input != "quit":
  good_or_bad(user_input,"I'm glad to hear that!","I'm sorry to hear that.")

if user_input != "quit":
  user_input = input("Where are you from? ")
if user_input != "quit":
  print(random.choice(responses))

if user_input != "quit":
  user_input = input("How many siblings do you have? ")
if user_input != "quit":
  if int(user_input) == 0:
    user_input = input("What's it like being an only child? ")
    good_or_bad(user_input,"I'm glad to hear that!","I'm sorry to hear that.")
  elif int(user_input) == 1:
    user_input = input("Cool! Do you have a brother or a sister? ")
    print(random.choice(responses))
  else:
    print(random.choice(responses))

if user_input != "quit":
  user_input = input("What's a hobby of yours? ")
if user_input != "quit":
  user_input = input("That's pretty cool! Tell me more!\nType something: ")
if user_input != "quit":
  user_input = input("How long have you had that hobby? ")
if user_input != "quit":
  print(random.choice(responses))

if user_input != "quit":
  user_input = input("Do you go to school? ")
if user_input != "quit":
  if user_input == "yes":
    user_input = input("Do you enjoy it? ")
    good_or_bad(user_input,"I'm glad to hear that!","I definitely hear ya. School sucks sometimes.")
  else:
    user_input("Ok, so what do you do for a living? ")
    user_input("Is this something you enjoy")
    good_or_bad(user_input,"I'm glad to hear that!","I'm sorry to hear that.")
if user_input != "quit":
  user_input = input("Just tell me more about yourself in general. Type \"quit\" if you don't want to talk anymore: ")
while user_input != "quit":
  print(random.choice(responses))
  user_input = ("Type something: ")
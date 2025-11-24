import random

print("🎮 Rock – Paper – Scissors Game")
options = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0

while True:
    user = input("Enter rock / paper / scissor (or 'exit' to quit): ").lower()
    
    if user == "exit":
        print("\nFinal Scores:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing! 👋")
        break
    
    if user not in options:
        print("Invalid input! Try again.")
        continue

    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("Result: It's a draw!")
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("You win! 😎")
        user_score += 1
    else:
        print("Computer wins! 🤖")
        computer_score += 1


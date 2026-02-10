import random

wins = 0
losses = 0

while True:
    print("\n🪙 Coin Toss Game 🪙")
    print("1. Toss the coin")
    print("2. View score")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        guess = input('Guess "Heads" or "Tails": ')
        coin = random.choice(["Heads", "Tails"])  # Randomly select Heads or Tails

        print("The coin landed on:", coin)

        if guess == coin:
            print("🎉 You guessed correctly!")
            wins = wins + 1
        else:
            print("❌ Wrong guess!")
            losses = losses + 1

    elif choice == "2":
        print("✅ Wins:", wins, "| ❌ Losses:", losses)

    elif choice == "3":
        print("Goodbye! 🪙")
        break

    else:
        print("❌ Invalid choice, please enter 1-3.")

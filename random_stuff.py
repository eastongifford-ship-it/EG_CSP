# eg 7th advanced Guess the Number with custom mode, streaks, and achievements
import random
import time

leaderboard = []
player_streaks = {}

def get_difficulty():
    print("Choose your difficulty:")
    print("1. Easy (1-50, 12 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")
    print("4. Custom (choose your own range and attempts)")
    while True:
        choice = input("Enter 1, 2, 3, or 4: ")
        if choice == "1":
            return 1, 50, 12
        elif choice == "2":
            return 2, 100, 10
        elif choice == "3":
            return 3, 200, 7
        elif choice == "4":
            try:
                max_num = int(input("Enter the maximum number (min 10): "))
                max_attempts = int(input("Enter the number of attempts (min 1): "))
                if max_num >= 10 and max_attempts >= 1:
                    return 4, max_num, max_attempts
                else:
                    print("Please enter valid numbers.")
            except ValueError:
                print("Please enter valid numbers.")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def show_leaderboard():
    if not leaderboard:
        print("\nNo scores yet. Be the first on the leaderboard!\n")
        return
    print("\n🏆 Leaderboard (Top 5 Fastest Wins):")
    sorted_lb = sorted(leaderboard, key=lambda x: (x['attempts'], x['time']))
    for i, entry in enumerate(sorted_lb[:5], 1):
        print(f"{i}. {entry['name']} - {entry['attempts']} attempts, {entry['time']:.1f} seconds (Difficulty: {entry['difficulty']})")
    print()

def get_achievement(attempts, elapsed, difficulty, max_attempts):
    achievements = []
    if attempts == 1:
        achievements.append("🎯 First Try!")
    if elapsed < 10:
        achievements.append("⚡ Lightning Fast!")
    if attempts <= max_attempts // 2:
        achievements.append("🏅 Efficient Guesser!")
    if difficulty == 3 and attempts <= 3:
        achievements.append("🔥 Hard Mode Master!")
    if difficulty == 4:
        achievements.append("🛠️ Custom Challenger!")
    return achievements

def update_streak(player_name, won):
    if player_name not in player_streaks:
        player_streaks[player_name] = 0
    if won:
        player_streaks[player_name] += 1
    else:
        player_streaks[player_name] = 0
    return player_streaks[player_name]

def guess_the_number():
    print("🎲 Welcome to Guess the Number!")
    player_name = input("Enter your name: ").strip() or "Player"
    show_leaderboard()
    difficulty, max_num, max_attempts = get_difficulty()
    print(f"I'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

    number = random.randint(1, max_num)
    attempts = 0
    previous_guesses = []
    start_time = time.time()

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            if guess < 1 or guess > max_num:
                print(f"Your guess must be between 1 and {max_num}.")
                continue

            if guess in previous_guesses:
                print("You've already guessed that number! Try a different one.")
                continue

            previous_guesses.append(guess)
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
                if number - guess <= max_num // 10:
                    print("Hint: You're very close!")
            elif guess > number:
                print("Too high! Try again.")
                if guess - number <= max_num // 10:
                    print("Hint: You're very close!")
            else:
                elapsed = time.time() - start_time
                print(f"🎉 You got it in {attempts} attempts and {elapsed:.1f} seconds!")
                achievements = get_achievement(attempts, elapsed, difficulty, max_attempts)
                if achievements:
                    print("Achievements unlocked:")
                    for ach in achievements:
                        print(ach)
                leaderboard.append({
                    'name': player_name,
                    'attempts': attempts,
                    'time': elapsed,
                    'difficulty': {1: 'Easy', 2: 'Medium', 3: 'Hard', 4: 'Custom'}[difficulty]
                })
                streak = update_streak(player_name, True)
                print(f"🔥 Current win streak: {streak}")
                break
        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"😢 Sorry, you're out of attempts. The number was {number}.")
        streak = update_streak(player_name, False)
        print(f"💔 Your win streak has been reset.")

    print("\nYour guesses were:", previous_guesses)
    print(f"Smallest guess: {min(previous_guesses)} | Largest guess: {max(previous_guesses)}")
    show_leaderboard()
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        print("\nRestarting game...\n")
        guess_the_number()
    else:
        print("Thanks for playing! Goodbye.")

guess_the_number()
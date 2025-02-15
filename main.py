import random

def toss_coin():
    # Simulate a single coin toss
    return random.choice(["Heads", "Tails"])

def simulate_coin_flips(num_flips):
    # Initialize a dictionary to keep track of the counts
    results = {"Heads": 0, "Tails": 0}
    for _ in range(num_flips):
        result = toss_coin()
        results[result] += 1
    return results

def print_results(results, total_flips):
    # Print out the counts and percentage for each outcome
    print("\nCoin Toss Results:")
    for side, count in results.items():
        percent = (count / total_flips) * 100
        print(f"{side}: {count} ({percent:.1f}%)")

def main():
    print("Welcome to the Virtual Coin Toss!\n")
    
    while True:
        try:
            # Get user input for the number of coin flips
            num = int(input("Enter the number of times you want to flip the coin: "))
            if num < 1:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("That's not a valid number. Try again!")
            continue
        
        # Simulate the coin tosses and display the results
        results = simulate_coin_flips(num)
        print_results(results, num)
        
        # Ask if the user wants to run another session
        again = input("\nDo you want to flip the coin again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()

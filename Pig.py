import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2 - 6): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 6:
            break
        else:
            print("Must be 2-6 players: ")
    else:
        print("Invalid!")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nIt's player ", player_idx + 1, "'s turn!")
        print("Your score is: ", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("If you wanna roll press (y): ")
            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled 1,your turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled ", value)

            print("Your score is: ", current_score)
            
        player_scores[player_idx] += current_score
        print("Your total score is :", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player",winning_idx + 1, "won with score: ", max_score)
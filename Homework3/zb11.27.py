def run_team_manager():
    players = {}
    count = 1

    while count <= 5:
        jersey = int(input(f"Enter player {count}'s jersey number:\n"))
        rating = int(input(f"Enter player {count}'s rating:\n"))
        players[jersey] = rating
        count += 1
        print()

    def print_roster():
        print("ROSTER")
        for j in sorted(players):
            print(f"Jersey number: {j}, Rating: {players[j]}")

    print_roster()

    while True:
        print("\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
        choice = input("Choose an option:\n")

        if choice == "q":
            break
        elif choice == "o":
            print_roster()
        elif choice == "a":
            new_jersey = int(input("Enter a new player's jersey number:\n"))
            new_rating = int(input("Enter the player's rating:\n"))
            players[new_jersey] = new_rating
        elif choice == "d":
            jersey_to_remove = int(input("Enter a jersey number:\n"))
            players.pop(jersey_to_remove, None)
        elif choice == "u":
            jersey_to_update = int(input("Enter a jersey number:\n"))
            if jersey_to_update in players:
                players[jersey_to_update] = int(input("Enter a new rating for player:\n"))
        elif choice == "r":
            threshold_rating = int(input("Enter a rating:\n"))
            print(f"ABOVE {threshold_rating}")
            for j, r in sorted(players.items()):
                if r > threshold_rating:
                    print(f"Jersey number: {j}, Rating: {r}")

if __name__ == "__main__":
    run_team_manager()

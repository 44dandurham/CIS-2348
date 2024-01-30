def get_age():
    entered_age = int(input("Please enter your age:"))
    if not 18 <= entered_age <= 75:
        raise ValueError("Invalid age.")
    return entered_age

def fat_burning_heart_rate(individual_age):
    optimal_rate = 0.7 * (220 - individual_age)
    return optimal_rate

if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")

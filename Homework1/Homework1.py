print('Birthday Calculator')

current_date = input('Enter the current date (MM DD YYYY): ').split()
birth_date = input('Enter your birth date (MM DD YYYY): ').split()



def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def calculate_age(current_month, current_day, current_year, birth_month, birth_day, birth_year):
    if (current_month, current_day) < (birth_month, birth_day):
        age = current_year - birth_year - 1
    else:
        age = current_year - birth_year
    return age


age = calculate_age(current_month, current_day, current_year, birth_month, birth_day, birth_year)

if (current_month, current_day) == (birth_month, birth_day):
    print('Happy Birthday')

print("You are", age, "years old.")

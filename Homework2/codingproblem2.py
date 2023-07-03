#Daniel Durham 1851947

from datetime import datetime

def convert_date(date_str):
    date = datetime.strptime(date_str, "%B %d, %Y")
    return date.strftime("%B %d, %Y")

current_date = datetime.now()

while True:
    date_input = input()
    if date_input == '-1':
        break

    month = date_input.find(" ")
    comma = date_input.find(",")
    space = date_input.find(" ", comma)

    if month != -1 and comma != -1 and space != -1:
        format_date = convert_date(date_input)
        date = datetime.strptime(date_input, "%B %d, %Y")
        if date <= current_date:
            print(format_date)
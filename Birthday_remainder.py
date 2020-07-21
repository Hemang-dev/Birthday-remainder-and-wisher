import datetime


def validate_month_date(month, date):
    '''Check if month and date entered is valid'''

    if month in range(1, 13) and date in range(1, 32):
        return True

    return False


def get_all_birthdates():
    '''Get all birthdates stored in a file'''

    try:
        with open('birthday.txt', 'r') as f:
            return [line.strip('\n') for line in f.readlines()]

    except FileNotFoundError:    # If 'birthday.txt' does not exists then creating an empty 'birthday.txt'
        with open('birthday.txt', 'w'):
            return []


def write_to_file(contents):
    with open('birthday.txt', 'w') as f:
        for content in contents:
            f.write(f'{content}\n')


def add_birthdtes():
    '''Add birthdates if not already in file'''

    birthdates = get_all_birthdates()

    name = input('\nWhose birthday is it? ').title()
    date = input('Enter date in YYYY-MM-DD: ')
    split_date = date.split('-')

    while not validate_month_date(int(split_date[1]), int(split_date[2])):   # Looping until we get valid month and date
        print('\nInvalid date.')

        date = input('Enter date in YYYY-MM-DD: ')
        split_date = date.split('-')

    write = f'{name} : {date}'    # ':' is delimiter for seperating name and birthdates

    if write in birthdates:
        print(f'\n{name}:{date} already exists in file')

    else:
        birthdates.append(write)
        birthdates.sort(key=len)    # Sorting according to the length in ascending order

        write_to_file(birthdates)


def main():
    '''Entry point of the program'''

    current_date = datetime.date.today()
    option = input('Do you want to add birthdates (y/n)?').lower()

    if option == 'y':
        add_birthdtes()

    lines = get_all_birthdates()

    for line in lines:
        split_line = line.split(' : ')
        name = split_line[0]
        date = split_line[1].split('-')

        month, day = int(date[1]), int(date[2])

        if current_date.month == month and current_date.day == day:
            print(f'\nToday is {name}\'s birthday')


if __name__ == '__main__':
    main()

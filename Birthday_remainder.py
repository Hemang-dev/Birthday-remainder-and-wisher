import datetime


current_date = str((datetime.date.today()))
current_date_lst = current_date.split('-')
# this will convert current date to list which helps to compare with preadded log
# print(current_dat)
bday_log = [
    ['1999', '10', '19'],
    ['1999', '04', '21']
]
person = ['Yash', 'Ayushi']
i = 1  # this will help during loop
add = input('To add birthday type y:')
if add.lower() == 'y':
    new = str(input('Add birthday in format yyyy-mm-dd:'))
    new_lst = new.split('-')
    # print(new_lst)
    name = input('Whose bday?')
    person.append(name)
    bday_log.append(new_lst)
    i += 1
# print(person)
# print(bday_log)
j = 1  # this is for bday month and date
while i >= 0:
    # current_dat[1] == bd[i][1] this will check if current month is same as birth month  and current date is same as
    # birth date as per preadded log
    if current_date_lst[1] == bday_log[i][j] and current_date_lst[2] == bday_log[i][j + 1]:
        yes = True
        age = int(current_date_lst[0]) - int(bday_log[i][0])
        print(f" It's {person[i]}'s {age} Birthday")
    i -= 1

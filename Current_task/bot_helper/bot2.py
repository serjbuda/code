import csv

def save_user_info(name, email, phone):
    with open('user_info.csv', mode='a') as user_info_file:
        user_writer = csv.writer(user_info_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        user_writer.writerow([name, email, phone])
        print(f"User information saved: {name}, {email}, {phone}")

while True:
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    save_user_info(name, email, phone)

    choice = input("Do you want to add another user? (y/n)")
    if choice.lower() == 'n':
        break

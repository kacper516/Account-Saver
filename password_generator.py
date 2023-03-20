import random
import pyperclip  # to copy generated password
from tkinter import messagebox  # to make a pop-up

def password_maker(number_letters, number_numbers, number_symbols):
    """This function will generate a new password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(number_letters)]
    symbols_list = [random.choice(symbols) for _ in range(number_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(number_numbers)]
    password_list = letters_list + symbols_list + numbers_list  # append 3 list in one

    random.shuffle(password_list)  # to shuffle numbers, symbols and letters

    password = "".join(password_list)  # string with combine of every element in list

    return password

def check_entries(letters, numbers, symbols):
    """This function will check if entries is good or not"""

    if letters == "" or numbers == "" or symbols == "":
        messagebox.showwarning(title="Error", message="Don't leave any fields empty!")
        return ""
    else:
        while True:  # while user want to change his password
            password = password_maker(int(letters), int(numbers), int(symbols))
            check_if_save = messagebox.askyesno(title="New password", message=f"Generated password is: {password}."
                                                                              f"\nIs it okay to save?")
            if check_if_save:
                pyperclip.copy(password)  # copy generated password

                return password


def check_message(website, email, password):
    """This function will check some conditions of given data"""
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Error", message="Don't leave any fields empty!")
        return False
    else:
        check_if_save = messagebox.askyesno(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                                   f"Password: {password}\nIs it okay to save?")
        if check_if_save:
            return True
        else:
            return False

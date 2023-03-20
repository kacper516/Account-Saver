import tkinter
import json
from password_generator import *


def search_button():
    """This function will search for saved password"""
    try:
        website = entry_website.get()
        with open("data.json", "r") as data_file:
            data = json.load(data_file)  # receive old file
            website_account = data[website]
            messagebox.showinfo(title="Account Info",
                                message=f"This is your account in {website}\nEmail: {website_account['email']}"
                                        f"\nPassword: {website_account['password']}")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
    except KeyError as error_message:
        messagebox.showwarning(title="Error", message="No details for the website you given exist")


def password_button():
    """This function will fill entry with new generate password with new window app"""

    def button_gen():
        """This is what happen when user click the generate button"""
        letters = letter_entry.get()
        numbers = numbers_entry.get()
        symbols = symbols_entry.get()

        password = check_entries(letters, numbers, symbols)
        if password != "":
            entry_password.delete(0, "end")
            entry_password.insert(0, password)
            new_window.destroy()  # to close this windows in this attempt

    new_window = tkinter.Toplevel(window)
    new_window.title("Password maker")
    new_window.minsize()
    new_window.config(pady=20, padx=20)

    # labels
    label_letters = tkinter.Label(new_window, text="Number of letters: ")
    label_letters.grid(row=0, column=0)

    label_numbers = tkinter.Label(new_window, text="Number of numbers: ")
    label_numbers.grid(row=1, column=0)

    label_symbols = tkinter.Label(new_window, text="Number of symbols: ")
    label_symbols.grid(row=2, column=0)

    # entries

    letter_entry = tkinter.Entry(new_window)
    letter_entry.grid(row=0, column=1, sticky="EW")
    letter_entry.focus()

    numbers_entry = tkinter.Entry(new_window)
    numbers_entry.grid(row=1, column=1, sticky="EW")

    symbols_entry = tkinter.Entry(new_window)
    symbols_entry.grid(row=2, column=1, sticky="EW")

    # buttons
    generate_button = tkinter.Button(new_window, text="Generate password", command=button_gen)
    generate_button.grid(row=3, column=0, columnspan=2)


def save_password():
    """This function will save inputs to the file"""
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if check_message(website, email, password):
        # JSON file
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # receive old file
                data.update(new_data)  # update file with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # save to file actual data
        finally:
            clear_entries()  # do it anyway


def clear_entries():
    """This function will clear entries while save account"""
    entry_website.delete(0, "end")
    entry_email.delete(0, "end")
    entry_password.delete(0, "end")


"""Main window"""
window = tkinter.Tk()
window.title("Password Generator")
window.minsize()
window.config(padx=25, pady=25)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
label_website = tkinter.Label()
label_website.config(text="Website:")
label_website.grid(row=1, column=0)

label_email = tkinter.Label()
label_email.config(text="Email/Username:")
label_email.grid(row=2, column=0)

label_password = tkinter.Label()
label_password.config(text="Password:")
label_password.grid(row=3, column=0)

# Entries
entry_website = tkinter.Entry()
entry_website.grid(row=1, column=1, sticky="EW")
entry_website.focus()  # to put mouse here

entry_email = tkinter.Entry()
entry_email.grid(row=2, column=1, columnspan=2, sticky="EW")

entry_password = tkinter.Entry()
entry_password.grid(row=3, column=1, sticky="EW")

# Buttons
button_generate = tkinter.Button(text="Generate Password", command=password_button)
button_generate.grid(row=3, column=2, sticky="EW")

button_add = tkinter.Button(text="ADD", command=save_password)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")

button_search = tkinter.Button(text="Search", command=search_button)
button_search.grid(row=1, column=2, sticky="EW")

window.mainloop()

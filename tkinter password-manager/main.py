from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
#data.txt
directory = '/Users/linusgao/Documents/Python/100-Days-Of-Python/Day 29/password-manager-start'

def findPassword():
    websiteInfo = websiteEntry.get()
    with open('data.json', 'r') as file:
        try:
            data = json.load(file)
            print(data)
            print(data.keys())
            
            if websiteInfo in data.keys():
                emailInfo = data[websiteInfo]["email"]
                passwordInfo = data[websiteInfo]["password"]
                messagebox.showinfo(title="Search Successful", message=f"{websiteInfo}\nEmail: {emailInfo}"
                                f"\nPassword: {passwordInfo}\n")
            else:
                messagebox.showinfo(title="No Search Found", message="No details for the website exists")
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(title="File not found", message="No Data File Found")

def writeToFile(newData):
        try:
            with open('data.json', 'r') as file:
            # Ensure the file exists and handle reading and updating data
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
         # Updating old data with new data
        data.update(newData)
        with open("data.json", "w") as file:
            #Saving updated data
            json.dump(data, file, indent=4)
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)

entries = os.listdir(directory)
def save_to_file(): 
    websiteInfo = websiteEntry.get()
    emailInfo = emailEntry.get()
    passwordInfo = passwordEntry.get()
    newData = {websiteInfo: {
        "email": emailInfo,
        "password": passwordInfo
    }}
    
    if len(websiteInfo) == 0 or len(passwordInfo) == 0:
        messagebox.showinfo(title="Invalid Information", message="Please do not leave anything blank")
    else:
        confirm = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {emailInfo}"
                            f"\nPassword: {passwordInfo} \nIs it ok to save?")
        if confirm:
            writeToFile(newData)
                    
                    
    
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

#Lock
canvas = Canvas(window, width=200, height=200)
lockImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lockImage)
canvas.grid(row=0, column=1)

#Website
website = Label(window, text="Website:")
website.grid(row=1, column=0)
websiteEntry = Entry(window, width=21)
websiteEntry.grid(row=1, column=1, columnspan=2, sticky="w")
website.focus()

searchEmail = Button(window, text="Search", command=findPassword)
searchEmail.grid(row=1, column=2, sticky="w")

#Email
email = Label(window, text="Email/Username:")
email.grid(row=2, column=0)
emailEntry = Entry(window, width=35)
emailEntry.grid(row=2, column=1, columnspan=2, sticky="w")
emailEntry.insert(0, "CSA@gmail.com")

#Password
password = Label(window, text="Password:")
password.grid(row=3, column=0, sticky="w")
passwordEntry = Entry(window, width=21)
passwordEntry.grid(row=3, column=1, sticky="w")

generatePass = Button(window, text="Generate Password", command=generate_password)
generatePass.grid(row=3, column=2, sticky="w")

#Add
add = Button(window, text="Add", command=save_to_file)
add.config(width=36)
add.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
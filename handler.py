import os
import time
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox


def os_apps_calculator():
    os.system("cls")
    print("Enter an Equation (example .'9 + 10', '50 * 100', '10 / 2')")
    try:
        eqt = input("> ")
        print(f"=> {eval(eqt)}")
        time.sleep(2)
        os.system("cls")
    except Exception as e:
        print("Invalid Equation, Error Occurred")
        time.sleep(2)
        os.system("cls")

    return 0


def os_apps_calculatorADV():
    pass


def os_mk_file():
    os.system("cls")
    print("Choose a Directory to Save The File :")
    user_file_dir = filedialog.askdirectory(initialdir=".\\root\\", title="Where to Save File? (Folder)")
    if user_file_dir is None:
        print("Error!")
        return 1
    else:
        print("")
        user_file_name = input("File Name > ")
        user_file_ext = input("File Extension (example- .txt or .html or .abc) > ")
        full_file_dir_name = user_file_dir + "/" + user_file_name + user_file_ext
        try:
            with open(full_file_dir_name, "x") as file:
                file.write("")
                file.close()
            print("Created File at " + full_file_dir_name)
            time.sleep(2)
            return 0
        except Exception as e:
            print("Error!, Check if File Already Exists in the Directory!")
            return 1


def os_mk_dir():
    os.system("cls")
    user_folder_name = input("Enter New Folder Name > ")
    path = r"./root/users/" + user_folder_name
    access_token = 0o755
    os.mkdir(path, access_token)
    print("Successfully Created Folder at " + path)
    time.sleep(2)
    return 0


def os_apps_weather():
    os.startfile(".\\root\\bin\\weather_app\\main.exe")

    return 0


user_file_text = ""

from tkinter import filedialog as fd


def os_text_editor():
    global user_file_text

    # user_file_name_text_ask = filedialog.askopenfile(title="Select a Text File (.txt) :",
    #                                                 filetypes=[("Text Files", ['.txt'])])

    user_file_name_text = fd.askopenfilename()

    # user_file_name_text = user_file_name_text_ask.read()

    if not user_file_name_text:
        return 1

    with open(user_file_name_text) as user_file:
        user_file_text = user_file.read()

    root = Tk()
    root.title("Text Editor for PyOS")
    root.geometry("300x500")

    text_box = Text(root, width=290)
    text_box.insert("end", user_file_text)
    text_box.pack(pady=10)

    cancel_btn = Button(root, text="Cancel", font=("Arial", 12), command=root.destroy)
    cancel_btn.pack(side=BOTTOM, pady=10)

    def save_changes():
        new_text = text_box.get(1.0, 'end')

        if user_file_text == new_text:
            messagebox.showwarning("No Change!", "No Text Edited")
            return

        with open(user_file_name_text, 'w') as new_file:
            new_file.write(new_text)
            messagebox.showinfo("Success!", "Successfully Changed Text!")
            cancel_btn["text"] = "Exit"

        return 0

    submit_btn = Button(root, text="Save", font=("Arial", 12), command=save_changes)
    submit_btn.pack(side=BOTTOM, pady=10)

    root.mainloop()
    return 0

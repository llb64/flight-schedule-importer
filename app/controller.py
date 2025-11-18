from tkinter import Tk
from tkinter.filedialog import askopenfilename

import model
import view

def flight_upload_btn_handler():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)

def login_handler(parent, username, password):
    users = model.load_users()
    if any(user["username"] == username and user["password"] == password for user in users):
        view.flight_overview_page(parent)

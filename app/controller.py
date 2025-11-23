from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename

import model
import view

def flight_upload_btn_handler():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)

def create_flight_btn_handler(parent, carrier, flight_number, station, departure_date, departure_hour, departure_minute, expected_date, expected_hour, expected_minute):
    departure_string = f"{departure_date} {departure_hour}:{departure_minute}"
    expected_string = f"{expected_date} {expected_hour}:{expected_minute}"
    flight_csv = f"{carrier},{flight_number},{station},{departure_string},{expected_string},"
    model.add_flight(flight_csv)
    view.flight_overview_page(parent)

def delete_flight(event, parent):
    item = int(event.widget.identify("item", event.x, event.y))
    model.delete_flight(item)
    view.flight_overview_page(parent)
    messagebox.showinfo(message="Flight successfully deleted")

def login_handler(parent, username, password):
    users = model.load_users()
    if any(user["username"] == username and user["password"] == password for user in users):
        view.flight_overview_page(parent)
        return
    messagebox.showerror(message="Username or password incorrect")

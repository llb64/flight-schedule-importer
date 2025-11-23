from tkinter import ttk
from tkcalendar import DateEntry

import model
import controller

# === Utils ===

def destroy_all_widgets(root):
    """Destroys all child widgets, used for page navigation."""
    widgets = root.winfo_children()
    for widget in widgets:
        widget.destroy()
    parent = root.master
    root.destroy()
    return parent

# === Pages ===

def login_page(parent):
    root = destroy_all_widgets(parent)
    frame = create_frame(root, 20)
    insert_title(frame, "Login Page")
    insert_login_inputs(frame)
    frame.pack(fill="both", expand=1)

def flight_overview_page(parent):
    root = destroy_all_widgets(parent)
    frame = create_frame(root, 20)
    insert_title(frame, "Flight Schedule Importer")
    insert_flight_overview_buttons(frame)
    insert_table(frame)
    frame.pack(fill="both", expand=1)

def create_flight_page(parent):
    root = destroy_all_widgets(parent)
    frame = create_frame(root, 20)
    insert_title(frame, "Create Flight")
    insert_create_flight_buttons(frame)
    frame.pack(fill="both", expand=1)

def edit_flight_page(parent):
    root = destroy_all_widgets(parent)
    frame = create_frame(root, 20)
    insert_title(frame, "Edit Flight")
    insert_edit_flight_buttons(frame)
    frame.pack(fill="both", expand=1)

# === Widgets ===

def create_frame(parent, padding = 0):
    return ttk.Frame(parent, padding=padding)

def insert_title(parent, text):
    ttk.Label(parent, text=text, font=('Helvetica', 20, 'bold')).pack(fill="x")

def insert_date_time_picker(parent, label):
    dtpicker_frame = create_frame(parent)
    ttk.Label(parent, text=label).pack(pady=10)
    date_entry = DateEntry(dtpicker_frame, values="Text", date_pattern="yyyy-mm-dd")
    date_entry.pack(side="left")
    hour_spin = ttk.Spinbox(dtpicker_frame, from_=0, to=23, width=3, format="%02.0f")
    minute_spin = ttk.Spinbox(dtpicker_frame, from_=0, to=59, width=3, format="%02.0f")
    hour_spin.set("12")
    minute_spin.set("00")
    hour_spin.pack(side="left")
    ttk.Label(dtpicker_frame, text=":").pack(side="left")
    minute_spin.pack(side="left")
    dtpicker_frame.pack()
    return date_entry, hour_spin, minute_spin

# === Flight Overview Widgets ===

def insert_flight_overview_buttons(parent):
    frame = create_frame(parent)
    ttk.Button(frame, text="Upload Flights", command=controller.flight_upload_btn_handler).pack(side="left", pady=10)
    ttk.Button(frame, text="Create Flight", command=lambda:create_flight_page(parent)).pack(side="left", pady=10, padx=10)
    ttk.Button(frame, text="Logout", command=lambda:login_page(parent)).pack(side="right", pady=10)
    frame.pack(fill="x")

def insert_table(parent):
    flight_data = model.load_flight_data()

    columns = ["Flight Carrier", "Flight Number", "Station", "Departure", "Files Expected", "Expected Hours in Advance", ""]
    tree = ttk.Treeview(parent, columns=columns, show="headings")
    tree.pack(side="left", fill="both", expand=1)

    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
    tree.bind("<Double-1>", lambda event: controller.delete_flight(event, parent))

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, anchor="center")
    id = 1
    for flight in flight_data:
        flight.append("Delete")
        tree.insert("", "end", values=flight, iid=id)
        id += 1

# === Login Widgets ===

def insert_login_inputs(parent):
    ttk.Label(parent, text="Username:").pack(pady=10)
    username_entry = ttk.Entry(parent)
    username_entry.pack()

    ttk.Label(parent, text="Password:").pack(pady=10)
    password_entry = ttk.Entry(parent, show="*")
    password_entry.pack()

    ttk.Button(parent, text="Login", command=lambda:controller.login_handler(parent, username_entry.get(), password_entry.get())).pack(pady=10)

# === Create Flight Widgets ===

def insert_create_flight_buttons(parent):
    ttk.Label(parent, text="Carrier:").pack(pady=10)
    carrier_entry = ttk.Entry(parent)
    carrier_entry.pack()

    ttk.Label(parent, text="Flight Number:").pack(pady=10)
    flight_number_entry = ttk.Entry(parent)
    flight_number_entry.pack()

    ttk.Label(parent, text="Station:").pack(pady=10)
    station_entry = ttk.Entry(parent)
    station_entry.pack()

    departure_date, departure_hour, departure_minute = insert_date_time_picker(parent, "Departure:")

    expected_date, expected_hour, expected_minute = insert_date_time_picker(parent, "Expected:")

    btn_frame = create_frame(parent)
    ttk.Button(btn_frame, text="Cancel", command=lambda:flight_overview_page(parent)).pack(side="left", pady=10, padx=10)
    ttk.Button(btn_frame, text="Create", command=lambda:controller.create_flight_btn_handler(parent, carrier_entry.get(), flight_number_entry.get(), station_entry.get(), departure_date.get(), departure_hour.get(), departure_minute.get(), expected_date.get(), expected_hour.get(), expected_minute.get())).pack(side="right", pady=10, padx=10)
    btn_frame.pack()

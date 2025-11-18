from tkinter import ttk

import model
import controller

# === Utils ===

def destroy_all(root):
    """Destroys all child widgets, used for page navigation."""
    children = root.winfo_children()
    for child in children:
        child.destroy()

# === Pages ===

def login_page(parent):
    destroy_all(parent)
    frame = create_frame(parent, 20)
    insert_title(frame, "Login Page")
    insert_login_inputs(frame)
    frame.pack(fill="both", expand=1)

def flight_overview_page(parent):
    destroy_all(parent)
    frame = create_frame(parent, 20)
    insert_title(frame, "Flight Schedule Importer")
    insert_buttons(frame)
    insert_table(frame)
    frame.pack(fill="both", expand=1)

# === Widgets ===

def create_frame(parent, padding = 0):
    return ttk.Frame(parent, padding=padding)

def insert_title(parent, text):
    ttk.Label(parent, text=text, font=('Helvetica', 20, 'bold')).pack(fill="x")

# === Flight Overview Widgets ===

def insert_buttons(parent):
    frame = create_frame(parent)
    ttk.Button(frame, text="Upload Flights", command=controller.flight_upload_btn_handler).pack(side="left", pady=10)
    ttk.Button(frame, text="Logout", command=lambda:login_page(parent)).pack(side="right", pady=10)
    frame.pack(fill="x")

def insert_table(parent):
    flight_data = model.load_flight_data()

    columns = ["Flight Carrier", "Flight Number", "Station", "Departure", "Files Expected", "Expected Hours in Advance"]
    tree = ttk.Treeview(parent, columns=columns, show="headings")
    tree.pack(side="left", fill="both", expand=1)

    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, anchor="center")
    for flight in flight_data:
        tree.insert("", "end", values=flight)

# === Login Widgets ===

def insert_login_inputs(parent):
    ttk.Label(parent, text="Username:").pack(pady=10)
    username_entry = ttk.Entry(parent)
    username_entry.pack()

    ttk.Label(parent, text="Password:").pack(pady=10)
    password_entry = ttk.Entry(parent, show="*")
    password_entry.pack()

    ttk.Button(parent, text="Login", command=lambda:controller.login_handler(parent, username_entry.get(), password_entry.get())).pack(pady=10)
import tkinter as tk
from ui import flight_overview_page

import sv_ttk

root = tk.Tk()
root.title("Flight Schedule Importer")
flight_overview_page(root)

sv_ttk.set_theme("light")

root.mainloop()

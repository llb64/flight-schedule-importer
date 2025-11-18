import tkinter as tk
import sv_ttk

import view

root = tk.Tk()
root.title("Flight Schedule Importer")
view.login_page(root)

sv_ttk.set_theme("light")

root.mainloop()

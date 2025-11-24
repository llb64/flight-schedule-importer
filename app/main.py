import tkinter as tk
import view

root = tk.Tk()
root.title("Flight Schedule Importer")
root.geometry("500x500")
root.minsize(500, 500)
view.login_page(root)

root.mainloop()

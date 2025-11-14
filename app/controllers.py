from tkinter import Tk
from tkinter.filedialog import askopenfilename

def flight_upload_btn_handler():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)

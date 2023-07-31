import ttkbootstrap as ttk
import tkinter as TK
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab


class app(TK.Tk):
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        super().__init__()
        self.title("Image Editor V1")
        self.resizable(0, 0)
        self.geometry("1500x900")
        self.leftFrame = ttk.Frame(self, width=200, height=600)
        self.leftFrame.pack(side="left", fill="y")

        self.canvas = ttk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()

        self.image_filters = ["Sobel Edge Detected", "Color Inversion", "Black and White", "Gaussian Blur"]
        filtercombobox = ttk.Combobox(self.leftFrame, values=self.image_filters, width=15)
        filtercombobox.pack(pady=10, padx=5)

        filtercombobox.bind("<<ComboboxSelected>>", lambda event: self.applyfilter(filtercombobox.get()))

        self.image_icon = ttk.PhotoImage(file='saveicon.png').subsample(12, 12)
        self.loadicon = ttk.PhotoImage(file='loadicon-removebg-preview.png').subsample(12, 12)

        savebutton = ttk.Button(self.leftFrame, image=self.image_icon, bootstyle="light", command=self.print2COnsole)
        savebutton.pack(pady=10)

        loadbutton = ttk.Button(self.leftFrame, image=self.loadicon, bootstyle="light", command=self.print2head)
        loadbutton.pack(pady=10)

       #Write the code to show the image within the GUI

        # self.canvas.create_image(0, 0, anchor='nw', image=)

    def applyfilter(self, grabbedfilter):
        if grabbedfilter == self.image_filters[0]:
            print("Sobel Edge Detector")
        elif grabbedfilter == self.image_filters[1]:
            print("Color Inversion")
        elif grabbedfilter == self.image_filters[2]:
            print("Black and White")
        else:
            print("Gaussian Blur")

    def print2Console(self):
        print("Testing")




if __name__ == "__main__":
    application = app()
    application.mainloop()
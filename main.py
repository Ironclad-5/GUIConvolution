import ttkbootstrap as ttk
import tkinter as TK
import threading
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab

import ImageProcessing

filepath = ""
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

        #Addded threading so that the GUI doesn't hang while the 'extremely' fast image processing occurs
        filtercombobox.bind("<<ComboboxSelected>>", lambda event: threading.Thread(self.applyfilter(filtercombobox.get())))

        self.image_icon = ttk.PhotoImage(file='saveicon.png').subsample(12, 12)
        self.loadicon = ttk.PhotoImage(file='loadicon-removebg-preview.png').subsample(12, 12)

        savebutton = ttk.Button(self.leftFrame, image=self.image_icon, bootstyle="light", command=self.print2Console)
        savebutton.pack(pady=10)

        loadbutton = ttk.Button(self.leftFrame, image=self.loadicon, bootstyle="light", command=self.loadImage)
        loadbutton.pack(pady=10)

       #Write the code to show the image within the GUI

        # self.canvas.create_image(0, 0, anchor='nw', image=)

    def applyfilter(self, grabbedfilter):
        global filepath, photo_image

        if grabbedfilter == self.image_filters[0]:
            img = ImageProcessing.EdgeDetector(filepath)
        elif grabbedfilter == self.image_filters[1]:
            img = ImageProcessing.imageInversion(filepath)
        elif grabbedfilter == self.image_filters[2]:
            img = ImageProcessing.greyscaleimage(filepath)

        new_width = int((self.WIDTH / 2))
        final_image = img.resize((new_width, self.HEIGHT), Image.LANCZOS)

        photo_image = ImageTk.PhotoImage(final_image)
        self.canvas.create_image(0, 0, anchor="nw", image=photo_image)



    def loadImage(self):
        global filepath
        filepath = filedialog.askopenfilename(title="Open Image File", filetypes = [("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
        if filepath:
            global image, photo_image
            image = Image.open(filepath)
            new_width = int((self.WIDTH / 2))
            image = image.resize((new_width, self.HEIGHT), Image.LANCZOS)

            image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor="nw", image=image)


    def print2Console(self):
        print("Testing")








if __name__ == "__main__":
    application = app()
    application.mainloop()

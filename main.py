import ttkbootstrap as ttk
import tkinter as TK
import threading
from tkinter import filedialog
from tkinter.messagebox import showerror, askyesno
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab

import ImageProcessing

filepath = ""
WIDTH = 750
HEIGHT = 560
photo_image = None
filtered_image = None


class app(TK.Tk):
    def __init__(self):

        super().__init__()

        self.title("Image Editor V1")
        self.resizable(0, 0)
        self.geometry("510x580+300+110")
        self.leftFrame = ttk.Frame(self, width=200, height=600)
        self.leftFrame.pack(side="left", fill="y")

        self.canvas = ttk.Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.image_filters = ["Sobel Edge Detected", "Color Inversion", "Black and White", "Gaussian Blur"]
        filtercombobox = ttk.Combobox(self.leftFrame, values=self.image_filters, width=15)
        filtercombobox.pack(pady=5, padx=10)

        # Addded threading so that the GUI doesn't hang while the 'extremely' fast image processing occurs
        filtercombobox.bind("<<ComboboxSelected>>",
                            lambda event: threading.Thread(self.applyfilter(filtercombobox.get())))

        self.image_icon = ttk.PhotoImage(file='saveicon.png').subsample(12, 12)
        self.loadicon = ttk.PhotoImage(file='loadicon-removebg-preview.png').subsample(12, 12)

        savebutton = ttk.Button(self.leftFrame, image=self.image_icon, bootstyle="light", command=self.save_image)
        savebutton.pack(pady=10)

        loadbutton = ttk.Button(self.leftFrame, image=self.loadicon, bootstyle="light", command=self.loadImage)
        loadbutton.pack(pady=10)

    # Write the code to show the image within the GUI

    # self.canvas.create_image(0, 0, anchor='nw', image=)

    def applyfilter(self, grabbedfilter):
        global filepath, photo_image, filtered_image

        if grabbedfilter == self.image_filters[0]:
            img = ImageProcessing.EdgeDetector(filepath)
        elif grabbedfilter == self.image_filters[1]:
            img = ImageProcessing.imageInversion(filepath)
        elif grabbedfilter == self.image_filters[2]:
            img = ImageProcessing.greyscaleimage(filepath)

        new_width = int((WIDTH / 2))
        filtered_image = img.resize((new_width, HEIGHT), Image.LANCZOS)

        photo_image = ImageTk.PhotoImage(filtered_image)
        self.canvas.create_image(0, 0, anchor="nw", image=photo_image)

    def loadImage(self):
        global filepath
        filepath = filedialog.askopenfilename(title="Open Image File",
                                              filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
        if filepath:
            global image, photo_image
            image = Image.open(filepath)
            new_width = int((WIDTH / 2))
            image = image.resize((new_width, HEIGHT), Image.LANCZOS)

            image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor="nw", image=image)

    def save_image(self):
        global filepath, photo_image, image
        self.update()

        if filepath:
            x = self.canvas.winfo_rootx() + 45
            y = self.canvas.winfo_rooty()
            x1 = x + self.canvas.winfo_width() + 1
            y1 = y + self.canvas.winfo_height() + 8

            # create a new PIL Image object from the canvas
            image = filtered_image

        image.show()

        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")

        if filepath:
            if askyesno(title='Save Image', message='Do you want to save this image?'):
                # save the image to a file
                image.save(filepath)


if __name__ == "__main__":
    application = app()
    application.mainloop()

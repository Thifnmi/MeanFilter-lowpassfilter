from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import lowpassfilter
import meanFilter
from tkinter import messagebox
import cv2
import matplotlib.pyplot as plt


canvas_img_origin = None
windows = None
canvas_img_convert = None
combo = None
img = None
path = None


class ImageProcessing(Frame):

    global canvas_img_origin,combo,img,path,windows,canvas_img_convert

    def __init__(self):

        super().__init__()
        self.initUI()
        self.initFrame()
        self.path = None

    def initFrame(self):

        self.combo = ttk.Combobox(windows)
        self.combo['value'] = ("Mean Filter", "Low Pass Filter")
        self.combo.current(0)
        self.combo.pack()
        self.canvas_img_origin = Canvas(windows, width = 400, height= 300)
        self.canvas_img_origin.pack(side="left")
        self.canvas_img_convert = Canvas(windows, width = 400, height= 300)
        self.canvas_img_convert.pack(side="right")

    def initUI(self):

        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Choose Image", command=self.chooseImage)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        run_menu = Menu(menubar)
        menubar.add_command(label="Run", command=self.apply)

    def onExit(self):

        self.quit()

    def chooseImage(self):

        self.path = filedialog.askopenfilename(title = "Choose image")
        self.load_img = Image.open(self.path)
        self.img = ImageTk.PhotoImage(self.load_img)
        Label.image = self.img
        self.canvas_img_origin.create_image(0,0, image = self.img, anchor = tkinter.NW)

    def apply(self):

        global path

        if self.path == None:
            messagebox.showinfo("Warnning", "Please choose image")

        else:

            if self.combo.get() == "Mean Filter":
                self.img1 = cv2.imread(self.path,0)
                self.img_convert = meanFilter.MeanFilter(self.img1, 9)
                self.imgg = ImageTk.PhotoImage(image = Image.fromarray(self.img_convert))
                Label.image = self.imgg
                self.canvas_img_convert.create_image(0,0, image = self.imgg, anchor = tkinter.NW)
                messagebox.showinfo("Complete", "Done")

            elif self.combo.get() == "Low Pass Filter":
                self.img2 = cv2.imread(self.path,0)
                self.img_convertt = lowpassfilter.LowPassFilter(self.img2, 2)
                self.imggg = ImageTk.PhotoImage(image = Image.fromarray(self.img_convertt))
                Label.image = self.imggg
                self.canvas_img_convert.create_image(0,0, image = self.imggg, anchor = tkinter.NW)
                messagebox.showinfo("Complete", "Done")

            else:
                messagebox.showinfo("Warnning", "Algorithm does not exist")

def main():

    global windows
    windows = Tk()
    windows.geometry("800x600")
    windows.title('Xử lý ảnh nhóm 4')
    app = ImageProcessing()
    windows.mainloop()

if __name__ == '__main__':

    main()

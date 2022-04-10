import tkinter as tk
from PIL import Image,ImageTk
import random
import glob

class gui:
    def __init__(self,mainwin):
        self.counter = 0
        self.mainwin = mainwin
        self.mainwin.title("Image Carousel")
        self.mainwin.state("normal")
        self.mainwin.configure(bg="Yellow")
        self.frame = tk.Frame(mainwin)
        self.img = tk.Label(self.frame)
        self.frame.place(relheight=0.85, relwidth=0.9, relx=0.05, rely=0.05)
        self.img.pack()
        self.color()
        self.pic()

    def color(self):
        #  self.colors = ["red","blue","green","orange"]
        #  c = random.choice(self.colors)
         c= "blue"
         self.mainwin.configure(bg=c)
         self.frame.config(bg=c)
         root.after(2000,self.color)
    def pic(self):
        self.pic_list = []
        for name in glob.glob(r'/home/rahul/Desktop/mywork/Images/*'):
            val = name
            self.pic_list.append(val)
        if self.counter == len(self.pic_list)-1:
            self.counter = 0
        else:
            self.counter = self.counter + 1
        self.file = self.pic_list[self.counter]
        self.load = Image.open(self.file)
        self.pic_width = self.load.size[0]
        self.pic_height = self.load.size[1]
        self.real_aspect = self.pic_width/self.pic_height
        self.cal_width = int(self.real_aspect*800)
        # self.load2 = self.load.resize(self.cal_width,800)
        newsize = (1920, 1080)
        self.load2 = self.load.resize(newsize)
        self.render = ImageTk.PhotoImage(self.load2)
        self.img.config(image=self.render)
        self.img.image = self.render
        root.after(3000,self.pic)


root = tk.Tk()
myprog = gui(root)
root.mainloop()
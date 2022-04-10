
from tkinter import *
from tkvideo import tkvideo
import glob

root = Tk()
root.title('Video Player')

video_label = Label(root)
video_label.pack()

counter = 0
video_list = []
# for name in glob.glob(r''):
#     val = name
#     video_list.append(val)

print(4)
player = tkvideo("sample.mp4", video_label,
                    loop = 0, size = (1920, 1080))
player.play()    
root.mainloop()
print(5)
import tkinter as tk
import time
import cv2
import PIL.Image, PIL.ImageTK

# Reference: https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/
# Reference2: https://www.pyimagesearch.com/2016/05/30/displaying-a-video-feed-with-opencv-and-tkinter/
# TK doc: https://docs.python.org/3/library/tk.html
# TK guide: https://likegeeks.com/python-gui-examples-tkinter-tutorial/

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        #self.window.geometry('350x200')
        self.btn = tk.Button(self.window, text="Hide", command=self.hide)
        #self.btn.grid(column=0, row=1)

        # open video source
        self.vid = MyVideoCapture(video_source)
        self.canvas = tk.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # After it is called once, the update method will be automatically called every delay 
        self.delay = 100
        self.update()
        
        self.window.mainloop()
    
    def update(self):
        # Do stuff
        print ("Hi")
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTK.Photo.Image(imag = PIL.Imag.fromarray(frame))
            self.canvas.create_image(0,0,image = self.photo, anchor = tk.NW)
        self.window.after(self.delay, self.update)

    def hide(self):
        self.window.iconify()
        time.sleep(3)
        self.window.deiconify()

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()




a = App(tk.Tk(), "CV testing")
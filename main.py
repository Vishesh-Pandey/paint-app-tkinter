from tkinter import *

root = Tk()
root.title("Paint App")
root.geometry("1100x600")

frame1 = Frame(root , height=100 , width=1100 , bg="red")
frame1.grid(row=0 , column=0, sticky=NW)

toolsFrame = Frame(frame1 , height=100 , width=100 , bg="green")
toolsFrame.grid(row=0 , column=0 )

def usePencil():
    stroke_color.set("black")
    

def useEraser():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX

pencilButton = Button(toolsFrame , text="Pencil" , width=10 , command=usePencil)
pencilButton.grid(row=0 , column=0)

eraserButton = Button(toolsFrame , text="Eraser" , width=10 , command=useEraser)
eraserButton.grid(row=1 , column=0)

toolsLabel = Label(toolsFrame , text="Tools", width=10)
toolsLabel.grid(row=3 , column=0)



frame2 = Frame(root , height=500 , width=1100 , bg="yellow")
frame2.grid(row=1 , column=0)

canvas = Canvas(frame2 , height=500 , width=1100 , bg="white" )
canvas.grid(row=0 , column=0)

stroke_color = StringVar()
stroke_color.set("green")

# variables for pencil 

prevPoint = [0,0]
currentPoint = [0,0] 

def paint(event):
    global prevPoint
    global currentPoint
    x = event.x
    y = event.y
    currentPoint = [x,y]
    # canvas.create_oval(x , y , x +5 , y + 5 , fill="black")

    if prevPoint != [0,0] : 
        canvas.create_line(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1],fill=stroke_color.get())

    prevPoint = currentPoint

    if event.type == "5" :
        prevPoint = [0,0]

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

root.resizable(False , False)
root.mainloop()
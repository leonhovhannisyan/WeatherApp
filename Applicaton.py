import tkinter

HEIGHT = 657
WIDTH = 1500

root = tkinter.Tk()
root.title("Weather Application")

canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
filename = tkinter.PhotoImage(file= "/home/leon/DevelopmentDir/WeatherApp/files/background.png")
bg_label = tkinter.Label(canvas, image=filename)
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
canvas.pack()

frame = tkinter.Frame(canvas)
button = tkinter.Button(frame, text='Check weather!')
button.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
entry = tkinter.Entry(frame)
entry.place(relx=0, rely=0, relwidth=0.9, relheight=1)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)



root.mainloop()
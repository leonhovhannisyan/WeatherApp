import tkinter
import requests

HEIGHT = 657
WIDTH = 1500

# api.openweathermap.org/data/2.5/forecast?id={city ID}&appid=3203c7a72e5efde44ee699c88e1cc019

def test_function(entry):
     print("You typed in: " + entry)

def get_weather(city):
    weather_key = '3203c7a72e5efde44ee699c88e1cc019'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID' : weather_key, 'q' : city, 'units' : 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    # print(weather['list'][0]['main']['temp'])
    # print(weather['list'][0]['weather'][0]['description'])
    # print(weather['city']['name'])




root = tkinter.Tk()
root.title("Weather Application")

canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
filename = tkinter.PhotoImage(file= "/home/leon/DevelopmentDir/WeatherApp/files/background.png")
bg_label = tkinter.Label(canvas, image=filename)
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
canvas.pack()

topFrame = tkinter.Frame(root, bd=5)
entry = tkinter.Entry(topFrame, font='Arial 20 bold')
entry.place(relx=0, rely=0, relwidth=0.85, relheight=1)
button = tkinter.Button(topFrame, text='Check weather!', command=lambda: get_weather(entry.get()))
button.place(relx=0.87, rely=0, relwidth=0.12, relheight=1)
topFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

leftFrame= tkinter.Frame(root, bd=5, bg='white')
leftFrame.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.6)

root.mainloop()
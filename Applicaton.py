import tkinter
import requests

HEIGHT = 657
WIDTH = 1500


def test_function(entry):
     print("You typed in: " + entry)

def weather_output(weather, day):

    try:
        temp = weather['list'][day]['main']['temp']
        descr = weather['list'][day]['weather'][0]['description']
        city = weather['city']['name']
        actualdate = weather['list'][day]['dt_txt']

        output = 'City: %s \nConditions: %s \nTemperature (Celsius): %s \nDate: %s' % (city, descr, temp, actualdate)
    except:
        output = "Please provide correct city name or zip code"

    return output

def get_weather(city):
    weather_key = '3203c7a72e5efde44ee699c88e1cc019'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID' : weather_key, 'q' : city, 'units' : 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    weatherLabel['text'] = weather_output(weather, 0)
    weatherLabel2['text'] = weather_output(weather, 8)
    weatherLabel3['text'] = weather_output(weather, 16)
    weatherLabel4['text'] = weather_output(weather, 24)

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

bottomframe= tkinter.Frame(root, bd=5, bg='#bee7f7')
bottomframe.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

weatherLabel=tkinter.Label(bottomframe)
weatherLabel.place(relx=0, rely=0, relwidth = 1, relheight = 0.22)

weatherLabel2=tkinter.Label(bottomframe, bg='white')
weatherLabel2.place(relx=0, rely=0.25, relwidth = 1, relheight =0.22)
#
weatherLabel3=tkinter.Label(bottomframe)
weatherLabel3.place(relx=0, rely=0.5, relwidth = 1, relheight = 0.22)

weatherLabel4=tkinter.Label(bottomframe, bg='white')
weatherLabel4.place(relx=0, rely=0.75, relwidth = 1, relheight = 0.22)

root.mainloop()
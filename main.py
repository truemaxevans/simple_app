import eel
import pyowm

owm = pyowm.OWM('b0481696676f42778fc41dd6e14843d4')


@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    detail = w.detailed_status

    return 'Location: ' + place + '  ' + str(temp) + 'C ' + 'status: ' + detail


eel.init('web')
eel.start('main.html', size=(700, 700))

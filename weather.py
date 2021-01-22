from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
city = input('Погода какого города вас интересует?: ')
owm = OWM('your-api-key', config_dict) #для получания API ключа: https://home.openweathermap.org/api_keys
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
weather = observation.weather
temperature = weather.temperature('celsius')['temp']
detail = weather.detailed_status

print('В городе ' + city + ' сейчас температура: ' + str(round(temperature)) + u'\xb0C') #Только для кодировки 850(CMD, Win)
print('Так же в указанном городе ' + str(detail))

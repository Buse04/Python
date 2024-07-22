import requests
from dotenv import load_dotenv
import os
from pprint import pprint #pprint prints data much more clean

load_dotenv()

def get_current_temp():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'


    #print(request_url)

    data = requests.get(request_url).json()
    pprint(data) 

get_current_temp()

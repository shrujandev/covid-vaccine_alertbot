import requests
import time
from playsound import playsound

pcode = 576111
date = '10-06-2021'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
    pcode, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

i=0
def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if((each["available_capacity"] > 0) & (each["min_age_limit"] == 18)):
            counter += 1
            print(each["name"])
            print(each["pincode"])
            print(each["vaccine"])
            print(each["available_capacity"])
            playsound('C:/Users/ASUS/Downloads/ding-sound.mp3')
            
    if(counter == 0):
        global i
        i+=1
        print(i," No Available Slots")
        return False


while(findAvailability() != True):
    time.sleep(5)
    findAvailability()
  
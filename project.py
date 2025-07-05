import requests
import json
import user_interface
import output_screen
import sys
    
    
def main():
    info = extract_api()
    temp = temperature(info)
    conditions = condition(info)
    cond = ""
    for i in range(len(conditions)):
        cond += conditions[i]
    date = local_time(info)[0]
    time = local_time(info)[1]
    sky = convert_to_time(local_time(info)[1])
    output_screen.print_screen(sky,temp,cond,date,time)
    

def get_key():  # Get API access key
    with open("keys/key3.txt", "r") as key:
        access_key = key.read().strip()
        return access_key
    

def get_location():  # Input City
    return user_interface.input_screen()


def extract_api():
    url = "http://api.weatherstack.com/current"
    access_key = get_key()
    querystring = get_location()
    
    params = {
        "access_key": access_key,
        "query": querystring
    }

    try:
        info = requests.get(url, params)
        info = info.json()
        # Getting sample response for maintenance/update script (for developer use).
        sample = json.dumps(info, indent=2)
        if "error" in info:
            raise ValueError
        return info
    # Handles some likely to occur users side errors
    except:   
        match info["error"]["code"]:
            case 601:
                sys.exit("Missing city")
            case 615:
                sys.exit("Location doesn't exist")
            case 429:
                sys.exit("API key unavailable. Switch to another key or wait till next month")
            case 101:
                sys.exit("Invalid API key")
            case _:
                sys.exit("Unknown program error")
    
    
def temperature(info):
    return f"{info["current"]["temperature"]}°C"


def condition(info):
    return info["current"]["weather_descriptions"]


def local_time(info):
    date, time = info["location"]["localtime"].split(" ")
    return date, time


# Day/Night time 
def convert_to_time(time):
    hour, minute = time.split(":")
    time_in_number = int(hour) + int(minute)/60
    if 6 <= time_in_number <= 19:
        return "day_time"
    else:
        return "night_time"


if __name__ == "__main__":
    main()

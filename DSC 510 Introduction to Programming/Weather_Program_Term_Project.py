import requests


def get_location():
    """
    Function to obtain latitude and longitude based on user's city/state or zip code input.
    """
    while True:
        location_type = input("Do you want to search by city/state or zip code? (Enter 'city' or 'zip'): ").lower()

        if location_type == 'city':
            city = input("Enter city name: ")
            state = input("Enter state abbreviation: ")
            if city and state:
                location = f"{city},{state}"
                return location
            else:
                print("Error: Please provide both city name and state abbreviation.")
        elif location_type == 'zip':
            zip_code = input("Enter zip code: ")
            if zip_code.isdigit() and len(zip_code) == 5:
                location = zip_code
                return location
            else:
                print("Error: Invalid zip code. Please enter a valid 5-digit zip code.")
        else:
            print("Invalid choice. Please enter 'city' or 'zip'.")


def get_weather_data(location, unit='metric'):
    """
    Function to retrieve weather data from OpenWeatherMap API based on the latitude and longitude.
    """
    api_key = '7aebf0ce4a4e304524d5b61ee0afbf37'
    geocode_url = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&q={location}&appid={api_key}'

    try:
        geocode_response = requests.get(geocode_url)
        geocode_response.raise_for_status()
        geocode_data = geocode_response.json()

        lat = geocode_data['coord']['lat']
        lon = geocode_data['coord']['lon']

        weather_url = (f'http://api.openweathermap.org/data/2.5/forecast?id=524901&lat={lat}&lon={lon}&units={unit}'
                       f'&exclude=minutely,hourly,daily&appid={api_key}')
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        return weather_data

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")


def display_weather_data(weather_data, unit):
    """
    Function to display weather data in a readable format to the user.
    """
    location = weather_data['timezone']
    current_temp = weather_data['current']['temp']
    feels_like_temp = weather_data['current']['feels_like']
    low_temp = weather_data['daily'][0]['temp']['min']
    high_temp = weather_data['daily'][0]['temp']['max']
    pressure = weather_data['current']['pressure']
    humidity = weather_data['current']['humidity']
    weather_description = weather_data['current']['weather'][0]['description']

    print(f"Location: {location}")
    print(f"Current Temperature: {current_temp}°{unit}")
    print(f"Feels Like: {feels_like_temp}°{unit}")
    print(f"Low Temperature: {low_temp}°{unit}")
    print(f"High Temperature: {high_temp}°{unit}")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description.capitalize()}")


def main():
    """
    Main function to interact with the user and display weather data.
    """
    while True:
        location = get_location()

        try:
            unit_choice = input(
                "Choose temperature unit (Enter 'C' for Celsius, 'F' for Fahrenheit, 'K' for Kelvin): ").upper()
            if unit_choice == 'C':
                unit = 'metric'
            elif unit_choice == 'F':
                unit = 'imperial'
            elif unit_choice == 'K':
                unit = 'standard'
            else:
                print("Invalid choice. Using Celsius as default.")
                unit = 'metric'

            weather_data = get_weather_data(location, unit)
            display_weather_data(weather_data, unit)

        except Exception as e:
            print(f"Error: {e}")

        repeat = input("Do you want to check another location? (yes/no): ").lower()
        if repeat != 'yes':
            print("Thank you for using the Weather Forecast App. Goodbye!")
            break


if __name__ == "__main__":
    main()

import json
import sys


def load_data(file_path):
    try:
        with open(file_path, 'r') as file_handler:
            return json.load(file_handler)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def get_name_of_bar(bar_data):
    return bar_data['properties']['Attributes']['Name']


def get_biggest_bar(loaded_data):
    max_seats_bar = max(loaded_data, key=lambda bars: bars['properties']['Attributes']['SeatsCount'])
    print('biggest bar is ' + get_name_of_bar(max_seats_bar))


def get_smallest_bar(loaded_data):
    min_seats_bar = min(loaded_data, key=lambda bars: bars['properties']['Attributes']['SeatsCount'])
    print('smallest bar is ' + get_name_of_bar(min_seats_bar))


def get_closest_bar(loaded_data, longitude, latitude):
    min_distance_bar = min(loaded_data, key=lambda bars: (bars['geometry']['coordinates'][0] - longitude)**2
                           + (bars['geometry']['coordinates'][1] - latitude)**2)
    print('closest bar is ' + get_name_of_bar(min_distance_bar))


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        bars_data = load_data(file_path)['features']

        get_biggest_bar(bars_data)
        get_smallest_bar(bars_data)

        try:
            longitude = float(input('longitude :'))
            latitude = float(input('latitude :'))
            get_closest_bar(bars_data, longitude, latitude)

        except ValueError:
            sys.exit('ERROR : incorrect input')
            
    except FileNotFoundError:
        sys.exit('no files to load from')

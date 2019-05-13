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


def get_biggest_bar(bars_data):
    max_seats_bar = max(
        bars_data,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'])

    return max_seats_bar


def get_smallest_bar(bars_data):
    min_seats_bar = min(
        bars_data,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return min_seats_bar


def get_closest_bar(bars_data, longitude, latitude):
    closest_bar = min(
        bars_data, key=lambda bar:
        (bar['geometry']['coordinates'][0] - longitude)**2
        + (bar['geometry']['coordinates'][1] - latitude)**2)

    return closest_bar


if __name__ == '__main__':

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        sys.exit('ERROR : no file path')

    bars_data = load_data(file_path)
    if not bars_data:
        sys.exit('ERROR : file not found or file not in a json format')
        
    else:
        bars_data_features = load_data(file_path)['features']
        print('THE BIGGEST BAR: {bar}'.format(
            bar=get_name_of_bar(get_biggest_bar(bars_data_features))))
        print('THE SMALLEST BAR: {bar}'.format(
            bar=get_name_of_bar(get_smallest_bar(bars_data_features))))

        try:
            longitude = float(input('longitude :'))
            latitude = float(input('latitude :'))
            print('THE CLOSEST BAR: {bar}'.format(
                bar=get_name_of_bar(get_closest_bar(bars_data_features, longitude, latitude))))

        except ValueError:
            sys.exit('ERROR : incorrect input')

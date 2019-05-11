import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    list_of_seats = [data['features'][index]['properties']['Attributes']['SeatsCount'] for index in
                     range(len(data['features']))]
    max_seats = max(list_of_seats)
    index = list_of_seats.index(max_seats)

    return data['features'][index]['properties']['Attributes'].get('Name')


def get_smallest_bar(data):
    list_of_seats = [data['features'][index]['properties']['Attributes']['SeatsCount'] for index in
                     range(len(data['features']))]
    min_seats = min(list_of_seats)
    index = list_of_seats.index(min_seats)

    return data['features'][index]['properties']['Attributes'].get('Name')


def get_closest_bar(data, longitude, latitude):
    coordinates = [data['features'][index]['geometry']['coordinates'] for index in range(len(data['features']))]
    dist = [(coordinates[index][0] - longitude)**2 + (coordinates[index][1] - latitude)**2 
            for index in range(len(coordinates))]
    index = dist.index(min(dist))
    return data['features'][index]['properties']['Attributes'].get('Name')


if __name__ == '__main__':
    bars_data = load_data("/Users/dns/Desktop/yandex/bars.json")

    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    longitude = float(input("longitude :"))
    latitude = float(input("latitude :"))
    print(get_closest_bar(data, longitude, latitude))

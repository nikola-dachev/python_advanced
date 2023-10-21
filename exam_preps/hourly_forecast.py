def forecast(*args):
    my_dict = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': []
    }
    final_result = ''

    for location, weather in args:
        if weather == 'Sunny':
            my_dict[weather].append(location)

        elif weather == 'Cloudy':
            my_dict[weather].append(location)

        elif weather == 'Rainy':
            my_dict[weather].append(location)

    for weather, locations in my_dict.items():
        if locations:
            for location in sorted(locations):
                final_result += f"{location} - {weather}\n"

    return final_result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

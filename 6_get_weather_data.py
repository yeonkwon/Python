import json

with open('./SeoulKR.json') as data_file: 
        data = json.load(data_file)
        print(data['main'])

        toCelsius = data['main']['temp'] + 273
        weather = data['weather'][0]['main']
        print(toCelsius)
        print(weather)
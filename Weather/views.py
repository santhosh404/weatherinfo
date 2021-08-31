from django.shortcuts import render
import requests


def index(request):
    if request.method == 'POST':
        try: 
            url = "https://community-open-weather-map.p.rapidapi.com/find"

            querystring = {"q":request.POST['city'],"cnt":"5","mode":"null","type":"link, accurate","units":"metric"}
            headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "2f7b24e6cdmsh731e79c46dc1c2ap142676jsnd3803b658253"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            data = response.json()
            print(data) 
            return render(request, 'weather.html', {'City_name' : data['list'][0]['name'],
            'data':data,
            'Temperature' : data['list'][0]['main']['temp'],
            'Humidity' : data['list'][0]['main']['humidity'],
            'Wind_speed' : data['list'][0]['wind']['speed'],
            'Country' : data['list'][0]['sys']['country'],
            'Rain':data['list'][0]['rain'],
            'Weather' : data['list'][0]['weather'][0]['description'],
            'cloud':data['list'][0]['weather'][0]['icon']})
           
        except IndexError:
            return render(request, 'error.html')

    return render(request, 'index.html')
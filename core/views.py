from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    #city = request.GET['city']
    city = request.GET.get('city','Lucknow')

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4a00ef73a75b5c3118d9c929f5e22aec'
    data = requests.get(url).json()
    payload = {'city':data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'Celsius':int(data['main']['temp']-273),
        'pressure':data['main']['pressure'],
        }

    context = {'data':payload}
    return render(request,'home.html',context)
 
from django.shortcuts import render
import requests,json
# Create your views here.

def wheather_view(request):

    data=''
    if request.method=="POST":
        city_name=request.POST.get('city')
        api_key="41b10911485ee0f7106219b9a7b34d92"
        base_url="https://api.openweathermap.org/data/2.5/weather?q="
        
        complete_url=base_url+city_name+"&appid="+api_key+"&units=metric"

        wheather_data=requests.get(complete_url)
        data=wheather_data.json()
    
    return render(request,'display.html',{"data":data})
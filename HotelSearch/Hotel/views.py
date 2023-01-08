from django.shortcuts import render
from . models import Amenities,Hotels
from django.http import JsonResponse
# Create your views here.



def home(request):
    
    amenities = Amenities.objects.all()
    all_hotels = Hotels.objects.all()

    context = {'amenities':amenities,'all_hotels':all_hotels}

    return render(request,'home.html',context)

def hotel_api(request):

    all_hotels = Hotels.objects.all()

    price=request.GET.get('price')
    print(price)
    if price:
        all_hotels = all_hotels.filter(price__lte=price)


    am = request.GET.get('amenities')
    print(type(am))
    if am:
        am1=am.split(',')
        am2=[]
        for i in am1:
            am2.append(int(i))

        print(am2)
        all_hotels= all_hotels.filter(am1__in = am).distinct()

    payload = []
    for hotel in all_hotels:
        result = {}
        result['hotel_name']=hotel.hotel_name
        result['hotel_desc']=hotel.hotel_desc
        result.update({'hotel_image':str(hotel.hotel_image)})
        result['price']=hotel.price

        payload.append(result)

    return JsonResponse(payload,safe=False)

from django.shortcuts import render
from .models import bus


def busbooking(request):
    obj = bus.objects.all()
    return render(request, "index.html", {'result': obj})


def booking(request):
    obj = bus.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        mail = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']

        return render(request, "response.html",
                      {'name': name, 'phone': phone, 'mail': mail, 'date': date, 'time': time})

    return render(request, "booking.html", {'result': obj})


def response(request):
    return render(request, "response.html")

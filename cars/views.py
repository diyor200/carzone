from django.shortcuts import render

# Create your views here.


def cars(requests):
    return render(requests, 'cars/cars.html')

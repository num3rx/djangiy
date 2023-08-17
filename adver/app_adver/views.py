from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisements
from .forms import AdvertisementForm
from django.urls import reverse

# Create your views here.
def index(request):
    advertisements = Advertisements.objects.all()  # тип перем. advertisements - queryset
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement(request):
    return render(request, 'advertisement.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)

    else:
        form = AdvertisementForm()
        context = {'form': form}
        return render(request, 'advertisement-post.html', context)

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')

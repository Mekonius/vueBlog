from django.shortcuts import render
from .models import Achuu_Profile

# Create your views here.
from django.shortcuts import render

def dashboard(request):
    return render(request, "base.html")

def profile_list(request):
    profiles = Achuu_Profile.objects.exclude(user=request.user)
    return render(request, "achuus/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Achuu_Profile.objects.get(pk=pk)
    return render(request, "achuus/profile.html", {"profile": profile})
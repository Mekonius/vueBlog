from django.shortcuts import render
from .models import AchuuProfile

# Create your views here.
from django.shortcuts import render


def dashboard(request):
    return render(request, "base.html")


def profile_list(request):
    achuuProfiles = AchuuProfile.objects.exclude(user=request.user)
    return render(request, "achuus/profile_list.html", {"profiles": achuuProfiles})


def profile(request, pk):
    achuuProfiles = AchuuProfile.objects.get(pk=pk)
    return render(request, "achuus/profile.html", {"profile": achuuProfiles})

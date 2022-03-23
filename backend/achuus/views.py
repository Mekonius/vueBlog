from django.shortcuts import render
from .models import AchuuProfile

# Create your views here.
from django.shortcuts import render


def dashboard(request):
    return render(request, "base.html")


def profile_list(request):
    achuu_Profiles = AchuuProfile.objects.exclude(user=request.user)
    return render(request, "achuus/profile_list.html", {"profiles": achuu_Profiles})


def profile(request, pk):
    achuu_Profiles = AchuuProfile.objects.get(pk=pk)
    return render(request, "achuus/profile.html", {"profile": achuu_Profiles})

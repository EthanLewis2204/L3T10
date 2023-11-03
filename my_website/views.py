from django.shortcuts import render

# Create your views here.
def the_wandering_foot(request):
    return render(request, "the_wandering_foot.html")

def songs(request):
    return render(request, "songs.html")

def gigs(request):
    return render(request, "gigs.html")
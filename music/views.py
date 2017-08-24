from .models import Album
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    """ try:
         album = Album.objects.get(id=album_id)
     except Album.DoesNotExist:
         raise Http404("You have landed on a unknown album page !")"""
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

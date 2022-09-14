from django.shortcuts import render

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html")
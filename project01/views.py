from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Django Project 020421</h1>")
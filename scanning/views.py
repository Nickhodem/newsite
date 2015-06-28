from django.shortcuts import render
from django.http import HttpResponse
'''
def index(request):
    return HttpResponse("Welcome to site about 3D scanning <br/> <a href='/scanning/about'>About</a>")

Po uzyciu htmla z templates:
'''
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Witajcie robaczki!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, '/Documents/newsite/templates/scanning/index.html',context_dict)

def about(request):
    return HttpResponse("This site will be about scanning, photogrammetry and remote sensing <a href='/scanning/'>Index</a>")


def scanners(request):
    return render(request, '/Documents/newsite/templates/scanning/scanners.html')


from django.shortcuts import render
from django.http import HttpResponse
from scanning.models import Category
from scanning.models import Tachymeter, Page


'''
def index(request):
    return HttpResponse("Welcome to site about 3D scanning <br/> <a href='/scanning/about'>About</a>")

Po uzyciu htmla z templates:
'''
def index(request):

    category_list = Page.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, '/Documents/newsite/templates/scanning/index.html',context_dict)

def about(request):
    return HttpResponse("This site will be about scanning, photogrammetry and remote sensing <a href='/scanning/'>Index</a>")


def scanners(request):
    return render(request, '/Documents/newsite/templates/scanning/scanners.html')


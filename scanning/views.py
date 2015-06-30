from django.shortcuts import render
from django.http import HttpResponse

from scanning.models import Page


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

#tworzenie Category view
from scanning.forms import CategoryForm

def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, '/Documents/newsite/templates/scanning/add_category.html', {'form': form})
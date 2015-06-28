import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsite.settings')
<<<<<<< HEAD
import random
import django
django.setup()

from scanning.models import Category, Page, Tachymeter


def populate():
    python_cat = add_cat('Tachymeter')
    add_tachy(cat=python_cat,
        title="Leica 407",
        name="zielony",
        likes=random.randint(0,230),
        url="http://www.gpprague.cz/pl/katalog/4011/Tachimetr_LEICA_TC_407._.html")
    add_tachy(cat=python_cat,
        title="Topcon",
        name='zolty',
        likes=random.randint(0,230),
        url="http://www.tpi.com.pl/")

=======

import django
django.setup()

from scanning.models import Category, Page


def populate():
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
    python_cat = add_cat('Python')

    add_page(cat=python_cat,
        title="Official Python Tutorial",
<<<<<<< HEAD
        likes=random.randint(0,230),
=======
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
<<<<<<< HEAD
        likes=random.randint(0,230),
=======
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
<<<<<<< HEAD
        likes=random.randint(0,230),
=======
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django")

    add_page(cat=django_cat,
        title="Official Django Tutorial",
<<<<<<< HEAD
        likes=random.randint(0,230),
=======
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
<<<<<<< HEAD
        likes=random.randint(0,230),
=======
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
<<<<<<< HEAD
        likes=random.randint(0,230),
=======
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
<<<<<<< HEAD
        likes=random.randint(0,230),
=======
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask",
<<<<<<< HEAD
        likes=random.randint(0,230),
        url="http://flask.pocoo.org")





=======
        url="http://flask.pocoo.org")

>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))
<<<<<<< HEAD
    for c in Category.objects.all():
        for p in Tachymeter.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_tachy(cat, title, url,name, likes, views=0):
    p = Tachymeter.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.name=name
    p.likes=likes
    p.save()
    return p
def add_page(cat, title, url,likes, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.likes=likes
    p.save()
=======

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
        p.url=url
        p.views=views
        p.save()
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Scanning population script..."
    populate()

#  we need to list on all the categories here so that whenever we click on a particular
# category, it will bring us all the products by that category.
# so for this, we will be using a python function called context processors.
# It takes a request as an argument and it will return the dictionary of data as a context.

from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)
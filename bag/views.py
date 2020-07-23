from django.shortcuts import render


# Create your views here.

def view_bag(request):
    """ A view that render the bag cotnent page"""

    return render(request, 'bag/bag.html')

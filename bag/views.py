from django.shortcuts import render


def view_bag(request):
    """ A view to display current bag items """
    
    return render(request, 'bag/bag.html')

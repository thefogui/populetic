from django.shortcuts import render
from .models import Gift

# Create your views here.
def index(request):
    categories = Gift.CATEGORIES
    gifts = Gift.objects.all()
    context = {
        'categories' : categories,
        'gifts' : gifts
    }
    return render(request, 'populetic/index.html', context)